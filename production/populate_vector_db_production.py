#!/usr/bin/env python3
"""
Production script to populate the vector database with MBS codes.
This script is designed to run in the production environment after deployment.
"""

import logging
import sqlite3
import httpx
import asyncio
import os
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
MBS_DB_PATH = "mbs.db"  # Local to production directory
VECTOR_SERVER_URL = os.getenv("VECTOR_SERVER_URL", "http://localhost:8002")
BATCH_SIZE = 25  # Smaller batches for production API limits


def load_mbs_data_from_db() -> List[Dict[str, Any]]:
    """Load MBS data from the SQLite database."""
    logger.info(f"Loading MBS data from {MBS_DB_PATH}")

    if not os.path.exists(MBS_DB_PATH):
        logger.error(f"MBS database not found at {MBS_DB_PATH}")
        return []

    documents = []

    try:
        with sqlite3.connect(MBS_DB_PATH) as conn:
            cur = conn.cursor()

            # Get all MBS items with descriptions
            cur.execute(
                """
                SELECT item_num, category, group_code, schedule_fee, description, 
                       derived_fee, start_date, end_date, provider_type, emsn_description
                FROM items
                WHERE description IS NOT NULL AND description != ''
                ORDER BY item_num
                LIMIT 1000
            """
            )

            items = cur.fetchall()
            logger.info(f"Found {len(items)} MBS items with descriptions")

            for item in items:
                item_num = item[0]
                description = item[4] or ""

                # Create description document
                if description:
                    documents.append(
                        {
                            "id": f"{item_num}_description",
                            "text": description,
                            "metadata": {
                                "item_num": item_num,
                                "chunk_type": "description",
                                "category": item[1],
                                "group_code": item[2],
                                "schedule_fee": item[3],
                                "start_date": item[6],
                                "end_date": item[7],
                                "provider_type": item[8],
                            },
                        }
                    )

            logger.info(f"Generated {len(documents)} documents for vector database")
            return documents

    except Exception as e:
        logger.error(f"Error loading MBS data: {e}")
        return []


async def populate_vector_database():
    """Populate the vector database via the vector server API."""
    logger.info("Starting vector database population...")

    # Check if vector server is running
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(f"{VECTOR_SERVER_URL}/health")
            if response.status_code != 200:
                logger.error(f"Vector server is not responding: {response.status_code}")
                return False
            logger.info("Vector server is healthy")
    except Exception as e:
        logger.error(f"Cannot connect to vector server: {e}")
        return False

    # Load MBS data
    documents = load_mbs_data_from_db()
    if not documents:
        logger.error("No documents to populate")
        return False

    # Process in batches
    total_batches = (len(documents) + BATCH_SIZE - 1) // BATCH_SIZE
    logger.info(f"Processing {len(documents)} documents in {total_batches} batches")

    async with httpx.AsyncClient(timeout=120.0) as client:
        for batch_idx in range(total_batches):
            start_idx = batch_idx * BATCH_SIZE
            end_idx = min(start_idx + BATCH_SIZE, len(documents))
            batch_documents = documents[start_idx:end_idx]

            logger.info(
                f"Processing batch {batch_idx + 1}/{total_batches} ({len(batch_documents)} documents)"
            )

            try:
                response = await client.post(
                    f"{VECTOR_SERVER_URL}/api/vector/add",
                    json={"documents": batch_documents},
                )

                if response.status_code == 200:
                    result = response.json()
                    logger.info(f"Successfully added batch {batch_idx + 1}: {result}")
                else:
                    logger.error(
                        f"Failed to add batch {batch_idx + 1}: {response.status_code} - {response.text}"
                    )
                    return False

            except Exception as e:
                logger.error(f"Error adding batch {batch_idx + 1}: {e}")
                return False

    # Get final stats
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(f"{VECTOR_SERVER_URL}/health")
            if response.status_code == 200:
                stats = response.json()
                logger.info(f"Vector database population complete!")
                logger.info(
                    f"Total documents: {stats.get('stats', {}).get('total_documents', 0)}"
                )
    except Exception as e:
        logger.warning(f"Could not get final stats: {e}")

    return True


if __name__ == "__main__":
    asyncio.run(populate_vector_database())
