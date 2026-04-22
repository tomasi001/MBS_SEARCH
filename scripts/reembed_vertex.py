#!/usr/bin/env python3
"""
Re-embed all MBS documents using Vertex AI embedding API.
RESUMABLE - saves progress after each batch so we never redo work.

Usage:
    poetry run python scripts/reembed_vertex.py
"""

import json
import logging
import os
import shutil
import sqlite3
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import requests
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Config
MBS_DB_PATH = os.getenv("MBS_DB_PATH", "mbs.db")
CHROMA_OUTPUT_DIR = "./chroma_db_gemini"
PROGRESS_FILE = "./scripts/.embed_progress.json"
VERTEX_API_KEY = os.getenv("VERTEX_API_KEY", "")
PROJECT_ID = os.getenv("VERTEX_PROJECT_ID", "741680163127")
LOCATION = "us-central1"
MODEL = "gemini-embedding-001"
EMBEDDING_DIM = 768
BATCH_SIZE = 50  # texts per API call (Vertex AI supports up to 250)
RATE_LIMIT_PAUSE = 1  # seconds between API calls


def load_documents() -> List[Dict[str, Any]]:
    """Load all MBS documents from SQLite."""
    logger.info(f"Loading MBS data from {MBS_DB_PATH}")
    documents = []

    with sqlite3.connect(MBS_DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            """SELECT item_num, category, group_code, schedule_fee, description,
                      start_date, end_date, provider_type
               FROM items WHERE description IS NOT NULL AND description != ''
               ORDER BY item_num"""
        )
        items = cur.fetchall()
        logger.info(f"Found {len(items)} items with descriptions")

        for item in items:
            item_num = item[0]
            metadata = {"item_num": item_num, "chunk_type": "description"}
            for i, key in [(1, "category"), (2, "group_code"), (3, "schedule_fee"),
                           (5, "start_date"), (6, "end_date"), (7, "provider_type")]:
                if item[i] is not None:
                    metadata[key] = item[i]

            documents.append({"id": f"{item_num}_description", "text": item[4], "metadata": metadata})

            cur.execute("SELECT relation_type, target_item_num, detail FROM relations WHERE item_num = ?", (item_num,))
            relations = cur.fetchall()
            if relations:
                text = f"Item {item_num} is related to: " + "; ".join(f"{r[0]} {r[1]} ({r[2]})" for r in relations)
                meta = {"item_num": item_num, "chunk_type": "relations"}
                if item[1] is not None: meta["category"] = item[1]
                if item[2] is not None: meta["group_code"] = item[2]
                documents.append({"id": f"{item_num}_relations", "text": text, "metadata": meta})

            cur.execute("SELECT constraint_type, value FROM constraints WHERE item_num = ?", (item_num,))
            constraints = cur.fetchall()
            if constraints:
                text = f"Item {item_num} constraints: " + "; ".join(f"{c[0]}: {c[1]}" for c in constraints)
                meta = {"item_num": item_num, "chunk_type": "constraints"}
                if item[1] is not None: meta["category"] = item[1]
                if item[2] is not None: meta["group_code"] = item[2]
                documents.append({"id": f"{item_num}_constraints", "text": text, "metadata": meta})

    logger.info(f"Total documents: {len(documents)}")
    return documents


def load_progress() -> Dict[str, List[float]]:
    """Load cached embeddings from previous runs."""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            data = json.load(f)
        logger.info(f"Resuming: {len(data)} embeddings already cached")
        return data
    return {}


def save_progress(progress: Dict[str, List[float]]):
    """Save embeddings cache to disk."""
    Path(PROGRESS_FILE).parent.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f)


def embed_batch_vertex(texts: List[str], max_retries: int = 5) -> List[List[float]]:
    """Embed texts via Vertex AI REST API."""
    url = (
        f"https://{LOCATION}-aiplatform.googleapis.com/v1/"
        f"projects/{PROJECT_ID}/locations/{LOCATION}/"
        f"publishers/google/models/{MODEL}:predict"
        f"?key={VERTEX_API_KEY}"
    )

    instances = [{"content": t, "task_type": "RETRIEVAL_DOCUMENT"} for t in texts]
    payload = {"instances": instances, "parameters": {"outputDimensionality": EMBEDDING_DIM}}

    for attempt in range(max_retries):
        try:
            resp = requests.post(url, json=payload, timeout=60)
            if resp.status_code == 200:
                predictions = resp.json()["predictions"]
                embeddings = []
                for pred in predictions:
                    vec = np.array(pred["embeddings"]["values"], dtype=np.float32)
                    vec = vec / np.linalg.norm(vec)
                    embeddings.append(vec.tolist())
                return embeddings
            elif resp.status_code == 429:
                wait = min(30 * (attempt + 1), 120)
                logger.warning(f"Rate limited (attempt {attempt+1}), waiting {wait}s...")
                time.sleep(wait)
            else:
                logger.error(f"API error {resp.status_code}: {resp.text[:300]}")
                time.sleep(5)
        except Exception as e:
            logger.error(f"Request failed (attempt {attempt+1}): {e}")
            time.sleep(10)

    raise RuntimeError(f"Failed after {max_retries} retries")


def main():
    documents = load_documents()
    if not documents:
        sys.exit(1)

    # Load cached progress
    progress = load_progress()
    total = len(documents)
    already_done = sum(1 for d in documents if d["id"] in progress)
    logger.info(f"{already_done}/{total} already embedded, {total - already_done} remaining")

    # Embed missing documents in batches
    to_embed = [(i, d) for i, d in enumerate(documents) if d["id"] not in progress]
    num_batches = (len(to_embed) + BATCH_SIZE - 1) // BATCH_SIZE
    start_time = time.time()

    for batch_idx in range(num_batches):
        s = batch_idx * BATCH_SIZE
        e = min(s + BATCH_SIZE, len(to_embed))
        batch = to_embed[s:e]

        texts = [d["text"] for _, d in batch]
        embeddings = embed_batch_vertex(texts)

        # Cache results immediately
        for (_, doc), emb in zip(batch, embeddings):
            progress[doc["id"]] = emb

        # Save to disk after every batch
        save_progress(progress)

        done_now = already_done + e
        elapsed = time.time() - start_time
        rate = (e) / elapsed if elapsed > 0 else 0
        remaining = len(to_embed) - e
        eta = remaining / rate if rate > 0 else 0

        logger.info(
            f"Batch {batch_idx+1}/{num_batches} | "
            f"{done_now}/{total} total | "
            f"{rate:.0f} docs/s | ETA {eta:.0f}s"
        )
        time.sleep(RATE_LIMIT_PAUSE)

    logger.info(f"All {total} embeddings complete. Building ChromaDB...")

    # Build ChromaDB from cached embeddings
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

    # Insert in batches of 500
    CHROMA_BATCH = 500
    for i in range(0, total, CHROMA_BATCH):
        batch = documents[i:i + CHROMA_BATCH]
        collection.add(
            ids=[d["id"] for d in batch],
            embeddings=[progress[d["id"]] for d in batch],
            documents=[d["text"] for d in batch],
            metadatas=[d["metadata"] for d in batch],
        )

    elapsed_total = time.time() - start_time
    logger.info(f"Done! {collection.count()} docs in ChromaDB. Took {elapsed_total:.1f}s")
    logger.info(f"Output: {CHROMA_OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
