"""
Gemini service for MBS AI Assistant MVP.

This module handles Google Gemini API interactions for text generation,
embeddings, and structured responses.
"""

import logging
from typing import Any, Dict, List, Optional, AsyncGenerator
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings

logger = logging.getLogger(__name__)


class GeminiService:
    """Service for Google Gemini API interactions."""

    def __init__(self):
        """Initialize the Gemini service."""
        self.api_key = settings.GEMINI_API_KEY
        self.model_name = settings.GEMINI_MODEL_NAME
        self.embedding_model = settings.GEMINI_EMBEDDING_MODEL

        # Configure Gemini
        genai.configure(api_key=self.api_key)

        # Initialize models
        self.model = genai.GenerativeModel(self.model_name)
        self.embedding_model_instance = genai.GenerativeModel(self.embedding_model)

        logger.info(f"Gemini service initialized with model: {self.model_name}")

    def generate_response_stream(
        self, prompt: str, system_prompt: Optional[str] = None
    ) -> AsyncGenerator[str, None]:
        """Generate streaming response from Gemini."""
        try:
            full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt

            response = self.model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=2048,
                ),
                safety_settings={
                    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                },
            )

            # For now, return the full response (streaming can be added later)
            if response.text:
                yield response.text

        except Exception as e:
            logger.error(f"Error generating Gemini response: {e}")
            yield f"Error: {str(e)}"

    def generate_structured_response(
        self, prompt: str, system_prompt: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generate structured response from Gemini."""
        try:
            full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt

            response = self.model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.3,
                    max_output_tokens=1024,
                ),
                safety_settings={
                    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                },
            )

            return {
                "success": True,
                "content": response.text if response.text else "",
                "model": self.model_name,
            }

        except Exception as e:
            logger.error(f"Error generating structured Gemini response: {e}")
            return {
                "success": False,
                "error": str(e),
                "content": "",
                "model": self.model_name,
            }

    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Get embeddings for a list of texts using Gemini."""
        try:
            embeddings = []

            for i, text in enumerate(texts):
                try:
                    # Use Gemini's embedding model
                    result = genai.embed_content(
                        model=self.embedding_model,
                        content=text,
                        task_type="retrieval_document",
                    )

                    if result and "embedding" in result:
                        embeddings.append(result["embedding"])
                    else:
                        logger.warning(
                            f"No embedding generated for text: {text[:50]}..."
                        )
                        embeddings.append([0.0] * 768)  # Fallback embedding

                except Exception as e:
                    if "quota" in str(e).lower() or "429" in str(e):
                        logger.warning(
                            f"Gemini quota exceeded for embedding {i+1}/{len(texts)}"
                        )
                        # Use fallback embeddings for remaining texts
                        embeddings.extend([[0.0] * 768 for _ in range(len(texts) - i)])
                        break
                    else:
                        logger.warning(
                            f"Error generating embedding for text {i+1}: {e}"
                        )
                        embeddings.append([0.0] * 768)  # Fallback embedding

            logger.info(f"Generated {len(embeddings)} embeddings using Gemini")
            return embeddings

        except Exception as e:
            logger.error(f"Error generating embeddings: {e}")
            # Return zero embeddings as fallback
            return [[0.0] * 768 for _ in texts]

    def analyze_medical_query(self, query: str) -> Dict[str, Any]:
        """Analyze a medical query to extract key information."""
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
        
        Return ONLY a JSON object with these fields. No other text.
        """

        try:
            response = self.generate_structured_response(query, system_prompt)

            if response["success"]:
                # Try to parse JSON response
                import json

                try:
                    # Clean the response content
                    content = response["content"].strip()

                    # Remove any markdown formatting
                    if content.startswith("```json"):
                        content = content[7:]
                    if content.endswith("```"):
                        content = content[:-3]
                    content = content.strip()

                    analysis = json.loads(content)

                    # Validate required fields
                    required_fields = [
                        "body_part",
                        "procedure_type",
                        "provider_type",
                        "location",
                    ]
                    for field in required_fields:
                        if field not in analysis:
                            analysis[field] = None

                    return analysis

                except json.JSONDecodeError as e:
                    logger.warning(f"Failed to parse JSON response: {e}")
                    logger.warning(f"Raw response: {response['content']}")

                    # Fallback to basic analysis
                    return self._basic_query_analysis(query)
            else:
                logger.warning(
                    f"Gemini analysis failed: {response.get('error', 'Unknown error')}"
                )
                return self._basic_query_analysis(query)

        except Exception as e:
            logger.error(f"Error analyzing medical query: {e}")
            return self._basic_query_analysis(query)

    def _basic_query_analysis(self, query: str) -> Dict[str, Any]:
        """Basic query analysis when AI is not available."""
        query_lower = query.lower()

        # Simple keyword-based analysis
        analysis = {
            "body_part": None,
            "procedure_type": None,
            "provider_type": None,
            "location": None,
            "specific_details": None,
            "patient_characteristics": None,
        }

        # Extract provider type
        if "general practitioner" in query_lower or "gp" in query_lower:
            analysis["provider_type"] = "general practitioner"
        elif "specialist" in query_lower:
            analysis["provider_type"] = "specialist"
        elif "consultant" in query_lower:
            analysis["provider_type"] = "consultant"

        # Extract procedure type
        if "consultation" in query_lower:
            analysis["procedure_type"] = "consultation"
        elif "examination" in query_lower:
            analysis["procedure_type"] = "examination"
        elif "surgery" in query_lower:
            analysis["procedure_type"] = "surgery"
        elif "imaging" in query_lower or "scan" in query_lower:
            analysis["procedure_type"] = "imaging"

        # Extract location
        if "consulting rooms" in query_lower:
            analysis["location"] = "consulting rooms"
        elif "hospital" in query_lower:
            analysis["location"] = "hospital"
        elif "home" in query_lower:
            analysis["location"] = "home"

        # Extract body parts
        body_parts = [
            "chest",
            "heart",
            "lung",
            "abdomen",
            "head",
            "neck",
            "back",
            "leg",
            "arm",
        ]
        for part in body_parts:
            if part in query_lower:
                analysis["body_part"] = part
                break

        return analysis

    def generate_follow_up_questions(
        self,
        query: str,
        suggested_codes: List[str],
        context: Optional[Dict[str, Any]] = None,
    ) -> List[str]:
        """Generate follow-up questions to narrow down code selection."""
        try:
            system_prompt = """
            You are a medical coding assistant. Given a doctor's query and suggested MBS codes,
            generate 3-5 concise follow-up questions to help narrow down the most appropriate code.
            Focus on details that differentiate the suggested codes or are missing from the initial query.
            Return only the questions, one per line.
            """

            context_info = f"Context: {context}" if context else ""
            prompt = f"""
            Doctor's query: {query}
            Suggested MBS codes: {', '.join(suggested_codes)}
            {context_info}
            Generate follow-up questions:
            """

            response = self.generate_structured_response(prompt, system_prompt)

            if response["success"]:
                # Split response into individual questions
                questions = [
                    q.strip() for q in response["content"].split("\n") if q.strip()
                ]
                logger.info(f"Generated {len(questions)} follow-up questions")
                return questions
            else:
                logger.warning(
                    f"Failed to generate follow-up questions: {response.get('error', 'Unknown error')}"
                )
                return self._generate_basic_follow_up_questions(query, suggested_codes)

        except Exception as e:
            logger.error(f"Error generating follow-up questions: {e}")
            return self._generate_basic_follow_up_questions(query, suggested_codes)

    def _generate_basic_follow_up_questions(
        self, query: str, suggested_codes: List[str]
    ) -> List[str]:
        """Generate basic follow-up questions when AI is not available."""
        questions = []

        query_lower = query.lower()

        # Basic questions based on common MBS code differentiators
        if "consultation" in query_lower:
            questions.extend(
                [
                    "Was this a standard consultation (Level A), long consultation (Level B), or very long consultation (Level C)?",
                    "What was the primary reason for the consultation?",
                    "Did the consultation involve any significant mental health component?",
                ]
            )

        if "examination" in query_lower:
            questions.extend(
                [
                    "What type of examination was performed?",
                    "Was this a comprehensive examination or focused examination?",
                    "Did the examination involve any specific body systems?",
                ]
            )

        if "surgery" in query_lower:
            questions.extend(
                [
                    "What type of surgical procedure was performed?",
                    "Was this performed under general or local anesthesia?",
                    "What was the complexity level of the surgery?",
                ]
            )

        # Generic questions if no specific type detected
        if not questions:
            questions.extend(
                [
                    "What was the primary reason for the procedure?",
                    "Were there any specific requirements or constraints?",
                    "What was the duration or complexity of the procedure?",
                ]
            )

        return questions[:5]  # Limit to 5 questions
