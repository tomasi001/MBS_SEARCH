"""
AI Processing Server for MBS AI Assistant Production Deployment.

This server handles:
- Gemini API integration
- Natural language processing
- Medical query analysis
- Conversational AI responses
"""

import logging
import os
import sys
from typing import Dict, Any, List, Optional
import httpx
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings
from services.gemini_service import GeminiService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Server configuration
VECTOR_SERVER_URL = os.getenv("VECTOR_SERVER_URL", "http://localhost:8002")
FRONTEND_SERVER_URL = os.getenv("FRONTEND_SERVER_URL", "http://localhost:8000")

# Global service instance
gemini_service: GeminiService = None

# Create FastAPI app
app = FastAPI(
    title="MBS AI Assistant - AI Server",
    description="AI processing and natural language understanding server",
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


@app.on_event("startup")
async def startup_event():
    """Initialize services on startup."""
    global gemini_service

    logger.info("Initializing AI services...")
    try:
        gemini_service = GeminiService()
        logger.info("AI services initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize AI services: {e}")
        # Continue without AI services


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


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "message": "AI server is running",
        "server": "ai",
        "gemini_available": gemini_service is not None,
        "vector_server_url": VECTOR_SERVER_URL,
    }


def _validate_mbs_query(self, query: str) -> Dict[str, Any]:
    """Validate that the query is related to MBS codes and medical procedures."""
    query_lower = query.lower()

    # Medical/MBS related keywords
    medical_keywords = [
        "consultation",
        "examination",
        "assessment",
        "treatment",
        "procedure",
        "general practitioner",
        "gp",
        "specialist",
        "surgeon",
        "physician",
        "chest",
        "heart",
        "lung",
        "abdomen",
        "head",
        "neck",
        "back",
        "leg",
        "arm",
        "pain",
        "injury",
        "condition",
        "disease",
        "disorder",
        "syndrome",
        "diagnosis",
        "therapy",
        "surgery",
        "operation",
        "intervention",
        "chronic",
        "acute",
        "emergency",
        "urgent",
        "routine",
        "follow-up",
        "mental health",
        "psychiatric",
        "psychological",
        "counseling",
        "imaging",
        "scan",
        "x-ray",
        "ultrasound",
        "mri",
        "ct",
        "pet",
        "blood test",
        "laboratory",
        "pathology",
        "biopsy",
        "culture",
        "vaccination",
        "immunization",
        "injection",
        "medication",
        "prescription",
        "patient",
        "medical",
        "health",
        "clinical",
        "hospital",
        "clinic",
        "mbs",
        "item",
        "code",
        "billing",
        "medicare",
        "fee",
        "schedule",
    ]

    # Check if query contains medical keywords
    has_medical_content = any(keyword in query_lower for keyword in medical_keywords)

    # Non-medical topics to reject
    non_medical_topics = [
        "weather",
        "sports",
        "cooking",
        "travel",
        "shopping",
        "entertainment",
        "politics",
        "finance",
        "technology",
        "programming",
        "coding",
        "education",
        "school",
        "university",
        "job",
        "career",
        "business",
        "relationship",
        "dating",
        "family",
        "personal",
        "hobby",
        "game",
    ]

    has_non_medical_content = any(topic in query_lower for topic in non_medical_topics)

    if not has_medical_content and len(query.split()) > 3:
        return {
            "valid": False,
            "reason": "This query doesn't appear to be related to medical procedures or MBS codes. Please ask about medical consultations, examinations, treatments, or procedures.",
        }

    if has_non_medical_content and not has_medical_content:
        return {
            "valid": False,
            "reason": "I can only help with medical procedures and MBS codes. Please ask about consultations, examinations, treatments, or other medical services.",
        }

    return {"valid": True, "reason": None}


@app.post("/api/ai/natural-language")
async def natural_language_query(request: Dict[str, Any]):
    """Process natural language queries from doctors."""
    try:
        if not gemini_service:
            raise HTTPException(status_code=503, detail="AI service not available")

        query = request.get("query", "")
        context = request.get("context", {})

        if not query:
            raise HTTPException(status_code=400, detail="Query is required")

        logger.info(f"Processing natural language query: '{query}'")

        # Step 0: Validate query is MBS-related
        validation = _validate_mbs_query(query)
        if not validation["valid"]:
            return {
                "query": query,
                "suggested_codes": [],
                "detailed_suggestions": [],
                "follow_up_questions": [],
                "context": context,
                "processing_time_ms": 0,
                "error": validation["reason"],
            }

        # Step 1: Analyze the query using Gemini
        analysis = gemini_service.analyze_medical_query(query)

        # Step 2: Perform vector search via vector server
        search_results = []
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{VECTOR_SERVER_URL}/api/vector/search",
                    json={"query": query, "n_results": 20},
                    timeout=10.0,
                )
                if response.status_code == 200:
                    search_results = response.json().get("results", [])
        except Exception as e:
            logger.warning(f"Vector search failed: {e}")

        # Step 3: Generate code suggestions
        suggested_codes = []
        if search_results:
            for result in search_results[:10]:
                item_num = result.get("metadata", {}).get("item_num")
                if item_num:
                    suggested_codes.append(item_num)

        # Step 4: Generate follow-up questions
        follow_up_questions = gemini_service.generate_follow_up_questions(
            query=query, suggested_codes=suggested_codes, context=analysis
        )

        return {
            "query": query,
            "suggested_codes": list(set(suggested_codes))[:15],
            "detailed_suggestions": [],  # Would need MBS lookup
            "follow_up_questions": follow_up_questions,
            "context": context,
            "processing_time_ms": 0,  # Would calculate actual time
            "analysis": analysis,
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing natural language query: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/ai/conversation")
async def conversational_query(request: Dict[str, Any]):
    """Process conversational queries with context awareness."""
    try:
        if not gemini_service:
            raise HTTPException(status_code=503, detail="AI service not available")

        query = request.get("query", "")
        conversation_history = request.get("conversation_history", [])
        context = request.get("context", {})

        if not query:
            raise HTTPException(status_code=400, detail="Query is required")

        logger.info(
            f"Processing conversational query: '{query}' with {len(conversation_history)} previous messages"
        )

        # For now, treat as regular natural language query
        # In full implementation, would build conversation context
        return await natural_language_query({"query": query, "context": context})

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing conversational query: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    # Use PORT environment variable for Render compatibility
    port = int(os.environ.get("PORT", 8001))
    host = "0.0.0.0"  # Required for Render

    logger.info(f"Starting AI server on {host}:{port}")
    logger.info(f"Vector Server URL: {VECTOR_SERVER_URL}")

    uvicorn.run(app, host=host, port=port, log_level="info")
