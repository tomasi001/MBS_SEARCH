"""
AI service configuration and main service for MBS Clarity AI assistant.

This module provides the main AI service that coordinates all AI functionality
including vector database, natural language search, and contextual chatbot.
"""

import logging
import os
from typing import Any, Dict, List, Optional

from mbs_clarity.ai_models import (
    AIConfig,
    ChatContext,
    ChatbotResponse,
    CodeSuggestion,
    NaturalLanguageQuery,
    SearchRequest,
    SearchResponse,
)
from mbs_clarity.contextual_chatbot import ContextualChatbotService
from mbs_clarity.natural_language_search import NaturalLanguageSearchService
from mbs_clarity.vector_db import VectorDatabaseService

logger = logging.getLogger(__name__)


class MBSAIService:
    """Main AI service for MBS Clarity."""

    def __init__(self, config: Optional[AIConfig] = None):
        """Initialize the MBS AI service."""
        self.config = config or self._create_default_config()
        self.vector_db = None
        self.natural_language_search = None
        self.chatbot = None
        self._initialize_services()

    def _create_default_config(self) -> AIConfig:
        """Create default AI configuration."""
        return AIConfig(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            openai_model="gpt-4o",
            embedding_model="sentence-transformers/all-MiniLM-L6-v2",  # Use local embeddings
            vector_db_path="vector_db",
            collection_name="mbs_codes",
            max_search_results=10,
            similarity_threshold=0.5,  # Lower threshold for better results
            max_conversation_history=20,
            enable_context_awareness=True,
            batch_size=100,
            cache_embeddings=True,
        )

    def _initialize_services(self) -> None:
        """Initialize all AI services."""
        try:
            logger.info("Initializing MBS AI services...")

            # Initialize vector database service
            self.vector_db = VectorDatabaseService(self.config)
            logger.info("Vector database service initialized")

            # Initialize natural language search service
            self.natural_language_search = NaturalLanguageSearchService(self.config)
            logger.info("Natural language search service initialized")

            # Initialize contextual chatbot service
            self.chatbot = ContextualChatbotService(self.config)
            logger.info("Contextual chatbot service initialized")

            logger.info("All AI services initialized successfully")

        except Exception as e:
            logger.error(f"Failed to initialize AI services: {e}")
            raise

    def process_natural_language_query(
        self, query: str, context: Optional[ChatContext] = None
    ) -> NaturalLanguageQuery:
        """Process a natural language query."""
        if not self.natural_language_search:
            raise RuntimeError("Natural language search service not initialized")

        return self.natural_language_search.process_natural_language_query(
            query, context
        )

    def search_codes(
        self,
        query: str,
        search_type: str = "hybrid",
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None,
    ) -> SearchResponse:
        """Search for MBS codes."""
        if not self.natural_language_search:
            raise RuntimeError("Natural language search service not initialized")

        request = SearchRequest(
            query=query,
            search_type=search_type,
            max_results=max_results,
            filters=filters or {},
        )

        return self.natural_language_search.search_with_filters(request)

    def chat_with_context(
        self, session_id: str, message: str, context: Optional[ChatContext] = None
    ) -> ChatbotResponse:
        """Chat with contextual awareness."""
        if not self.chatbot:
            raise RuntimeError("Chatbot service not initialized")

        return self.chatbot.process_message(session_id, message, context)

    def start_chat_session(
        self,
        session_id: Optional[str] = None,
        initial_context: Optional[ChatContext] = None,
    ) -> str:
        """Start a new chat session."""
        if not self.chatbot:
            raise RuntimeError("Chatbot service not initialized")

        return self.chatbot.start_conversation(session_id, initial_context)

    def get_detailed_code_suggestions(
        self, suggested_codes: List[str], query: str
    ) -> List[CodeSuggestion]:
        """Get detailed suggestions for MBS codes."""
        if not self.natural_language_search:
            raise RuntimeError("Natural language search service not initialized")

        return self.natural_language_search.get_detailed_code_suggestions(
            suggested_codes, query
        )

    def populate_vector_database(self) -> None:
        """Populate the vector database with MBS data."""
        if not self.vector_db:
            raise RuntimeError("Vector database service not initialized")

        self.vector_db.populate_vector_db()

    def get_vector_db_stats(self) -> Dict[str, Any]:
        """Get vector database statistics."""
        if not self.vector_db:
            raise RuntimeError("Vector database service not initialized")

        return self.vector_db.get_stats()

    def reset_vector_database(self) -> None:
        """Reset the vector database."""
        if not self.vector_db:
            raise RuntimeError("Vector database service not initialized")

        self.vector_db.reset_database()

    def get_chat_history(self, session_id: str) -> List[Dict[str, str]]:
        """Get chat history for a session."""
        if not self.chatbot:
            raise RuntimeError("Chatbot service not initialized")

        messages = self.chatbot.get_conversation_history(session_id)
        return [
            {"role": msg.role, "content": msg.content, "timestamp": msg.timestamp or ""}
            for msg in messages
        ]

    def clear_chat_session(self, session_id: str) -> bool:
        """Clear a chat session."""
        if not self.chatbot:
            raise RuntimeError("Chatbot service not initialized")

        return self.chatbot.clear_conversation(session_id)

    def is_ai_enabled(self) -> bool:
        """Check if AI features are enabled."""
        return (
            self.vector_db is not None
            and self.natural_language_search is not None
            and self.chatbot is not None
        )

    def get_service_status(self) -> Dict[str, Any]:
        """Get status of all AI services."""
        status = {
            "ai_enabled": self.is_ai_enabled(),
            "vector_db_initialized": self.vector_db is not None,
            "natural_language_search_initialized": self.natural_language_search
            is not None,
            "chatbot_initialized": self.chatbot is not None,
            "openai_available": bool(self.config.openai_api_key),
            "embedding_model": self.config.embedding_model.value,
            "llm_model": self.config.openai_model.value,
        }

        if self.vector_db:
            try:
                stats = self.get_vector_db_stats()
                status["vector_db_stats"] = stats
            except Exception as e:
                status["vector_db_error"] = str(e)

        return status


# Global AI service instance
_ai_service: Optional[MBSAIService] = None


def get_ai_service() -> MBSAIService:
    """Get the global AI service instance."""
    global _ai_service
    if _ai_service is None:
        _ai_service = MBSAIService()
    return _ai_service


def initialize_ai_service(config: Optional[AIConfig] = None) -> MBSAIService:
    """Initialize the global AI service with configuration."""
    global _ai_service
    _ai_service = MBSAIService(config)
    return _ai_service


def reset_ai_service() -> None:
    """Reset the global AI service."""
    global _ai_service
    _ai_service = None
