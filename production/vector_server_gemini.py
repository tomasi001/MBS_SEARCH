"""
Vector Search Server for MBS AI Assistant Production Deployment.

This server handles:
- ChromaDB vector database operations
- Gemini API embeddings (no local models)
- Semantic search functionality
- Vector database management

This version uses Gemini embeddings to avoid memory issues on free tier.
"""

import logging
import os
import sys
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import google.generativeai as genai
import numpy as np
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration (self-contained)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
USE_GEMINI_EMBEDDINGS = os.getenv("USE_GEMINI_EMBEDDINGS", "true").lower() == "true"
GEMINI_EMBEDDING_MODEL = os.getenv(
    "GEMINI_EMBEDDING_MODEL", "models/text-embedding-004"
)
CHROMA_PERSIST_DIRECTORY = os.getenv("CHROMA_PERSIST_DIRECTORY", "./chroma_db")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Try to import ChromaDB
try:
    import chromadb
    from chromadb.config import Settings

    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False
    logger.warning("ChromaDB not available")

# Global service instances
vector_client = None
collection = None
gemini_client = None

# Create FastAPI app
app = FastAPI(
    title="MBS AI Assistant - Vector Server",
    description="Vector database and semantic search server using Gemini embeddings",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Initialize vector services on startup."""
    global vector_client, collection, gemini_client

    logger.info("Initializing vector services...")

    try:
        # Initialize Gemini client
        if GEMINI_API_KEY and USE_GEMINI_EMBEDDINGS:
            genai.configure(api_key=GEMINI_API_KEY)
            gemini_client = genai
            logger.info("Gemini client initialized successfully")
        else:
            logger.warning("Gemini API key not provided or embeddings disabled")

        # Initialize ChromaDB client
        if not CHROMADB_AVAILABLE:
            raise Exception("ChromaDB not available")

        vector_client = chromadb.PersistentClient(
            path=CHROMA_PERSIST_DIRECTORY,
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True,
            ),
        )

        # Get or create collection
        collection_name = "mbs_codes"
        try:
            collection = vector_client.get_collection(name=collection_name)
            logger.info(f"Loaded existing collection: {collection_name}")
        except Exception:
            collection = vector_client.create_collection(
                name=collection_name,
                metadata={"description": "MBS codes and descriptions"},
            )
            logger.info(f"Created new collection: {collection_name}")

        logger.info("Vector services initialized successfully")

    except Exception as e:
        logger.error(f"Failed to initialize vector services: {e}")
        # Continue without vector services


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all requests."""
    import time

    start = time.time()
    response = await call_next(request)
    duration = (time.time() - start) * 1000
    logger.info(
        f"{request.method} {request.url.path} - {response.status_code} - {duration:.1f}ms"
    )
    return response


def generate_embeddings(texts: List[str]) -> List[List[float]]:
    """Generate embeddings using Gemini API."""
    if not gemini_client:
        raise Exception("Gemini client not initialized")

    try:
        # Process texts one at a time to ensure we get one embedding per text
        embeddings = []
        for text in texts:
            result = genai.embed_content(
                model=GEMINI_EMBEDDING_MODEL,
                content=text,
                task_type="RETRIEVAL_QUERY",
                output_dimensionality=768,  # Smaller dimension to save space
            )
            
            # Extract embedding and normalize it
            if "embeddings" in result:
                embedding_values = result["embeddings"][0]
            elif "embedding" in result:
                embedding_values = result["embedding"]
            else:
                # Try to get the first value that looks like an embedding
                for key, value in result.items():
                    if isinstance(value, list) and len(value) > 0:
                        embedding_values = value[0] if isinstance(value[0], list) else value
                        break
                else:
                    raise Exception(f"Could not find embedding in response: {result}")
            
            # Handle nested embedding structure
            if isinstance(embedding_values, list) and len(embedding_values) > 0 and isinstance(embedding_values[0], list):
                # If it's nested, flatten it
                embedding_values = embedding_values[0]
            
            # Normalize the embedding
            normed_embedding = np.array(embedding_values) / np.linalg.norm(embedding_values)
            embeddings.append(normed_embedding.tolist())
        
        logger.info(f"Generated {len(embeddings)} embeddings using Gemini API")
        return embeddings

    except Exception as e:
        logger.error(f"Error generating embeddings: {e}")
        raise


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    stats = None
    if collection:
        try:
            count = collection.count()
            stats = {"total_documents": count}
        except Exception as e:
            logger.warning(f"Could not get collection stats: {e}")

    return {
        "status": "healthy",
        "message": "Vector server is running",
        "server": "vector",
        "chromadb_available": CHROMADB_AVAILABLE,
        "gemini_embeddings_available": gemini_client is not None,
        "collection_initialized": collection is not None,
        "embedding_model": GEMINI_EMBEDDING_MODEL,
        "stats": stats,
    }


@app.post("/api/vector/search")
async def vector_search(request: Dict[str, Any]):
    """Perform vector search using Gemini embeddings."""
    try:
        if not collection:
            raise HTTPException(status_code=503, detail="Vector database not available")

        if not gemini_client:
            raise HTTPException(
                status_code=503, detail="Gemini embeddings not available"
            )

        query = request.get("query", "")
        n_results = request.get("n_results", 5)
        filters = request.get("filters")

        if not query:
            raise HTTPException(status_code=400, detail="Query is required")

        logger.info(f"Vector search: '{query}'")

        # Generate query embedding using Gemini
        try:
            query_embeddings = generate_embeddings([query])
            query_embedding = query_embeddings[0]
            logger.info("Generated query embedding using Gemini API")
        except Exception as e:
            logger.error(f"Failed to generate query embedding: {e}")
            raise HTTPException(
                status_code=500, detail=f"Failed to generate embedding: {e}"
            )

        # Perform search
        where_clause = filters if filters else None
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            where=where_clause,
        )

        # Format results
        formatted_results = []
        if results and results["ids"]:
            for i in range(len(results["ids"][0])):
                formatted_results.append(
                    {
                        "id": results["ids"][0][i],
                        "document": results["documents"][0][i],
                        "metadata": results["metadatas"][0][i],
                        "distance": results["distances"][0][i],
                        "similarity_score": 1 - results["distances"][0][i],
                    }
                )

        logger.info(f"Found {len(formatted_results)} vector search results")
        return {"results": formatted_results}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error performing vector search: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/vector/add")
async def add_documents(request: Dict[str, Any]):
    """Add documents to the vector database using Gemini embeddings."""
    try:
        if not collection:
            raise HTTPException(status_code=503, detail="Vector database not available")

        if not gemini_client:
            raise HTTPException(
                status_code=503, detail="Gemini embeddings not available"
            )

        documents = request.get("documents", [])
        if not documents:
            raise HTTPException(status_code=400, detail="No documents provided")

        logger.info(f"Adding {len(documents)} documents to vector database")

        # Extract data
        ids = []
        texts = []
        metadatas = []

        for doc in documents:
            ids.append(doc["id"])
            texts.append(doc["text"])
            metadatas.append(doc["metadata"])

        # Generate embeddings using Gemini
        try:
            embeddings = generate_embeddings(texts)
            logger.info(f"Generated {len(embeddings)} embeddings using Gemini API")
        except Exception as e:
            logger.error(f"Failed to generate embeddings: {e}")
            raise HTTPException(
                status_code=500, detail=f"Failed to generate embeddings: {e}"
            )

        # Add to collection
        collection.add(
            ids=ids, embeddings=embeddings, documents=texts, metadatas=metadatas
        )

        logger.info(f"Added {len(documents)} documents to ChromaDB")
        return {"success": True, "count": len(documents)}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error adding documents: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/vector/stats")
async def get_vector_stats():
    """Get vector database statistics."""
    try:
        if not collection:
            raise HTTPException(status_code=503, detail="Vector database not available")

        count = collection.count()
        return {
            "total_documents": count,
            "collection_name": collection.name,
            "embedding_model": GEMINI_EMBEDDING_MODEL,
            "embedding_provider": "gemini",
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting vector stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    # Use PORT environment variable for Render compatibility
    port = int(os.environ.get("PORT", 8002))
    host = "0.0.0.0"  # Required for Render

    logger.info(f"Starting Vector server on {host}:{port}")
    logger.info(f"ChromaDB available: {CHROMADB_AVAILABLE}")
    logger.info(f"Gemini embeddings available: {gemini_client is not None}")

    uvicorn.run(app, host=host, port=port, log_level="info")
