#!/usr/bin/env python3
"""
Script to resume populating the vector database from a specific batch.
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
START_BATCH = 100  # Resume from batch 100


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


async def resume_populate_vector_database():
    """Resume populating the vector database from a specific batch."""
    logger.info(f"Resuming vector database population from batch {START_BATCH}...")

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

    # Calculate starting index
    start_idx = (START_BATCH - 1) * BATCH_SIZE
    remaining_documents = documents[start_idx:]

    if not remaining_documents:
        logger.info("No remaining documents to process")
        return True

    # Process in batches
    total_batches = (len(remaining_documents) + BATCH_SIZE - 1) // BATCH_SIZE
    logger.info(
        f"Processing {len(remaining_documents)} remaining documents in {total_batches} batches (starting from batch {START_BATCH})"
    )

    async with httpx.AsyncClient(timeout=120.0) as client:
        for batch_idx in range(total_batches):
            current_batch = START_BATCH + batch_idx
            start_idx = batch_idx * BATCH_SIZE
            end_idx = min(start_idx + BATCH_SIZE, len(remaining_documents))
            batch_documents = remaining_documents[start_idx:end_idx]

            logger.info(
                f"Processing batch {current_batch} ({len(batch_documents)} documents)"
            )

            try:
                response = await client.post(
                    f"{VECTOR_SERVER_URL}/api/vector/add",
                    json={"documents": batch_documents},
                )

                if response.status_code == 200:
                    result = response.json()
                    logger.info(f"Successfully added batch {current_batch}: {result}")
                else:
                    logger.error(
                        f"Failed to add batch {current_batch}: {response.status_code} - {response.text}"
                    )
                    return False

            except Exception as e:
                logger.error(f"Error adding batch {current_batch}: {e}")
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
    asyncio.run(resume_populate_vector_database())
