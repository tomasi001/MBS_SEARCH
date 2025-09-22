"""
Main FastAPI application for MBS AI Assistant MVP.

This module provides the main API endpoints for the MBS AI Assistant.
"""

import logging
import time
from contextlib import asynccontextmanager
from typing import Dict, Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings
from services.gemini_service import GeminiService
from services.vector_service import VectorService
from services.nlp_service import NLPService
from models import (
    NaturalLanguageQuery,
    NaturalLanguageResponse,
    ChatRequest,
    ChatResponse,
    AIStatusResponse,
)
from templates.enhanced_chat_ui import ENHANCED_CHAT_UI
from src.mbs_clarity.db import fetch_item_aggregate

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global service instances
gemini_service: GeminiService = None
vector_service: VectorService = None
nlp_service: NLPService = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    global gemini_service, vector_service, nlp_service

    logger.info("App startup: initializing services")

    try:
        # Initialize Gemini service
        logger.info("Initializing Gemini service...")
        gemini_service = GeminiService()
        logger.info("Gemini service initialized successfully")

        # Initialize Vector service
        logger.info("Initializing Vector service...")
        vector_service = VectorService()
        logger.info("Vector service initialized successfully")

        # Skip vector DB population during startup for faster deployment
        # Vector DB will be populated on first use if needed
        logger.info(
            "Skipping vector DB population during startup for faster deployment"
        )

        # Initialize NLP service
        logger.info("Initializing NLP service...")
        nlp_service = NLPService()
        logger.info("NLP service initialized successfully")

        logger.info("App startup: all services initialized successfully")

    except Exception as e:
        logger.error(f"App startup: failed to initialize services: {e}")
        logger.error(
            f"Service status - Gemini: {gemini_service is not None}, Vector: {vector_service is not None}, NLP: {nlp_service is not None}"
        )
        # Continue startup even if services fail

    yield

    logger.info("App shutdown")


# Create FastAPI app
app = FastAPI(
    title="MBS AI Assistant MVP",
    description="AI-powered MBS code lookup assistant using Gemini",
    version="1.0.0",
    lifespan=lifespan,
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
    start = time.time()
    response = await call_next(request)
    duration = (time.time() - start) * 1000

    logger.info(
        f"{request.method} {request.url.path} - {response.status_code} - {duration:.1f}ms"
    )
    return response


@app.get("/", response_class=HTMLResponse)
async def index():
    """Serve the dual-panel MBS AI Assistant UI."""
    return HTMLResponse(ENHANCED_CHAT_UI)


@app.get("/api/ai/status", response_model=AIStatusResponse)
async def get_ai_status():
    """Get AI service status and capabilities."""
    try:
        global gemini_service, vector_service, nlp_service

        # Try to initialize services if they failed during startup
        if not gemini_service:
            try:
                logger.info("Attempting to initialize Gemini service on-demand...")
                gemini_service = GeminiService()
                logger.info("Gemini service initialized successfully on-demand")
            except Exception as e:
                logger.error(f"Failed to initialize Gemini service on-demand: {e}")

        if not vector_service:
            try:
                logger.info("Attempting to initialize Vector service on-demand...")
                vector_service = VectorService()
                logger.info("Vector service initialized successfully on-demand")
            except Exception as e:
                logger.error(f"Failed to initialize Vector service on-demand: {e}")

        if not nlp_service and gemini_service and vector_service:
            try:
                logger.info("Attempting to initialize NLP service on-demand...")
                nlp_service = NLPService()
                logger.info("NLP service initialized successfully on-demand")
            except Exception as e:
                logger.error(f"Failed to initialize NLP service on-demand: {e}")

        # Check service availability
        ai_enabled = all([gemini_service, vector_service, nlp_service])
        gemini_available = gemini_service is not None
        vector_db_initialized = vector_service is not None
        nlp_service_initialized = nlp_service is not None

        # Get vector DB stats if available
        vector_db_stats = None
        if vector_service:
            try:
                vector_db_stats = vector_service.get_collection_stats()
            except Exception as e:
                logger.warning(f"Could not get vector DB stats: {e}")

        return AIStatusResponse(
            ai_enabled=ai_enabled,
            gemini_available=gemini_available,
            vector_db_initialized=vector_db_initialized,
            nlp_service_initialized=nlp_service_initialized,
            model_name=settings.GEMINI_MODEL_NAME,
            embedding_model=settings.GEMINI_EMBEDDING_MODEL,
            vector_db_stats=vector_db_stats,
        )

    except Exception as e:
        logger.error(f"Error getting AI status: {e}")
        return AIStatusResponse(
            ai_enabled=False,
            gemini_available=False,
            vector_db_initialized=False,
            nlp_service_initialized=False,
            model_name="",
            embedding_model="",
            error=str(e),
        )


@app.post("/api/ai/natural-language", response_model=NaturalLanguageResponse)
async def natural_language_query(request: NaturalLanguageQuery):
    """Process natural language queries from doctors."""
    try:
        global nlp_service

        if not nlp_service:
            raise HTTPException(status_code=503, detail="NLP service not available")

        logger.info(f"Natural language query: '{request.query}'")

        # Process the query
        result = nlp_service.process_natural_language_query(
            query=request.query, context=request.context
        )

        logger.info(
            f"Query processed, found {len(result.get('suggested_codes', []))} suggestions"
        )

        return NaturalLanguageResponse(**result)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing natural language query: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/ai/conversation", response_model=NaturalLanguageResponse)
async def conversational_query(request: Dict[str, Any]):
    """Process conversational queries with context awareness."""
    try:
        global nlp_service
        if not nlp_service:
            raise HTTPException(status_code=503, detail="NLP service not available")

        query = request.get("query", "")
        conversation_history = request.get("conversation_history", [])
        context = request.get("context", {})

        if not query:
            raise HTTPException(status_code=400, detail="Query is required")

        logger.info(
            f"Conversational query: '{query}' with {len(conversation_history)} previous messages"
        )

        result = nlp_service.process_conversational_query(
            query=query, conversation_history=conversation_history, context=context
        )

        logger.info(
            f"Conversational query processed, found {len(result.get('suggested_codes', []))} suggestions"
        )

        return NaturalLanguageResponse(**result)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing conversational query: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/items")
async def get_items(codes: str):
    """Get MBS item information for specific codes."""
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
    # Use PORT environment variable for Render compatibility - EXACTLY as per Render docs
    port = int(
        os.environ.get("PORT", 8000)
    )  # Use Render's PORT or default to 8000 locally
    host = "0.0.0.0"  # Required for Render

    logger.info(f"Starting server on {host}:{port}")
    logger.info(f"PORT environment variable: {os.environ.get('PORT')}")
    logger.info(f"DEBUG mode: {settings.DEBUG}")

    uvicorn.run(app, host=host, port=port, log_level="info")
