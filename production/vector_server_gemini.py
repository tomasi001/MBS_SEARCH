"""
Vector Search Server for MBS AI Assistant Production Deployment.

This server handles:
- ChromaDB vector database operations
- Gemini API embeddings (gemini-embedding-001) for query-time search
- Semantic search functionality
- Vector database management

Documents are pre-embedded offline. This server only embeds search queries
at runtime using the Gemini free tier API.
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

# Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMBEDDING_MODEL = "models/gemini-embedding-001"
EMBEDDING_DIM = 768
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
gemini_available = False

# Create FastAPI app
app = FastAPI(
    title="MBS AI Assistant - Vector Server",
    description="Vector database and semantic search server",
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
    global vector_client, collection, gemini_available

    logger.info("Initializing vector services...")

    try:
        # Initialize Gemini for query-time embeddings
        if GEMINI_API_KEY:
            genai.configure(api_key=GEMINI_API_KEY)
            gemini_available = True
            logger.info(f"Gemini configured for query embeddings: {EMBEDDING_MODEL}")
        else:
            logger.warning("GEMINI_API_KEY not set - query embeddings unavailable")

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
            logger.info(f"Loaded existing collection: {collection_name} ({collection.count()} docs)")
        except Exception:
            collection = vector_client.create_collection(
                name=collection_name,
                metadata={"description": "MBS codes and descriptions"},
            )
            logger.info(f"Created new collection: {collection_name}")

        logger.info("Vector services initialized successfully")

    except Exception as e:
        logger.error(f"Failed to initialize vector services: {e}")


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


def generate_query_embedding(text: str) -> List[float]:
    """Generate embedding for a search query using Gemini API."""
    if not gemini_available:
        raise Exception("Gemini API not configured")

    result = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=text,
        task_type="RETRIEVAL_QUERY",
        output_dimensionality=EMBEDDING_DIM,
    )

    raw = result["embedding"]
    vec = np.array(raw, dtype=np.float32)
    vec = vec / np.linalg.norm(vec)
    return vec.tolist()


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
        "gemini_embeddings_available": gemini_available,
        "collection_initialized": collection is not None,
        "embedding_model": EMBEDDING_MODEL,
        "stats": stats,
    }


@app.post("/api/vector/search")
async def vector_search(request: Dict[str, Any]):
    """Perform vector search."""
    try:
        if not collection:
            raise HTTPException(status_code=503, detail="Vector database not available")

        if not gemini_available:
            raise HTTPException(status_code=503, detail="Gemini embeddings not available")

        query = request.get("query", "")
        n_results = request.get("n_results", 5)
        filters = request.get("filters")

        if not query:
            raise HTTPException(status_code=400, detail="Query is required")

        logger.info(f"Vector search: '{query}'")

        try:
            query_embedding = generate_query_embedding(query)
        except Exception as e:
            logger.error(f"Failed to generate query embedding: {e}")
            raise HTTPException(status_code=500, detail=f"Failed to generate embedding: {e}")

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
    """Add documents to the vector database."""
    try:
        if not collection:
            raise HTTPException(status_code=503, detail="Vector database not available")

        if not gemini_available:
            raise HTTPException(status_code=503, detail="Gemini embeddings not available")

        documents = request.get("documents", [])
        if not documents:
            raise HTTPException(status_code=400, detail="No documents provided")

        logger.info(f"Adding {len(documents)} documents to vector database")

        ids = []
        texts = []
        metadatas = []

        for doc in documents:
            ids.append(doc["id"])
            texts.append(doc["text"])
            metadatas.append(doc["metadata"])

        # Generate embeddings one at a time via Gemini
        embeddings = []
        for text in texts:
            emb = generate_query_embedding(text)
            embeddings.append(emb)

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
            "embedding_model": EMBEDDING_MODEL,
            "embedding_provider": "gemini",
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting vector stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8002))
    host = "0.0.0.0"

    logger.info(f"Starting Vector server on {host}:{port}")
    logger.info(f"ChromaDB available: {CHROMADB_AVAILABLE}")
    logger.info(f"Gemini available: {gemini_available}")

    uvicorn.run(app, host=host, port=port, log_level="info")
