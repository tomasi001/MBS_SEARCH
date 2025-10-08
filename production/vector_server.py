"""
Vector Search Server for MBS AI Assistant Production Deployment.

This server handles:
- ChromaDB vector database operations
- Sentence transformers for embeddings
- Semantic search functionality
- Vector database management
"""

import logging
import os
import sys
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Try to import ChromaDB and sentence-transformers
try:
    import chromadb
    from chromadb.config import Settings

    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False
    logger.warning("ChromaDB not available")

try:
    from sentence_transformers import SentenceTransformer

    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False
    logger.warning("sentence-transformers not available")

# Global service instances
vector_client = None
collection = None
embedding_model = None

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
    global vector_client, collection, embedding_model

    logger.info("Initializing vector services...")

    try:
        if not CHROMADB_AVAILABLE:
            raise Exception("ChromaDB not available")

        # Initialize ChromaDB client
        vector_client = chromadb.PersistentClient(
            path=settings.CHROMA_PERSIST_DIRECTORY,
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

        # Initialize embedding model if available
        if SENTENCE_TRANSFORMERS_AVAILABLE and settings.USE_LOCAL_EMBEDDINGS:
            try:
                embedding_model = SentenceTransformer(settings.LOCAL_EMBEDDING_MODEL)
                logger.info(f"Loaded embedding model: {settings.LOCAL_EMBEDDING_MODEL}")
            except Exception as e:
                logger.warning(f"Failed to load embedding model: {e}")

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
        "sentence_transformers_available": SENTENCE_TRANSFORMERS_AVAILABLE,
        "collection_initialized": collection is not None,
        "embedding_model_loaded": embedding_model is not None,
        "stats": stats,
    }


@app.post("/api/vector/search")
async def vector_search(request: Dict[str, Any]):
    """Perform vector search."""
    try:
        if not collection:
            raise HTTPException(status_code=503, detail="Vector database not available")

        query = request.get("query", "")
        n_results = request.get("n_results", 5)
        filters = request.get("filters")

        if not query:
            raise HTTPException(status_code=400, detail="Query is required")

        logger.info(f"Vector search: '{query}'")

        # Generate query embedding
        query_embedding = None
        if embedding_model:
            try:
                query_embedding = embedding_model.encode([query])[0].tolist()
                logger.info("Generated query embedding using local model")
            except Exception as e:
                logger.warning(f"Local embedding failed: {e}")

        # If no local embedding, would need to use Gemini API
        if not query_embedding:
            # For now, return empty results
            logger.warning("No embedding available, returning empty results")
            return {"results": []}

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
                        "similarity_score": 1
                        - results["distances"][0][i],  # Convert distance to similarity
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

        # Generate embeddings
        embeddings = None
        if embedding_model:
            try:
                embeddings = embedding_model.encode(texts).tolist()
                logger.info(f"Generated {len(embeddings)} embeddings using local model")
            except Exception as e:
                logger.warning(f"Local embedding failed: {e}")

        if not embeddings:
            raise HTTPException(status_code=500, detail="Could not generate embeddings")

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
            "embedding_model": (
                settings.LOCAL_EMBEDDING_MODEL if embedding_model else None
            ),
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
    logger.info(f"Sentence transformers available: {SENTENCE_TRANSFORMERS_AVAILABLE}")

    uvicorn.run(app, host=host, port=port, log_level="info")
