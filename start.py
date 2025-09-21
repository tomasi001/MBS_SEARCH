#!/usr/bin/env python3
"""
Production startup script for MBS AI Assistant.
This script ensures the vector database is populated before starting the server.
"""

import os
import sys
import logging
import subprocess
from pathlib import Path

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.vector_service import VectorService
from config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def check_and_populate_vector_db():
    """Check if vector database exists and populate if needed."""
    try:
        vector_service = VectorService()
        stats = vector_service.get_db_stats()

        if stats.get("total_documents", 0) == 0:
            logger.info("Vector database is empty. Populating...")

            # Run the population script
            result = subprocess.run(
                [sys.executable, "scripts/populate_mbs_data.py"],
                capture_output=True,
                text=True,
            )

            if result.returncode == 0:
                logger.info("Vector database populated successfully")
            else:
                logger.error(f"Failed to populate vector database: {result.stderr}")
                return False
        else:
            logger.info(
                f"Vector database already has {stats['total_documents']} documents"
            )

        return True

    except Exception as e:
        logger.error(f"Error checking vector database: {e}")
        return False


def main():
    """Main startup function."""
    logger.info("Starting MBS AI Assistant...")

    # Check if we're in production mode
    if os.getenv("RENDER"):
        logger.info("Running in Render production environment")

        # Ensure vector database is populated
        if not check_and_populate_vector_db():
            logger.error("Failed to initialize vector database. Exiting.")
            sys.exit(1)

    # Start the FastAPI server
    logger.info("Starting FastAPI server...")

    # Import and run the app
    from api.main import app
    import uvicorn

    port = int(os.getenv("PORT", 8000))
    host = os.getenv("API_HOST", "0.0.0.0")

    uvicorn.run(app, host=host, port=port, log_level="info")


if __name__ == "__main__":
    main()
