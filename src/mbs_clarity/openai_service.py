"""
OpenAI service for MBS Clarity AI assistant.

This module handles OpenAI API interactions for embeddings, chat completions,
and natural language processing tasks.
"""

import logging
import os
from typing import Any, Dict, List, Optional

import openai
from openai import OpenAI

from mbs_clarity.ai_models import AIConfig, ChatMessage, LLMModel

logger = logging.getLogger(__name__)


class OpenAIService:
    """Service for OpenAI API interactions."""

    def __init__(self, config: AIConfig):
        """Initialize the OpenAI service."""
        self.config = config
        self.client = None
        self._initialize_client()

    def _initialize_client(self) -> None:
        """Initialize OpenAI client."""
        try:
            api_key = self.config.openai_api_key or os.getenv("OPENAI_API_KEY")
            if not api_key:
                logger.warning("OpenAI API key not found. Some features may not work.")
                return

            self.client = OpenAI(api_key=api_key)
            logger.info("OpenAI client initialized successfully")

        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            raise

    def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts."""
        if not self.client:
            raise RuntimeError("OpenAI client not initialized")

        try:
            logger.info(f"Generating embeddings for {len(texts)} texts")

            response = self.client.embeddings.create(
                model=self.config.embedding_model.value, input=texts
            )

            embeddings = [data.embedding for data in response.data]
            logger.info(f"Generated {len(embeddings)} embeddings")

            return embeddings

        except Exception as e:
            logger.error(f"Error generating embeddings: {e}")
            raise

    def generate_chat_completion(
        self,
        messages: List[ChatMessage],
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        system_prompt: Optional[str] = None,
    ) -> str:
        """Generate a chat completion response."""
        if not self.client:
            raise RuntimeError("OpenAI client not initialized")

        try:
            # Prepare messages
            openai_messages = []

            if system_prompt:
                openai_messages.append({"role": "system", "content": system_prompt})

            for message in messages:
                openai_messages.append(
                    {"role": message.role, "content": message.content}
                )

            logger.info(
                f"Generating chat completion with {len(openai_messages)} messages"
            )

            response = self.client.chat.completions.create(
                model=self.config.openai_model.value,
                messages=openai_messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )

            content = response.choices[0].message.content
            logger.info("Generated chat completion successfully")

            return content

        except Exception as e:
            logger.error(f"Error generating chat completion: {e}")
            raise

    def analyze_medical_query(self, query: str) -> Dict[str, Any]:
        """Analyze a medical query to extract key information."""
        if not self.client:
            raise RuntimeError("OpenAI client not initialized")

        system_prompt = """
        You are a medical coding assistant. Analyze the following medical procedure description
        and extract key information for MBS code matching.
        
        Extract:
        1. Body part/organ mentioned
        2. Procedure type (consultation, surgery, imaging, etc.)
        3. Specific details (left/right, duration, complexity)
        4. Patient characteristics (age, condition)
        5. Provider type (GP, specialist, etc.)
        6. Location (consulting rooms, hospital, etc.)
        
        Return a JSON object with these fields.
        """

        try:
            messages = [
                ChatMessage(role="system", content=system_prompt),
                ChatMessage(
                    role="user", content=f"Analyze this medical query: {query}"
                ),
            ]

            response = self.generate_chat_completion(
                messages=messages, temperature=0.3, max_tokens=500
            )

            # Try to parse JSON response
            import json

            try:
                analysis = json.loads(response)
                logger.info("Successfully analyzed medical query")
                return analysis
            except json.JSONDecodeError:
                logger.warning("Failed to parse JSON response, returning raw text")
                return {"raw_response": response}

        except Exception as e:
            logger.error(f"Error analyzing medical query: {e}")
            return {"error": str(e)}

    def generate_follow_up_questions(
        self,
        query: str,
        suggested_codes: List[str],
        context: Optional[Dict[str, Any]] = None,
    ) -> List[str]:
        """Generate follow-up questions to narrow down code selection."""
        if not self.client:
            raise RuntimeError("OpenAI client not initialized")

        system_prompt = """
        You are a medical coding assistant. Given a doctor's query and suggested MBS codes,
        generate 3-5 follow-up questions to help narrow down the correct code.
        
        Focus on:
        - Specific details (left/right, duration, complexity)
        - Patient characteristics
        - Procedure specifics
        - Location requirements
        
        Return only the questions, one per line.
        """

        try:
            context_info = ""
            if context:
                context_info = f"Context: {context}"

            prompt = f"""
            Doctor's query: {query}
            
            Suggested codes: {', '.join(suggested_codes)}
            
            {context_info}
            
            Generate follow-up questions:
            """

            messages = [
                ChatMessage(role="system", content=system_prompt),
                ChatMessage(role="user", content=prompt),
            ]

            response = self.generate_chat_completion(
                messages=messages, temperature=0.7, max_tokens=300
            )

            # Split response into individual questions
            questions = [q.strip() for q in response.split("\n") if q.strip()]
            logger.info(f"Generated {len(questions)} follow-up questions")

            return questions

        except Exception as e:
            logger.error(f"Error generating follow-up questions: {e}")
            return []

    def explain_mbs_code(
        self,
        item_num: str,
        code_details: Dict[str, Any],
        user_context: Optional[str] = None,
    ) -> str:
        """Generate a human-readable explanation of an MBS code."""
        if not self.client:
            raise RuntimeError("OpenAI client not initialized")

        system_prompt = """
        You are a medical coding assistant. Explain an MBS code in simple, clear language
        that a doctor can easily understand. Focus on:
        
        1. What the code covers
        2. When to use it
        3. Key requirements
        4. Important exclusions
        5. Practical examples
        
        Use clear, professional language suitable for healthcare professionals.
        """

        try:
            prompt = f"""
            MBS Code: {item_num}
            
            Code Details:
            - Description: {code_details.get('description', 'N/A')}
            - Category: {code_details.get('category', 'N/A')}
            - Fee: ${code_details.get('schedule_fee', 'N/A')}
            - Relations: {code_details.get('relations', [])}
            - Constraints: {code_details.get('constraints', [])}
            
            User Context: {user_context or 'No specific context provided'}
            
            Explain this MBS code:
            """

            messages = [
                ChatMessage(role="system", content=system_prompt),
                ChatMessage(role="user", content=prompt),
            ]

            response = self.generate_chat_completion(
                messages=messages, temperature=0.5, max_tokens=800
            )

            logger.info(f"Generated explanation for MBS code {item_num}")
            return response

        except Exception as e:
            logger.error(f"Error explaining MBS code: {e}")
            return f"Error generating explanation: {str(e)}"

    def suggest_related_codes(
        self, query: str, current_codes: List[str], search_results: List[Dict[str, Any]]
    ) -> List[str]:
        """Suggest related MBS codes based on query and context."""
        if not self.client:
            raise RuntimeError("OpenAI client not initialized")

        system_prompt = """
        You are a medical coding assistant. Based on a doctor's query and search results,
        suggest the most relevant MBS codes. Consider:
        
        1. Exact matches for the described procedure
        2. Related procedures that might be relevant
        3. Prerequisites or follow-up procedures
        4. Alternative codes for similar procedures
        
        Return only the MBS item numbers, separated by commas.
        """

        try:
            results_summary = "\n".join(
                [
                    f"- {result.get('item_num', 'N/A')}: {result.get('content', 'N/A')[:100]}..."
                    for result in search_results[:5]
                ]
            )

            prompt = f"""
            Doctor's query: {query}
            
            Current codes being considered: {', '.join(current_codes)}
            
            Search results:
            {results_summary}
            
            Suggest the most relevant MBS codes:
            """

            messages = [
                ChatMessage(role="system", content=system_prompt),
                ChatMessage(role="user", content=prompt),
            ]

            response = self.generate_chat_completion(
                messages=messages, temperature=0.3, max_tokens=200
            )

            # Parse response to extract codes
            codes = [
                code.strip() for code in response.split(",") if code.strip().isdigit()
            ]
            logger.info(f"Suggested {len(codes)} related codes")

            return codes

        except Exception as e:
            logger.error(f"Error suggesting related codes: {e}")
            return []
