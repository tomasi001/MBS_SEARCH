#!/usr/bin/env python3
"""
Re-embed all MBS documents using Gemini embedding API (gemini-embedding-001).

Uses TRUE batch embedding - sends multiple texts per API call, so 10K docs
only needs ~104 API calls (not 10K).

Generates a fresh chroma_db that can be deployed to Render's vector server.

Usage:
    poetry run python scripts/reembed_gemini.py
"""

import logging
import os
import shutil
import sqlite3
import sys
import time
from typing import Any, Dict, List

import google.generativeai as genai
import numpy as np
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Config
MBS_DB_PATH = os.getenv("MBS_DB_PATH", "mbs.db")
CHROMA_OUTPUT_DIR = "./chroma_db_gemini"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMBEDDING_MODEL = "models/gemini-embedding-001"
EMBEDDING_DIM = 768
TEXTS_PER_API_CALL = 100  # texts sent in ONE embed_content call
CHROMA_BATCH_SIZE = 500   # docs added to ChromaDB per insert
RATE_LIMIT_PAUSE = 2      # seconds between API calls to stay under 100 RPM


def load_documents() -> List[Dict[str, Any]]:
    """Load all MBS documents from SQLite (descriptions, relations, constraints)."""
    logger.info(f"Loading MBS data from {MBS_DB_PATH}")
    documents = []

    with sqlite3.connect(MBS_DB_PATH) as conn:
        cur = conn.cursor()

        cur.execute(
            """SELECT item_num, category, group_code, schedule_fee, description,
                      start_date, end_date, provider_type
               FROM items
               WHERE description IS NOT NULL AND description != ''
               ORDER BY item_num"""
        )
        items = cur.fetchall()
        logger.info(f"Found {len(items)} items with descriptions")

        for item in items:
            item_num = item[0]
            metadata = {"item_num": item_num, "chunk_type": "description"}
            if item[1] is not None:
                metadata["category"] = item[1]
            if item[2] is not None:
                metadata["group_code"] = item[2]
            if item[3] is not None:
                metadata["schedule_fee"] = item[3]
            if item[5] is not None:
                metadata["start_date"] = item[5]
            if item[6] is not None:
                metadata["end_date"] = item[6]
            if item[7] is not None:
                metadata["provider_type"] = item[7]

            documents.append(
                {"id": f"{item_num}_description", "text": item[4], "metadata": metadata}
            )

            # Relations
            cur.execute(
                "SELECT relation_type, target_item_num, detail FROM relations WHERE item_num = ?",
                (item_num,),
            )
            relations = cur.fetchall()
            if relations:
                relation_text = f"Item {item_num} is related to: " + "; ".join(
                    f"{r[0]} {r[1]} ({r[2]})" for r in relations
                )
                rel_meta = {"item_num": item_num, "chunk_type": "relations"}
                if item[1] is not None:
                    rel_meta["category"] = item[1]
                if item[2] is not None:
                    rel_meta["group_code"] = item[2]
                documents.append(
                    {"id": f"{item_num}_relations", "text": relation_text, "metadata": rel_meta}
                )

            # Constraints
            cur.execute(
                "SELECT constraint_type, value FROM constraints WHERE item_num = ?",
                (item_num,),
            )
            constraints = cur.fetchall()
            if constraints:
                constraint_text = f"Item {item_num} constraints: " + "; ".join(
                    f"{c[0]}: {c[1]}" for c in constraints
                )
                con_meta = {"item_num": item_num, "chunk_type": "constraints"}
                if item[1] is not None:
                    con_meta["category"] = item[1]
                if item[2] is not None:
                    con_meta["group_code"] = item[2]
                documents.append(
                    {"id": f"{item_num}_constraints", "text": constraint_text, "metadata": con_meta}
                )

    logger.info(f"Total documents to embed: {len(documents)}")
    return documents


def embed_batch(texts: List[str], max_retries: int = 5) -> List[List[float]]:
    """Embed a list of texts in a SINGLE Gemini API call (true batching)."""
    for attempt in range(max_retries):
        try:
            result = genai.embed_content(
                model=EMBEDDING_MODEL,
                content=texts,
                task_type="RETRIEVAL_DOCUMENT",
                output_dimensionality=EMBEDDING_DIM,
            )

            raw_embeddings = result["embedding"]  # list of lists when batched
            embeddings = []
            for raw in raw_embeddings:
                vec = np.array(raw, dtype=np.float32)
                vec = vec / np.linalg.norm(vec)
                embeddings.append(vec.tolist())
            return embeddings

        except Exception as exc:
            error_str = str(exc)
            if "429" in error_str:
                # Extract retry delay from error if available
                wait = min(30 * (attempt + 1), 120)
                logger.warning(f"Rate limited (attempt {attempt+1}), waiting {wait}s...")
                time.sleep(wait)
            else:
                raise

    raise RuntimeError(f"Failed after {max_retries} retries")


def main():
    if not GEMINI_API_KEY:
        logger.error("GEMINI_API_KEY not set")
        sys.exit(1)

    genai.configure(api_key=GEMINI_API_KEY)

    # Load documents
    documents = load_documents()
    if not documents:
        logger.error("No documents loaded")
        sys.exit(1)

    # Fresh chroma_db directory
    if os.path.exists(CHROMA_OUTPUT_DIR):
        shutil.rmtree(CHROMA_OUTPUT_DIR)
    os.makedirs(CHROMA_OUTPUT_DIR)

    import chromadb
    from chromadb.config import Settings

    client = chromadb.PersistentClient(
        path=CHROMA_OUTPUT_DIR,
        settings=Settings(anonymized_telemetry=False, allow_reset=True),
    )
    collection = client.create_collection(
        name="mbs_codes",
        metadata={"description": "MBS codes and descriptions"},
    )

    # Generate ALL embeddings first via batched API calls
    total = len(documents)
    all_embeddings = []
    api_calls = 0
    num_api_batches = (total + TEXTS_PER_API_CALL - 1) // TEXTS_PER_API_CALL
    start_time = time.time()

    logger.info(
        f"Embedding {total} documents in {num_api_batches} API calls "
        f"({TEXTS_PER_API_CALL} texts per call)"
    )

    for i in range(0, total, TEXTS_PER_API_CALL):
        batch_texts = [d["text"] for d in documents[i : i + TEXTS_PER_API_CALL]]
        batch_num = i // TEXTS_PER_API_CALL + 1

        embeddings = embed_batch(batch_texts)
        all_embeddings.extend(embeddings)
        api_calls += 1

        elapsed = time.time() - start_time
        docs_done = min(i + TEXTS_PER_API_CALL, total)
        rate = docs_done / elapsed if elapsed > 0 else 0
        eta = (total - docs_done) / rate if rate > 0 else 0

        logger.info(
            f"API call {batch_num}/{num_api_batches} done "
            f"({docs_done}/{total} docs, {rate:.0f} docs/s, ETA {eta:.0f}s)"
        )

        # Rate limit: stay under 100 RPM
        time.sleep(RATE_LIMIT_PAUSE)

    logger.info(f"All embeddings generated ({api_calls} API calls)")

    # Insert into ChromaDB in larger batches
    logger.info("Inserting into ChromaDB...")
    for i in range(0, total, CHROMA_BATCH_SIZE):
        batch = documents[i : i + CHROMA_BATCH_SIZE]
        batch_embeddings = all_embeddings[i : i + CHROMA_BATCH_SIZE]

        collection.add(
            ids=[d["id"] for d in batch],
            embeddings=batch_embeddings,
            documents=[d["text"] for d in batch],
            metadatas=[d["metadata"] for d in batch],
        )

    elapsed_total = time.time() - start_time
    final_count = collection.count()
    logger.info(f"Done! {final_count} documents embedded in {elapsed_total:.1f}s")
    logger.info(f"API calls used: {api_calls}")
    logger.info(f"Output: {CHROMA_OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
