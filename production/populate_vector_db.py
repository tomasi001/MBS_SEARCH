#!/usr/bin/env python3
"""
Script to populate the vector database with MBS codes using the production vector server.
This script loads MBS data from the SQLite database and sends it to the vector server.
"""

import logging
import sqlite3
import httpx
import asyncio
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
MBS_DB_PATH = "mbs.db"  # Local to production directory
VECTOR_SERVER_URL = "http://localhost:8002"
BATCH_SIZE = 50


def load_mbs_data_from_db() -> List[Dict[str, Any]]:
    """Load MBS data from the SQLite database."""
    logger.info(f"Loading MBS data from {MBS_DB_PATH}")

    documents = []

    try:
        with sqlite3.connect(MBS_DB_PATH) as conn:
            cur = conn.cursor()

            # Get all MBS items
            cur.execute(
                """
                SELECT item_num, category, group_code, schedule_fee, description, 
                       derived_fee, start_date, end_date, provider_type, emsn_description
                FROM items
                WHERE description IS NOT NULL AND description != ''
                ORDER BY item_num
            """
            )

            items = cur.fetchall()
            logger.info(f"Found {len(items)} MBS items with descriptions")

            for item in items:
                item_num = item[0]
                description = item[4] or ""

                # Create description document
                if description:
                    # Filter out None values from metadata
                    metadata = {
                        "item_num": item_num,
                        "chunk_type": "description",
                    }
                    if item[1] is not None:
                        metadata["category"] = item[1]
                    if item[2] is not None:
                        metadata["group_code"] = item[2]
                    if item[3] is not None:
                        metadata["schedule_fee"] = item[3]
                    if item[6] is not None:
                        metadata["start_date"] = item[6]
                    if item[7] is not None:
                        metadata["end_date"] = item[7]
                    if item[8] is not None:
                        metadata["provider_type"] = item[8]

                    documents.append(
                        {
                            "id": f"{item_num}_description",
                            "text": description,
                            "metadata": metadata,
                        }
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
                    relation_text = f"Item {item_num} is related to: "
                    relation_details = []
                    for rel in relations:
                        relation_details.append(f"{rel[0]} {rel[1]} ({rel[2]})")
                    relation_text += "; ".join(relation_details)

                    # Filter out None values from metadata
                    metadata = {
                        "item_num": item_num,
                        "chunk_type": "relations",
                    }
                    if item[1] is not None:
                        metadata["category"] = item[1]
                    if item[2] is not None:
                        metadata["group_code"] = item[2]

                    documents.append(
                        {
                            "id": f"{item_num}_relations",
                            "text": relation_text,
                            "metadata": metadata,
                        }
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
                    constraint_text = f"Item {item_num} constraints: "
                    constraint_details = []
                    for constraint in constraints:
                        constraint_details.append(f"{constraint[0]}: {constraint[1]}")
                    constraint_text += "; ".join(constraint_details)

                    # Filter out None values from metadata
                    metadata = {
                        "item_num": item_num,
                        "chunk_type": "constraints",
                    }
                    if item[1] is not None:
                        metadata["category"] = item[1]
                    if item[2] is not None:
                        metadata["group_code"] = item[2]

                    documents.append(
                        {
                            "id": f"{item_num}_constraints",
                            "text": constraint_text,
                            "metadata": metadata,
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
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{VECTOR_SERVER_URL}/health")
            if response.status_code != 200:
                logger.error("Vector server is not responding")
                return False
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

    async with httpx.AsyncClient(timeout=60.0) as client:
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
        async with httpx.AsyncClient() as client:
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
