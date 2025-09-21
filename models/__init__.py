"""
Pydantic models for MBS AI Assistant MVP.

This module defines the data structures for API requests and responses.
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class NaturalLanguageQuery(BaseModel):
    """Request model for natural language queries."""

    query: str = Field(..., description="Natural language query from doctor")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context")


class Suggestion(BaseModel):
    """Model for MBS code suggestions."""

    code: str = Field(..., description="MBS code number")
    description: str = Field(..., description="Code description")
    confidence: float = Field(..., description="Confidence score (0.0-1.0)")
    reasoning: str = Field(..., description="Reasoning for suggestion")
    requirements: List[str] = Field(
        default_factory=list, description="Code requirements"
    )
    exclusions: List[str] = Field(default_factory=list, description="Code exclusions")


class FollowUpQuestion(BaseModel):
    """Model for follow-up questions."""

    question: str = Field(..., description="Follow-up question text")
    category: Optional[str] = Field(None, description="Question category")


class NaturalLanguageResponse(BaseModel):
    """Response model for natural language queries."""

    query: str = Field(..., description="Original query")
    suggested_codes: List[str] = Field(
        default_factory=list, description="Suggested MBS codes"
    )
    detailed_suggestions: List[Suggestion] = Field(
        default_factory=list, description="Detailed suggestions"
    )
    follow_up_questions: List[str] = Field(
        default_factory=list, description="Follow-up questions"
    )
    context: Dict[str, Any] = Field(
        default_factory=dict, description="Response context"
    )
    processing_time_ms: float = Field(
        0.0, description="Processing time in milliseconds"
    )
    error: Optional[str] = Field(None, description="Error message if any")


class ChatMessage(BaseModel):
    """Model for chat messages."""

    role: str = Field(..., description="Message role (user/assistant)")
    content: str = Field(..., description="Message content")
    timestamp: Optional[str] = Field(None, description="Message timestamp")


class ChatRequest(BaseModel):
    """Request model for chat messages."""

    message: str = Field(..., description="User message")
    session_id: Optional[str] = Field(None, description="Chat session ID")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context")


class ChatResponse(BaseModel):
    """Response model for chat messages."""

    message: str = Field(..., description="Assistant response")
    session_id: str = Field(..., description="Chat session ID")
    suggestions: List[Suggestion] = Field(
        default_factory=list, description="Code suggestions"
    )
    follow_up_questions: List[str] = Field(
        default_factory=list, description="Follow-up questions"
    )
    context_updated: bool = Field(False, description="Whether context was updated")


class AIStatusResponse(BaseModel):
    """Response model for AI service status."""

    ai_enabled: bool = Field(..., description="Whether AI services are enabled")
    gemini_available: bool = Field(..., description="Whether Gemini is available")
    vector_db_initialized: bool = Field(
        ..., description="Whether vector DB is initialized"
    )
    nlp_service_initialized: bool = Field(
        ..., description="Whether NLP service is initialized"
    )
    model_name: str = Field(..., description="Gemini model name")
    embedding_model: str = Field(..., description="Embedding model name")
    vector_db_stats: Optional[Dict[str, Any]] = Field(
        None, description="Vector DB statistics"
    )
    error: Optional[str] = Field(None, description="Error message if any")
