"""
Vector database service for MBS Clarity AI assistant.

This module handles vector database operations, embedding generation,
and semantic search capabilities using ChromaDB and OpenAI embeddings.
"""

import logging
import os
import uuid
from typing import Any, Dict, List, Optional, Tuple

import chromadb
import numpy as np
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

from mbs_clarity.ai_models import (
    AIConfig,
    EmbeddingModel,
    MBSChunk,
    SearchResult,
    SearchType,
)
from mbs_clarity.db import fetch_item_aggregate, get_conn

logger = logging.getLogger(__name__)


class VectorDatabaseService:
    """Service for managing vector database operations."""

    def __init__(self, config: AIConfig):
        """Initialize the vector database service."""
        self.config = config
        self.client = None
        self.collection = None
        self.embedding_model = None
        self._initialize_client()
        self._initialize_embedding_model()

    def _initialize_client(self) -> None:
        """Initialize ChromaDB client."""
        try:
            # Create directory if it doesn't exist
            os.makedirs(self.config.vector_db_path, exist_ok=True)

            self.client = chromadb.PersistentClient(
                path=self.config.vector_db_path,
                settings=Settings(
                    anonymized_telemetry=False,
                    allow_reset=True,
                ),
            )

            # Get or create collection
            try:
                self.collection = self.client.get_collection(
                    name=self.config.collection_name
                )
                logger.info(
                    f"Loaded existing collection: {self.config.collection_name}"
                )
            except Exception:
                self.collection = self.client.create_collection(
                    name=self.config.collection_name,
                    metadata={"description": "MBS codes and descriptions"},
                )
                logger.info(f"Created new collection: {self.config.collection_name}")

        except Exception as e:
            logger.error(f"Failed to initialize ChromaDB client: {e}")
            raise

    def _initialize_embedding_model(self) -> None:
        """Initialize the embedding model."""
        try:
            if self.config.embedding_model == EmbeddingModel.SENTENCE_TRANSFORMERS:
                self.embedding_model = SentenceTransformer(
                    "sentence-transformers/all-MiniLM-L6-v2"
                )
                logger.info("Initialized sentence-transformers embedding model")
            else:
                # OpenAI embeddings will be handled in the embedding service
                self.embedding_model = None
                logger.info("Using OpenAI embeddings (no local model needed)")

        except Exception as e:
            logger.error(f"Failed to initialize embedding model: {e}")
            raise

    def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts."""
        if self.config.embedding_model == EmbeddingModel.SENTENCE_TRANSFORMERS:
            if not self.embedding_model:
                raise RuntimeError("Sentence transformer model not initialized")

            embeddings = self.embedding_model.encode(texts)
            return embeddings.tolist()
        else:
            # For OpenAI embeddings, we'll use the OpenAI service
            from mbs_clarity.openai_service import OpenAIService

            openai_service = OpenAIService(self.config)
            return openai_service.generate_embeddings(texts)

    def chunk_mbs_data(self) -> List[MBSChunk]:
        """Chunk MBS data for vector storage."""
        logger.info("Chunking MBS data for vector storage...")
        chunks = []

        with get_conn() as conn:
            cur = conn.cursor()

            # Get all items with their relations and constraints
            cur.execute(
                """
                SELECT 
                    i.item_num,
                    i.category,
                    i.group_code,
                    i.schedule_fee,
                    i.description,
                    i.derived_fee,
                    i.start_date,
                    i.end_date,
                    i.provider_type,
                    i.emsn_description
                FROM items i
                ORDER BY CAST(i.item_num AS INTEGER)
            """
            )

            items = cur.fetchall()
            logger.info(f"Processing {len(items)} items for chunking")

            for item in items:
                item_num = item[0]
                description = item[4] or ""

                # Create description chunk
                if description:
                    chunks.append(
                        MBSChunk(
                            item_num=item_num,
                            chunk_id=f"{item_num}_description",
                            content=description,
                            chunk_type="description",
                            metadata={
                                "category": item[1],
                                "group_code": item[2],
                                "schedule_fee": item[3],
                                "start_date": item[6],
                                "end_date": item[7],
                                "provider_type": item[8],
                            },
                        )
                    )

                # Get relations for this item
                cur.execute(
                    """
                    SELECT relation_type, target_item_num, detail
                    FROM relations
                    WHERE item_num = ?
                """,
                    (item_num,),
                )

                relations = cur.fetchall()
                if relations:
                    relation_text = "Relations: " + "; ".join(
                        [
                            f"{rel[0]} {rel[1] or 'general'}"
                            + (f" ({rel[2]})" if rel[2] else "")
                            for rel in relations
                        ]
                    )

                    chunks.append(
                        MBSChunk(
                            item_num=item_num,
                            chunk_id=f"{item_num}_relations",
                            content=relation_text,
                            chunk_type="relations",
                            metadata={"relation_count": len(relations)},
                        )
                    )

                # Get constraints for this item
                cur.execute(
                    """
                    SELECT constraint_type, value
                    FROM constraints
                    WHERE item_num = ?
                """,
                    (item_num,),
                )

                constraints = cur.fetchall()
                if constraints:
                    constraint_text = "Constraints: " + "; ".join(
                        [f"{con[0]}: {con[1]}" for con in constraints]
                    )

                    chunks.append(
                        MBSChunk(
                            item_num=item_num,
                            chunk_id=f"{item_num}_constraints",
                            content=constraint_text,
                            chunk_type="constraints",
                            metadata={"constraint_count": len(constraints)},
                        )
                    )

        logger.info(f"Created {len(chunks)} chunks from MBS data")
        return chunks

    def populate_vector_db(self) -> None:
        """Populate the vector database with MBS data."""
        logger.info("Populating vector database with MBS data...")

        # Check if collection already has data
        try:
            count = self.collection.count()
            if count > 0:
                logger.info(f"Vector database already has {count} documents")
                return
        except Exception:
            pass

        # Generate chunks
        chunks = self.chunk_mbs_data()

        if not chunks:
            logger.warning("No chunks generated from MBS data")
            return

        # Generate embeddings in batches
        batch_size = self.config.batch_size
        total_batches = (len(chunks) + batch_size - 1) // batch_size

        logger.info(
            f"Generating embeddings for {len(chunks)} chunks in {total_batches} batches"
        )

        for batch_idx in range(total_batches):
            start_idx = batch_idx * batch_size
            end_idx = min(start_idx + batch_size, len(chunks))
            batch_chunks = chunks[start_idx:end_idx]

            logger.info(
                f"Processing batch {batch_idx + 1}/{total_batches} ({len(batch_chunks)} chunks)"
            )

            # Generate embeddings for this batch
            texts = [chunk.content for chunk in batch_chunks]
            embeddings = self.generate_embeddings(texts)

            # Prepare data for ChromaDB
            ids = [chunk.chunk_id for chunk in batch_chunks]
            documents = [chunk.content for chunk in batch_chunks]
            metadatas = []

            for chunk in batch_chunks:
                metadata = {
                    "item_num": chunk.item_num,
                    "chunk_type": chunk.chunk_type,
                    **chunk.metadata,
                }
                # Filter out None values for ChromaDB compatibility
                metadata = {k: v for k, v in metadata.items() if v is not None}
                metadatas.append(metadata)

            # Add to collection
            self.collection.add(
                ids=ids, embeddings=embeddings, documents=documents, metadatas=metadatas
            )

            logger.info(f"Added batch {batch_idx + 1} to vector database")

        logger.info(f"Successfully populated vector database with {len(chunks)} chunks")

    def search(
        self,
        query: str,
        search_type: SearchType = SearchType.SEMANTIC,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[SearchResult]:
        """Search the vector database."""
        logger.info(f"Searching vector database: '{query}' (type: {search_type})")

        try:
            # Generate query embedding
            query_embedding = self.generate_embeddings([query])[0]

            # Prepare where clause for filtering
            where_clause = {}
            if filters:
                for key, value in filters.items():
                    where_clause[key] = value

            # Perform search
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=min(max_results, self.config.max_search_results),
                where=where_clause if where_clause else None,
                include=["documents", "metadatas", "distances"],
            )

            # Convert results to SearchResult objects
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

                    if similarity_score >= self.config.similarity_threshold:
                        search_results.append(
                            SearchResult(
                                item_num=metadata["item_num"],
                                score=similarity_score,
                                content=doc,
                                chunk_type=metadata["chunk_type"],
                                metadata=metadata,
                            )
                        )

            logger.info(f"Found {len(search_results)} results above threshold")
            return search_results

        except Exception as e:
            logger.error(f"Error searching vector database: {e}")
            return []

    def get_item_chunks(self, item_num: str) -> List[MBSChunk]:
        """Get all chunks for a specific MBS item."""
        try:
            results = self.collection.get(
                where={"item_num": item_num}, include=["documents", "metadatas"]
            )

            chunks = []
            if results["documents"]:
                for doc, metadata in zip(results["documents"], results["metadatas"]):
                    chunks.append(
                        MBSChunk(
                            item_num=metadata["item_num"],
                            chunk_id=metadata.get("id", ""),
                            content=doc,
                            chunk_type=metadata["chunk_type"],
                            metadata=metadata,
                        )
                    )

            return chunks

        except Exception as e:
            logger.error(f"Error getting chunks for item {item_num}: {e}")
            return []

    def reset_database(self) -> None:
        """Reset the vector database."""
        logger.info("Resetting vector database...")
        try:
            self.client.delete_collection(self.config.collection_name)
            self.collection = self.client.create_collection(
                name=self.config.collection_name,
                metadata={"description": "MBS codes and descriptions"},
            )
            logger.info("Vector database reset successfully")
        except Exception as e:
            logger.error(f"Error resetting vector database: {e}")
            raise

    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about the vector database."""
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
                "total_chunks": count,
                "unique_items": len(item_nums),
                "chunk_types": chunk_types,
                "collection_name": self.config.collection_name,
                "embedding_model": self.config.embedding_model.value,
            }

        except Exception as e:
            logger.error(f"Error getting vector database stats: {e}")
            return {"error": str(e)}
