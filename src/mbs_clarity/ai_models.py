"""
AI models and configurations for MBS Clarity AI assistant.

This module defines the data structures and configurations for AI-powered
MBS code search, natural language processing, and chatbot functionality.
"""

from enum import Enum
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class EmbeddingModel(str, Enum):
    """Available embedding models for vector search."""

    OPENAI_ADA = "text-embedding-ada-002"
    OPENAI_3_SMALL = "text-embedding-3-small"
    OPENAI_3_LARGE = "text-embedding-3-large"
    SENTENCE_TRANSFORMERS = "sentence-transformers/all-MiniLM-L6-v2"


class LLMModel(str, Enum):
    """Available LLM models for natural language processing."""

    OPENAI_GPT4 = "gpt-4"
    OPENAI_GPT4_TURBO = "gpt-4-turbo-preview"
    OPENAI_GPT35_TURBO = "gpt-3.5-turbo"
    OPENAI_GPT4O = "gpt-4o"


class SearchType(str, Enum):
    """Types of search operations."""

    SEMANTIC = "semantic"  # Vector similarity search
    HYBRID = "hybrid"  # Combined semantic + keyword search
    KEYWORD = "keyword"  # Traditional keyword search
    NATURAL_LANGUAGE = "natural_language"  # LLM-powered search


class ChatMessage(BaseModel):
    """A single message in a chat conversation."""

    role: str = Field(..., description="Message role: 'user', 'assistant', or 'system'")
    content: str = Field(..., description="Message content")
    timestamp: Optional[str] = Field(None, description="Message timestamp")


class ChatContext(BaseModel):
    """Context information for chatbot conversations."""

    current_codes: List[str] = Field(
        default_factory=list, description="Currently displayed MBS codes"
    )
    search_history: List[str] = Field(
        default_factory=list, description="Previous search queries"
    )
    session_id: Optional[str] = Field(None, description="Session identifier")
    user_preferences: Dict[str, Any] = Field(
        default_factory=dict, description="User preferences"
    )


class MBSChunk(BaseModel):
    """A chunk of MBS data for vector storage."""

    item_num: str = Field(..., description="MBS item number")
    chunk_id: str = Field(..., description="Unique chunk identifier")
    content: str = Field(
        ..., description="Chunk content (description, constraints, etc.)"
    )
    chunk_type: str = Field(
        ..., description="Type of chunk: 'description', 'constraints', 'relations'"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )
    embedding: Optional[List[float]] = Field(None, description="Vector embedding")


class SearchResult(BaseModel):
    """Result from a semantic or hybrid search."""

    item_num: str = Field(..., description="MBS item number")
    score: float = Field(..., description="Relevance score")
    content: str = Field(..., description="Matching content")
    chunk_type: str = Field(..., description="Type of matching chunk")
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )


class NaturalLanguageQuery(BaseModel):
    """A natural language query from a doctor."""

    query: str = Field(..., description="Doctor's natural language description")
    context: Optional[ChatContext] = Field(None, description="Conversation context")
    follow_up_questions: List[str] = Field(
        default_factory=list, description="Suggested follow-up questions"
    )
    suggested_codes: List[str] = Field(
        default_factory=list, description="Suggested MBS codes"
    )


class CodeSuggestion(BaseModel):
    """A suggested MBS code with reasoning."""

    item_num: str = Field(..., description="Suggested MBS item number")
    confidence: float = Field(..., description="Confidence score (0-1)")
    reasoning: str = Field(..., description="Why this code was suggested")
    requirements: List[str] = Field(
        default_factory=list, description="Requirements for this code"
    )
    exclusions: List[str] = Field(
        default_factory=list, description="Items this excludes"
    )
    follow_up_questions: List[str] = Field(
        default_factory=list, description="Questions to narrow down"
    )


class ChatbotResponse(BaseModel):
    """Response from the contextual chatbot."""

    message: str = Field(..., description="Chatbot's response message")
    suggested_actions: List[str] = Field(
        default_factory=list, description="Suggested actions"
    )
    code_suggestions: List[CodeSuggestion] = Field(
        default_factory=list, description="Code suggestions"
    )
    follow_up_questions: List[str] = Field(
        default_factory=list, description="Follow-up questions"
    )
    context_updated: bool = Field(False, description="Whether context was updated")


class AIConfig(BaseModel):
    """Configuration for AI services."""

    # OpenAI Configuration
    openai_api_key: Optional[str] = Field(None, description="OpenAI API key")
    openai_model: LLMModel = Field(
        LLMModel.OPENAI_GPT4O, description="OpenAI model to use"
    )
    embedding_model: EmbeddingModel = Field(
        EmbeddingModel.OPENAI_3_SMALL, description="Embedding model"
    )

    # Vector Database Configuration
    vector_db_path: str = Field("vector_db", description="Path to vector database")
    collection_name: str = Field("mbs_codes", description="ChromaDB collection name")

    # Search Configuration
    max_search_results: int = Field(10, description="Maximum search results to return")
    similarity_threshold: float = Field(0.7, description="Minimum similarity threshold")

    # Chatbot Configuration
    max_conversation_history: int = Field(
        20, description="Maximum conversation history length"
    )
    enable_context_awareness: bool = Field(True, description="Enable context awareness")

    # Performance Configuration
    batch_size: int = Field(100, description="Batch size for embedding generation")
    cache_embeddings: bool = Field(True, description="Cache embeddings for reuse")


class ConversationState(BaseModel):
    """State of an ongoing conversation."""

    session_id: str = Field(..., description="Session identifier")
    messages: List[ChatMessage] = Field(
        default_factory=list, description="Conversation messages"
    )
    context: ChatContext = Field(
        default_factory=ChatContext, description="Current context"
    )
    current_suggestions: List[CodeSuggestion] = Field(
        default_factory=list, description="Current code suggestions"
    )
    conversation_goal: Optional[str] = Field(
        None, description="Goal of the conversation"
    )


class SearchRequest(BaseModel):
    """Request for searching MBS codes."""

    query: str = Field(..., description="Search query")
    search_type: SearchType = Field(
        SearchType.HYBRID, description="Type of search to perform"
    )
    max_results: int = Field(10, description="Maximum results to return")
    filters: Dict[str, Any] = Field(default_factory=dict, description="Search filters")
    context: Optional[ChatContext] = Field(None, description="Search context")


class SearchResponse(BaseModel):
    """Response from MBS code search."""

    results: List[SearchResult] = Field(
        default_factory=list, description="Search results"
    )
    total_found: int = Field(0, description="Total number of results found")
    search_time_ms: float = Field(0.0, description="Search time in milliseconds")
    suggestions: List[str] = Field(
        default_factory=list, description="Search suggestions"
    )
    follow_up_questions: List[str] = Field(
        default_factory=list, description="Follow-up questions"
    )
