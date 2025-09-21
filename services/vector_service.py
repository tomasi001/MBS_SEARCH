"""
Vector service for MBS AI Assistant MVP.

This module handles ChromaDB operations for vector storage and semantic search.
"""

import logging
import os
from typing import Any, Dict, List, Optional
import chromadb
from chromadb.config import Settings

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings
from services.gemini_service import GeminiService

logger = logging.getLogger(__name__)

# Try to import sentence-transformers for local embeddings
try:
    from sentence_transformers import SentenceTransformer

    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False
    logger.warning("sentence-transformers not available. Local embeddings disabled.")


class VectorService:
    """Service for vector database operations using ChromaDB."""

    def __init__(self):
        """Initialize the vector service."""
        self.persist_directory = settings.CHROMA_PERSIST_DIRECTORY
        self.collection_name = "mbs_codes"
        self.gemini_service = GeminiService()

        # Initialize local embedding model if available and configured
        self.local_embedding_model = None
        if settings.USE_LOCAL_EMBEDDINGS and SENTENCE_TRANSFORMERS_AVAILABLE:
            try:
                self.local_embedding_model = SentenceTransformer(
                    settings.LOCAL_EMBEDDING_MODEL
                )
                logger.info(
                    f"Local embedding model loaded: {settings.LOCAL_EMBEDDING_MODEL}"
                )
            except Exception as e:
                logger.warning(f"Failed to load local embedding model: {e}")
                self.local_embedding_model = None

        # Initialize ChromaDB client
        self.client = chromadb.PersistentClient(
            path=self.persist_directory,
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True,
            ),
        )

        # Get or create collection
        try:
            self.collection = self.client.get_collection(name=self.collection_name)
            logger.info(f"Loaded existing collection: {self.collection_name}")
        except Exception:
            self.collection = self.client.create_collection(
                name=self.collection_name,
                metadata={"description": "MBS codes and descriptions"},
            )
            logger.info(f"Created new collection: {self.collection_name}")

        logger.info("Vector service initialized successfully")

    def add_documents(self, documents: List[Dict[str, Any]]) -> bool:
        """Add documents to the vector database."""
        try:
            if not documents:
                logger.warning("No documents to add")
                return False

            # Prepare data for ChromaDB
            ids = []
            texts = []
            metadatas = []

            for doc in documents:
                ids.append(doc["id"])
                texts.append(doc["content"])

                # Filter out None values for ChromaDB compatibility
                metadata = {k: v for k, v in doc["metadata"].items() if v is not None}
                metadatas.append(metadata)

            # Generate embeddings using Gemini or local model
            logger.info(f"Generating embeddings for {len(texts)} documents...")

            if self.local_embedding_model:
                try:
                    embeddings = self.local_embedding_model.encode(texts)
                    embeddings = embeddings.tolist()
                    logger.info(
                        f"Generated {len(embeddings)} embeddings using local model"
                    )
                except Exception as e:
                    logger.warning(
                        f"Local embedding failed, falling back to Gemini: {e}"
                    )
                    embeddings = self.gemini_service.get_embeddings(texts)
            else:
                embeddings = self.gemini_service.get_embeddings(texts)

            # Add to collection
            self.collection.add(
                ids=ids, embeddings=embeddings, documents=texts, metadatas=metadatas
            )

            logger.info(
                f"Successfully added {len(documents)} documents to vector database"
            )
            return True

        except Exception as e:
            logger.error(f"Error adding documents to vector database: {e}")
            return False

    def search(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        """Search the vector database."""
        try:
            logger.info(f"Searching vector database: '{query}'")

            # Generate query embedding using Gemini or local model
            if self.local_embedding_model:
                try:
                    query_embedding = self.local_embedding_model.encode([query])[
                        0
                    ].tolist()
                    logger.info("Generated query embedding using local model")
                except Exception as e:
                    logger.warning(
                        f"Local embedding failed, falling back to Gemini: {e}"
                    )
                    query_embeddings = self.gemini_service.get_embeddings([query])
                    query_embedding = query_embeddings[0]
            else:
                query_embeddings = self.gemini_service.get_embeddings([query])
                query_embedding = query_embeddings[0]

            # Prepare where clause for filtering
            where_clause = {}
            if filters:
                for key, value in filters.items():
                    where_clause[key] = value

            # Perform search
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=max_results,
                where=where_clause if where_clause else None,
                include=["documents", "metadatas", "distances"],
            )

            # Convert results to our format
            search_results = []
            if results["documents"] and results["documents"][0]:
                for i, (doc, metadata, distance) in enumerate(
                    zip(
                        results["documents"][0],
                        results["metadatas"][0],
                        results["distances"][0],
                    )
                ):
                    # Convert distance to similarity score (ChromaDB uses cosine distance)
                    similarity_score = 1 - distance

                    search_results.append(
                        {
                            "id": metadata.get("id", f"result_{i}"),
                            "content": doc,
                            "metadata": metadata,
                            "similarity_score": similarity_score,
                            "distance": distance,
                        }
                    )

            logger.info(f"Found {len(search_results)} results")
            return search_results

        except Exception as e:
            logger.error(f"Error searching vector database: {e}")
            return []

    def get_collection_stats(self) -> Dict[str, Any]:
        """Get statistics about the collection."""
        try:
            count = self.collection.count()

            # Get sample of metadata to understand data distribution
            sample_results = self.collection.get(limit=100, include=["metadatas"])

            chunk_types = {}
            item_nums = set()

            if sample_results["metadatas"]:
                for metadata in sample_results["metadatas"]:
                    chunk_type = metadata.get("chunk_type", "unknown")
                    chunk_types[chunk_type] = chunk_types.get(chunk_type, 0) + 1
                    item_nums.add(metadata.get("item_num", ""))

            return {
                "total_documents": count,
                "unique_items_in_sample": len(item_nums),
                "chunk_types_in_sample": chunk_types,
                "persist_directory": self.persist_directory,
                "collection_name": self.collection_name,
                "embedding_model": settings.GEMINI_EMBEDDING_MODEL,
            }

        except Exception as e:
            logger.error(f"Error getting collection stats: {e}")
            return {"error": str(e)}

    def reset_collection(self) -> bool:
        """Reset the collection (delete all documents)."""
        try:
            self.client.delete_collection(name=self.collection_name)
            self.collection = self.client.create_collection(
                name=self.collection_name,
                metadata={"description": "MBS codes and descriptions"},
            )
            logger.info("Collection reset successfully")
            return True

        except Exception as e:
            logger.error(f"Error resetting collection: {e}")
            return False
