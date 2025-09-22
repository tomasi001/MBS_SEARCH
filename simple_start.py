#!/usr/bin/env python3
"""
Simple startup script for Render deployment.
This avoids loading heavy models during startup to prevent timeouts.
"""

import os
import sys
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def main():
    """Start the FastAPI app with minimal initialization."""
    
    # Log environment info
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    
    logger.info(f"Starting MBS AI Assistant on {host}:{port}")
    logger.info(f"PORT environment variable: {os.environ.get('PORT')}")
    logger.info(f"RENDER environment variable: {os.environ.get('RENDER')}")
    
    try:
        # Import and start the app
        from api.main import app
        import uvicorn
        
        logger.info("FastAPI app imported successfully")
        logger.info("Starting uvicorn server...")
        
        # Start the server
        uvicorn.run(
            app, 
            host=host, 
            port=port, 
            log_level="info",
            access_log=True
        )
        
    except Exception as e:
        logger.error(f"Failed to start application: {e}")
        logger.error("Full traceback:", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
