"""
Frontend/API Server for MBS AI Assistant Production Deployment.

This server handles:
- Web UI serving
- MBS code lookup (SQLite)
- API orchestration (proxies to other servers)
- Health monitoring
"""

import logging
import os
import sys
from typing import Dict, Any
import httpx
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings
from templates.enhanced_chat_ui import ENHANCED_CHAT_UI
from src.mbs_clarity.db import fetch_item_aggregate

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Server configuration
AI_SERVER_URL = os.getenv("AI_SERVER_URL", "http://localhost:8001")
VECTOR_SERVER_URL = os.getenv("VECTOR_SERVER_URL", "http://localhost:8002")

# Create FastAPI app
app = FastAPI(
    title="MBS AI Assistant - Frontend Server",
    description="Frontend and API orchestration server",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all requests."""
    import time

    start = time.time()
    response = await call_next(request)
    duration = (time.time() - start) * 1000
    logger.info(
        f"{request.method} {request.url.path} - {response.status_code} - {duration:.1f}ms"
    )
    return response


@app.get("/")
async def index():
    """Serve the MBS AI Assistant UI."""
    return HTMLResponse(ENHANCED_CHAT_UI)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "message": "Frontend server is running",
        "server": "frontend",
        "ai_server_url": AI_SERVER_URL,
        "vector_server_url": VECTOR_SERVER_URL,
    }


@app.get("/api/ai/status")
async def get_ai_status():
    """Get AI service status by checking all servers."""
    try:
        # Check AI server
        ai_status = {"available": False, "error": None}
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{AI_SERVER_URL}/health", timeout=5.0)
                if response.status_code == 200:
                    ai_status = {"available": True, "data": response.json()}
        except Exception as e:
            ai_status["error"] = str(e)

        # Check Vector server
        vector_status = {"available": False, "error": None}
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{VECTOR_SERVER_URL}/health", timeout=5.0)
                if response.status_code == 200:
                    vector_status = {"available": True, "data": response.json()}
        except Exception as e:
            vector_status["error"] = str(e)

        return {
            "ai_enabled": ai_status["available"] and vector_status["available"],
            "gemini_available": ai_status["available"],
            "vector_db_initialized": vector_status["available"],
            "nlp_service_initialized": ai_status["available"],
            "model_name": "gemini-2.5-flash",
            "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
            "vector_db_stats": vector_status.get("data", {}).get("stats"),
            "servers": {"ai_server": ai_status, "vector_server": vector_status},
        }

    except Exception as e:
        logger.error(f"Error getting AI status: {e}")
        return {
            "ai_enabled": False,
            "gemini_available": False,
            "vector_db_initialized": False,
            "nlp_service_initialized": False,
            "model_name": "unknown",
            "embedding_model": "unknown",
            "vector_db_stats": None,
            "error": str(e),
        }


@app.post("/api/ai/natural-language")
async def natural_language_query(request: Dict[str, Any]):
    """Proxy natural language queries to AI server."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{AI_SERVER_URL}/api/ai/natural-language", json=request, timeout=30.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        logger.error(f"Error proxying to AI server: {e}")
        raise HTTPException(status_code=503, detail=f"AI server unavailable: {e}")
    except Exception as e:
        logger.error(f"Error processing natural language query: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/ai/conversation")
async def conversational_query(request: Dict[str, Any]):
    """Proxy conversational queries to AI server."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{AI_SERVER_URL}/api/ai/conversation", json=request, timeout=30.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        logger.error(f"Error proxying to AI server: {e}")
        raise HTTPException(status_code=503, detail=f"AI server unavailable: {e}")
    except Exception as e:
        logger.error(f"Error processing conversational query: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/items")
async def get_items(codes: str):
    """Get MBS item information for specific codes (local SQLite lookup)."""
    try:
        if not codes:
            raise HTTPException(status_code=400, detail="No codes provided")

        # Parse comma-separated codes
        code_list = [code.strip() for code in codes.split(",") if code.strip()]

        if not code_list:
            raise HTTPException(status_code=400, detail="No valid codes provided")

        items = []

        for code in code_list:
            try:
                # Fetch item data using the existing function
                item_data = fetch_item_aggregate(code)

                if item_data and item_data[0]:  # item_row exists
                    item_row, rel_rows, con_rows = item_data

                    # Convert to structured format
                    item = {
                        "item": {
                            "item_num": item_row[0],
                            "category": item_row[1],
                            "group_code": item_row[2],
                            "schedule_fee": item_row[3],
                            "description": item_row[4],
                            "derived_fee": item_row[5],
                            "start_date": item_row[6],
                            "end_date": item_row[7],
                            "provider_type": item_row[8],
                            "emsn_description": item_row[9],
                        },
                        "relations": [
                            {
                                "relation_type": rel[0],
                                "target_item_num": rel[1],
                                "detail": rel[2],
                            }
                            for rel in rel_rows
                        ],
                        "constraints": [
                            {
                                "constraint_type": con[0],
                                "value": con[1],
                            }
                            for con in con_rows
                        ],
                    }

                    items.append(item)

            except Exception as e:
                logger.warning(f"Failed to fetch item {code}: {e}")
                continue

        if not items:
            raise HTTPException(status_code=404, detail="No items found")

        return {"items": items}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching items: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    # Use PORT environment variable for Render compatibility
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"  # Required for Render

    logger.info(f"Starting Frontend server on {host}:{port}")
    logger.info(f"AI Server URL: {AI_SERVER_URL}")
    logger.info(f"Vector Server URL: {VECTOR_SERVER_URL}")

    uvicorn.run(app, host=host, port=port, log_level="info")
