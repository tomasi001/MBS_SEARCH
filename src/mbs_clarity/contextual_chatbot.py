"""
Contextual chatbot service for MBS Clarity AI assistant.

This module handles contextual conversations with doctors, providing
AI-powered assistance for MBS code selection and explanation.
"""

import logging
import time
import uuid
from typing import Any, Dict, List, Optional

from mbs_clarity.ai_models import (
    AIConfig,
    ChatContext,
    ChatMessage,
    ChatbotResponse,
    CodeSuggestion,
    ConversationState,
)
from mbs_clarity.db import fetch_item_aggregate
from mbs_clarity.natural_language_search import NaturalLanguageSearchService
from mbs_clarity.openai_service import OpenAIService

logger = logging.getLogger(__name__)


class ContextualChatbotService:
    """Service for contextual chatbot conversations."""

    def __init__(self, config: AIConfig):
        """Initialize the contextual chatbot service."""
        self.config = config
        self.openai_service = OpenAIService(config)
        self.natural_language_search = NaturalLanguageSearchService(config)
        self.conversations: Dict[str, ConversationState] = {}

    def start_conversation(
        self,
        session_id: Optional[str] = None,
        initial_context: Optional[ChatContext] = None,
    ) -> str:
        """Start a new conversation session."""
        if not session_id:
            session_id = str(uuid.uuid4())

        self.conversations[session_id] = ConversationState(
            session_id=session_id,
            context=initial_context or ChatContext(),
            conversation_goal=None,
        )

        logger.info(f"Started new conversation: {session_id}")
        return session_id

    def process_message(
        self, session_id: str, message: str, context: Optional[ChatContext] = None
    ) -> ChatbotResponse:
        """Process a message in a conversation."""
        logger.info(f"Processing message in session {session_id}: '{message}'")

        try:
            # Get or create conversation
            if session_id not in self.conversations:
                self.start_conversation(session_id, context)

            conversation = self.conversations[session_id]

            # Update context if provided
            if context:
                conversation.context = context

            # Add user message to conversation
            user_message = ChatMessage(
                role="user",
                content=message,
                timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
            )
            conversation.messages.append(user_message)

            # Determine conversation intent
            intent = self._analyze_intent(message, conversation)

            # Generate response based on intent
            response = self._generate_response(message, intent, conversation)

            # Add assistant message to conversation
            assistant_message = ChatMessage(
                role="assistant",
                content=response.message,
                timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
            )
            conversation.messages.append(assistant_message)

            # Update conversation state
            if response.code_suggestions:
                conversation.current_suggestions = response.code_suggestions

            # Trim conversation history if too long
            if len(conversation.messages) > self.config.max_conversation_history:
                conversation.messages = conversation.messages[
                    -self.config.max_conversation_history :
                ]

            logger.info(f"Generated response for session {session_id}")
            return response

        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return ChatbotResponse(
                message=f"I apologize, but I encountered an error: {str(e)}",
                suggested_actions=[],
                code_suggestions=[],
                follow_up_questions=[],
                context_updated=False,
            )

    def _analyze_intent(self, message: str, conversation: ConversationState) -> str:
        """Analyze the intent of the user's message."""
        message_lower = message.lower()

        # Intent keywords
        if any(
            word in message_lower
            for word in ["explain", "what does", "tell me about", "describe"]
        ):
            return "explain_code"
        elif any(
            word in message_lower
            for word in ["find", "search", "look for", "need code"]
        ):
            return "search_codes"
        elif any(
            word in message_lower for word in ["compare", "difference", "vs", "versus"]
        ):
            return "compare_codes"
        elif any(
            word in message_lower for word in ["when to use", "appropriate", "suitable"]
        ):
            return "usage_guidance"
        elif any(word in message_lower for word in ["help", "assist", "guide"]):
            return "general_help"
        elif any(word in message_lower for word in ["yes", "no", "correct", "wrong"]):
            return "confirmation"
        else:
            return "general_query"

    def _generate_response(
        self, message: str, intent: str, conversation: ConversationState
    ) -> ChatbotResponse:
        """Generate a response based on the intent."""

        if intent == "explain_code":
            return self._handle_explain_code(message, conversation)
        elif intent == "search_codes":
            return self._handle_search_codes(message, conversation)
        elif intent == "compare_codes":
            return self._handle_compare_codes(message, conversation)
        elif intent == "usage_guidance":
            return self._handle_usage_guidance(message, conversation)
        elif intent == "confirmation":
            return self._handle_confirmation(message, conversation)
        else:
            return self._handle_general_query(message, conversation)

    def _handle_explain_code(
        self, message: str, conversation: ConversationState
    ) -> ChatbotResponse:
        """Handle requests to explain MBS codes."""
        try:
            # Extract code numbers from message
            import re

            codes = re.findall(r"\b\d+\b", message)

            if not codes:
                return ChatbotResponse(
                    message="I'd be happy to explain an MBS code! Please specify which code number you'd like me to explain.",
                    suggested_actions=["Enter a code number"],
                    code_suggestions=[],
                    follow_up_questions=[
                        "Which MBS code would you like me to explain?"
                    ],
                    context_updated=False,
                )

            explanations = []
            suggestions = []

            for code in codes[:3]:  # Limit to 3 codes
                item_data = fetch_item_aggregate(code)
                if item_data:
                    # Generate AI explanation if available
                    if self.openai_service.client:
                        explanation = self.openai_service.explain_mbs_code(
                            item_num=code, code_details=item_data, user_context=message
                        )
                    else:
                        explanation = self._generate_basic_explanation(item_data)

                    explanations.append(f"**MBS Code {code}:**\n{explanation}")

                    # Create code suggestion
                    suggestions.append(
                        CodeSuggestion(
                            item_num=code,
                            confidence=1.0,
                            reasoning="Code explanation requested",
                            requirements=self._extract_requirements(item_data),
                            exclusions=self._extract_exclusions(item_data),
                            follow_up_questions=[],
                        )
                    )

            if explanations:
                response_message = "\n\n".join(explanations)
                return ChatbotResponse(
                    message=response_message,
                    suggested_actions=[
                        "Search for related codes",
                        "Compare with other codes",
                    ],
                    code_suggestions=suggestions,
                    follow_up_questions=[
                        "Would you like me to find related codes?",
                        "Do you need help comparing this with other codes?",
                    ],
                    context_updated=True,
                )
            else:
                return ChatbotResponse(
                    message="I couldn't find the MBS codes you mentioned. Please check the code numbers and try again.",
                    suggested_actions=["Verify code numbers"],
                    code_suggestions=[],
                    follow_up_questions=["What codes were you looking for?"],
                    context_updated=False,
                )

        except Exception as e:
            logger.error(f"Error explaining codes: {e}")
            return ChatbotResponse(
                message=f"Sorry, I encountered an error while explaining the codes: {str(e)}",
                suggested_actions=[],
                code_suggestions=[],
                follow_up_questions=[],
                context_updated=False,
            )

    def _handle_search_codes(
        self, message: str, conversation: ConversationState
    ) -> ChatbotResponse:
        """Handle requests to search for MBS codes."""
        try:
            # Process natural language query
            nl_query = self.natural_language_search.process_natural_language_query(
                query=message, context=conversation.context
            )

            if nl_query.suggested_codes:
                # Get detailed suggestions
                suggestions = (
                    self.natural_language_search.get_detailed_code_suggestions(
                        suggested_codes=nl_query.suggested_codes, query=message
                    )
                )

                # Generate response message
                response_parts = [
                    f"I found {len(suggestions)} MBS codes that might match your description:"
                ]

                for i, suggestion in enumerate(suggestions[:5], 1):
                    response_parts.append(
                        f"{i}. **Code {suggestion.item_num}** (Confidence: {suggestion.confidence:.1%})\n"
                        f"   {suggestion.reasoning}"
                    )

                response_message = "\n".join(response_parts)

                return ChatbotResponse(
                    message=response_message,
                    suggested_actions=[
                        "Select a code",
                        "Refine search",
                        "Get more details",
                    ],
                    code_suggestions=suggestions,
                    follow_up_questions=nl_query.follow_up_questions,
                    context_updated=True,
                )
            else:
                return ChatbotResponse(
                    message="I couldn't find any MBS codes matching your description. Could you provide more specific details about the procedure?",
                    suggested_actions=[
                        "Provide more details",
                        "Try different keywords",
                    ],
                    code_suggestions=[],
                    follow_up_questions=[
                        "What type of procedure was performed?",
                        "Which body part was involved?",
                        "What was the duration of the procedure?",
                    ],
                    context_updated=False,
                )

        except Exception as e:
            logger.error(f"Error searching codes: {e}")
            return ChatbotResponse(
                message=f"Sorry, I encountered an error while searching: {str(e)}",
                suggested_actions=[],
                code_suggestions=[],
                follow_up_questions=[],
                context_updated=False,
            )

    def _handle_compare_codes(
        self, message: str, conversation: ConversationState
    ) -> ChatbotResponse:
        """Handle requests to compare MBS codes."""
        try:
            # Extract code numbers from message
            import re

            codes = re.findall(r"\b\d+\b", message)

            if len(codes) < 2:
                return ChatbotResponse(
                    message="I can help you compare MBS codes! Please provide at least two code numbers to compare.",
                    suggested_actions=["Enter two or more code numbers"],
                    code_suggestions=[],
                    follow_up_questions=["Which codes would you like me to compare?"],
                    context_updated=False,
                )

            # Get details for each code
            comparisons = []
            suggestions = []

            for code in codes[:3]:  # Limit to 3 codes
                item_data = fetch_item_aggregate(code)
                if item_data:
                    comparisons.append({"code": code, "data": item_data})

                    suggestions.append(
                        CodeSuggestion(
                            item_num=code,
                            confidence=1.0,
                            reasoning="Code comparison requested",
                            requirements=self._extract_requirements(item_data),
                            exclusions=self._extract_exclusions(item_data),
                            follow_up_questions=[],
                        )
                    )

            if len(comparisons) >= 2:
                # Generate comparison
                comparison_text = self._generate_comparison(comparisons)

                return ChatbotResponse(
                    message=comparison_text,
                    suggested_actions=["Choose best code", "Get more details"],
                    code_suggestions=suggestions,
                    follow_up_questions=[
                        "Which code seems most appropriate?",
                        "Do you need more details about any specific code?",
                    ],
                    context_updated=True,
                )
            else:
                return ChatbotResponse(
                    message="I couldn't find enough valid MBS codes to compare. Please check the code numbers.",
                    suggested_actions=["Verify code numbers"],
                    code_suggestions=[],
                    follow_up_questions=["What codes were you trying to compare?"],
                    context_updated=False,
                )

        except Exception as e:
            logger.error(f"Error comparing codes: {e}")
            return ChatbotResponse(
                message=f"Sorry, I encountered an error while comparing codes: {str(e)}",
                suggested_actions=[],
                code_suggestions=[],
                follow_up_questions=[],
                context_updated=False,
            )

    def _handle_usage_guidance(
        self, message: str, conversation: ConversationState
    ) -> ChatbotResponse:
        """Handle requests for usage guidance."""
        try:
            # Extract code numbers from message
            import re

            codes = re.findall(r"\b\d+\b", message)

            if not codes:
                return ChatbotResponse(
                    message="I can provide usage guidance for MBS codes! Please specify which code you'd like guidance on.",
                    suggested_actions=["Enter a code number"],
                    code_suggestions=[],
                    follow_up_questions=["Which MBS code do you need guidance on?"],
                    context_updated=False,
                )

            guidance_parts = []
            suggestions = []

            for code in codes[:2]:  # Limit to 2 codes
                item_data = fetch_item_aggregate(code)
                if item_data:
                    guidance = self._generate_usage_guidance(item_data)
                    guidance_parts.append(
                        f"**Code {code} Usage Guidance:**\n{guidance}"
                    )

                    suggestions.append(
                        CodeSuggestion(
                            item_num=code,
                            confidence=1.0,
                            reasoning="Usage guidance requested",
                            requirements=self._extract_requirements(item_data),
                            exclusions=self._extract_exclusions(item_data),
                            follow_up_questions=[],
                        )
                    )

            if guidance_parts:
                response_message = "\n\n".join(guidance_parts)
                return ChatbotResponse(
                    message=response_message,
                    suggested_actions=["Find similar codes", "Check requirements"],
                    code_suggestions=suggestions,
                    follow_up_questions=[
                        "Are there any specific scenarios you're unsure about?",
                        "Do you need help with the requirements?",
                    ],
                    context_updated=True,
                )
            else:
                return ChatbotResponse(
                    message="I couldn't find the MBS codes you mentioned for usage guidance.",
                    suggested_actions=["Verify code numbers"],
                    code_suggestions=[],
                    follow_up_questions=["What codes were you looking for?"],
                    context_updated=False,
                )

        except Exception as e:
            logger.error(f"Error providing usage guidance: {e}")
            return ChatbotResponse(
                message=f"Sorry, I encountered an error providing guidance: {str(e)}",
                suggested_actions=[],
                code_suggestions=[],
                follow_up_questions=[],
                context_updated=False,
            )

    def _handle_confirmation(
        self, message: str, conversation: ConversationState
    ) -> ChatbotResponse:
        """Handle confirmation responses."""
        message_lower = message.lower()

        if any(word in message_lower for word in ["yes", "correct", "right", "good"]):
            if conversation.current_suggestions:
                return ChatbotResponse(
                    message="Great! I'm glad I could help. Is there anything else you'd like to know about these codes?",
                    suggested_actions=["Get more details", "Find related codes"],
                    code_suggestions=conversation.current_suggestions,
                    follow_up_questions=[
                        "Would you like more details about any of these codes?",
                        "Do you need help with the billing requirements?",
                    ],
                    context_updated=False,
                )
            else:
                return ChatbotResponse(
                    message="Perfect! Is there anything else I can help you with regarding MBS codes?",
                    suggested_actions=["Search for codes", "Get explanations"],
                    code_suggestions=[],
                    follow_up_questions=["What else would you like to know?"],
                    context_updated=False,
                )
        else:
            return ChatbotResponse(
                message="I understand. Let me help you find the right information. Could you provide more details about what you're looking for?",
                suggested_actions=["Provide more details", "Try different search"],
                code_suggestions=[],
                follow_up_questions=[
                    "What specific information do you need?",
                    "How can I better assist you?",
                ],
                context_updated=False,
            )

    def _handle_general_query(
        self, message: str, conversation: ConversationState
    ) -> ChatbotResponse:
        """Handle general queries."""
        return ChatbotResponse(
            message="I'm here to help you with MBS codes! You can ask me to:\n\n• Explain specific codes\n• Search for codes based on procedures\n• Compare different codes\n• Provide usage guidance\n\nWhat would you like to know?",
            suggested_actions=["Search for codes", "Explain a code", "Get help"],
            code_suggestions=[],
            follow_up_questions=[
                "What type of procedure are you looking for?",
                "Do you have a specific code you'd like explained?",
                "Would you like me to help you find the right code?",
            ],
            context_updated=False,
        )

    def _generate_basic_explanation(self, item_data: Dict[str, Any]) -> str:
        """Generate a basic explanation when AI is not available."""
        description = item_data.get("description", "")
        constraints = item_data.get("constraints", [])

        explanation_parts = [f"Description: {description}"]

        if constraints:
            constraint_text = "; ".join(
                [
                    f"{c.get('constraint_type', '')}: {c.get('value', '')}"
                    for c in constraints[:5]
                ]
            )
            explanation_parts.append(f"Key requirements: {constraint_text}")

        return "\n".join(explanation_parts)

    def _generate_comparison(self, comparisons: List[Dict[str, Any]]) -> str:
        """Generate a comparison between codes."""
        if len(comparisons) < 2:
            return "Not enough codes to compare."

        comparison_parts = ["**MBS Code Comparison:**\n"]

        for comp in comparisons:
            code = comp["code"]
            data = comp["data"]
            description = data.get("description", "")
            fee = data.get("schedule_fee", 0)

            comparison_parts.append(
                f"**Code {code}:**\n"
                f"- Fee: ${fee}\n"
                f"- Description: {description[:100]}...\n"
            )

        comparison_parts.append(
            "\n**Key Differences:**\n"
            "- Compare fees, requirements, and applicability\n"
            "- Consider patient characteristics and procedure details\n"
            "- Check for any exclusions or restrictions"
        )

        return "\n".join(comparison_parts)

    def _generate_usage_guidance(self, item_data: Dict[str, Any]) -> str:
        """Generate usage guidance for a code."""
        description = item_data.get("description", "")
        constraints = item_data.get("constraints", [])

        guidance_parts = [
            f"**When to use this code:**\n{description}\n",
            "**Key requirements:**",
        ]

        for constraint in constraints[:5]:
            constraint_type = constraint.get("constraint_type", "")
            value = constraint.get("value", "")

            if constraint_type == "requirement":
                guidance_parts.append(f"• {value}")
            elif constraint_type == "duration_min_minutes":
                guidance_parts.append(f"• Minimum duration: {value} minutes")
            elif constraint_type == "location":
                guidance_parts.append(f"• Location: {value}")
            elif constraint_type == "provider":
                guidance_parts.append(f"• Provider type: {value}")

        return "\n".join(guidance_parts)

    def _extract_requirements(self, item_data: Dict[str, Any]) -> List[str]:
        """Extract requirements from item data."""
        requirements = []
        constraints = item_data.get("constraints", [])

        for constraint in constraints:
            constraint_type = constraint.get("constraint_type", "")
            value = constraint.get("value", "")

            if constraint_type == "requirement":
                requirements.append(value)
            elif constraint_type in ["duration_min_minutes", "duration_max_minutes"]:
                requirements.append(f"Duration: {value} minutes")
            elif constraint_type == "location":
                requirements.append(f"Location: {value}")
            elif constraint_type == "provider":
                requirements.append(f"Provider: {value}")

        return requirements

    def _extract_exclusions(self, item_data: Dict[str, Any]) -> List[str]:
        """Extract exclusions from item data."""
        exclusions = []
        relations = item_data.get("relations", [])

        for relation in relations:
            if relation.get("relation_type") == "excludes":
                target_item = relation.get("target_item_num")
                detail = relation.get("detail", "")
                if target_item:
                    exclusions.append(f"Excludes item {target_item}: {detail}")
                else:
                    exclusions.append(f"General exclusion: {detail}")

        return exclusions

    def get_conversation_history(self, session_id: str) -> List[ChatMessage]:
        """Get conversation history for a session."""
        if session_id in self.conversations:
            return self.conversations[session_id].messages
        return []

    def clear_conversation(self, session_id: str) -> bool:
        """Clear conversation history for a session."""
        if session_id in self.conversations:
            del self.conversations[session_id]
            logger.info(f"Cleared conversation: {session_id}")
            return True
        return False
