#!/usr/bin/env python3
"""
Debug startup script to see exactly what's happening during Render deployment.
This will help us identify the exact issue with port binding.
"""

import os
import sys
import logging
import time
from pathlib import Path

# Set up comprehensive logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('startup_debug.log')
    ]
)

logger = logging.getLogger(__name__)

def log_environment():
    """Log all environment variables and system info."""
    logger.info("=" * 80)
    logger.info("STARTUP DEBUG - Environment Information")
    logger.info("=" * 80)
    
    logger.info(f"Python version: {sys.version}")
    logger.info(f"Python executable: {sys.executable}")
    logger.info(f"Current working directory: {os.getcwd()}")
    logger.info(f"Script location: {__file__}")
    
    # Log all environment variables
    logger.info("Environment variables:")
    for key, value in sorted(os.environ.items()):
        if 'PASSWORD' in key.upper() or 'SECRET' in key.upper() or 'KEY' in key.upper():
            logger.info(f"  {key}=***HIDDEN***")
        else:
            logger.info(f"  {key}={value}")
    
    logger.info("=" * 80)

def log_file_structure():
    """Log the file structure to see what's available."""
    logger.info("File structure:")
    for root, dirs, files in os.walk('.'):
        level = root.replace('.', '').count(os.sep)
        indent = ' ' * 2 * level
        logger.info(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            logger.info(f"{subindent}{file}")

def test_imports():
    """Test critical imports to see what's failing."""
    logger.info("Testing imports:")
    
    try:
        import fastapi
        logger.info(f"✓ FastAPI imported successfully: {fastapi.__version__}")
    except ImportError as e:
        logger.error(f"✗ FastAPI import failed: {e}")
    
    try:
        import uvicorn
        logger.info(f"✓ Uvicorn imported successfully: {uvicorn.__version__}")
    except ImportError as e:
        logger.error(f"✗ Uvicorn import failed: {e}")
    
    try:
        import chromadb
        logger.info(f"✓ ChromaDB imported successfully: {chromadb.__version__}")
    except ImportError as e:
        logger.error(f"✗ ChromaDB import failed: {e}")
    
    try:
        import sentence_transformers
        logger.info(f"✓ Sentence Transformers imported successfully")
    except ImportError as e:
        logger.error(f"✗ Sentence Transformers import failed: {e}")

def test_port_binding():
    """Test if we can bind to the port."""
    logger.info("Testing port binding:")
    
    port = int(os.environ.get("PORT", 8000))
    logger.info(f"Attempting to bind to port: {port}")
    
    try:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.close()
        logger.info(f"✓ Successfully bound to 0.0.0.0:{port}")
    except Exception as e:
        logger.error(f"✗ Failed to bind to 0.0.0.0:{port}: {e}")

def main():
    """Main debug function."""
    logger.info("Starting comprehensive startup debug...")
    
    log_environment()
    log_file_structure()
    test_imports()
    test_port_binding()
    
    logger.info("=" * 80)
    logger.info("DEBUG COMPLETE - Starting actual application...")
    logger.info("=" * 80)
    
    # Now start the actual app
    try:
        from api.main import app
        import uvicorn
        
        port = int(os.environ.get("PORT", 8000))
        host = "0.0.0.0"
        
        logger.info(f"Starting FastAPI app on {host}:{port}")
        logger.info("App object created successfully")
        
        uvicorn.run(app, host=host, port=port, log_level="debug")
        
    except Exception as e:
        logger.error(f"Failed to start application: {e}")
        logger.error("Full traceback:", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
