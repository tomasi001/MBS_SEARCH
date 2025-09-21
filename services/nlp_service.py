"""
Natural Language Processing service for MBS AI Assistant MVP.

This module handles natural language queries from doctors and converts them
into relevant MBS code suggestions using Gemini and vector search.
"""

import logging
import time
from typing import Any, Dict, List, Optional

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.gemini_service import GeminiService
from services.vector_service import VectorService
from config import settings
from src.mbs_clarity.db import fetch_item_aggregate

logger = logging.getLogger(__name__)


class NLPService:
    """Service for natural language MBS code search."""

    def __init__(self):
        """Initialize the NLP service."""
        self.gemini_service = GeminiService()
        self.vector_service = VectorService()

        logger.info("NLP service initialized successfully")

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
        has_medical_content = any(
            keyword in query_lower for keyword in medical_keywords
        )

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

        has_non_medical_content = any(
            topic in query_lower for topic in non_medical_topics
        )

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

    def process_natural_language_query(
        self, query: str, context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Process a natural language query from a doctor."""
        logger.info(f"Processing natural language query: '{query}'")

        start_time = time.time()

        try:
            # Step 0: Validate query is MBS-related
            validation = self._validate_mbs_query(query)
            if not validation["valid"]:
                return {
                    "query": query,
                    "suggested_codes": [],
                    "detailed_suggestions": [],
                    "follow_up_questions": [],
                    "context": context or {},
                    "processing_time_ms": 0,
                    "error": validation["reason"],
                }

            # Step 1: Analyze the query using Gemini
            analysis = self.gemini_service.analyze_medical_query(query)

            # Step 2: Perform vector search
            search_results = self._perform_vector_search(query, analysis)

            # Step 3: Generate code suggestions
            suggested_codes = self._generate_code_suggestions(
                query, search_results, analysis
            )

            # Step 4: Generate follow-up questions
            follow_up_questions = self._generate_follow_up_questions(
                query, suggested_codes, analysis, context
            )

            processing_time = (time.time() - start_time) * 1000

            logger.info(
                f"Processed query in {processing_time:.1f}ms, found {len(suggested_codes)} suggestions"
            )

            return {
                "query": query,
                "suggested_codes": suggested_codes,
                "detailed_suggestions": self._get_detailed_suggestions(
                    suggested_codes, query, search_results
                ),
                "follow_up_questions": follow_up_questions,
                "context": context or {},
                "processing_time_ms": processing_time,
                "analysis": analysis,
            }

        except Exception as e:
            logger.error(f"Error processing natural language query: {e}")
            return {
                "query": query,
                "suggested_codes": [],
                "detailed_suggestions": [],
                "follow_up_questions": [],
                "context": context or {},
                "processing_time_ms": 0,
                "error": str(e),
            }

    def process_conversational_query(
        self,
        query: str,
        conversation_history: List[Dict[str, Any]],
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Process a conversational query with context from previous messages."""
        logger.info(f"Processing conversational query: '{query}'")

        start_time = time.time()

        try:
            # Build context from conversation history
            conversation_context = self._build_conversation_context(
                conversation_history, query
            )

            # Step 1: Analyze the query with conversation context
            analysis = self.gemini_service.analyze_medical_query(query)

            # Add conversation context to analysis
            analysis["conversation_context"] = conversation_context

            # Step 2: Perform vector search with conversation context
            search_query = self._build_contextual_search_query(
                query, conversation_context
            )
            search_results = self._perform_vector_search(search_query, analysis)

            # Step 3: Generate code suggestions
            suggested_codes = self._generate_code_suggestions(
                query, search_results, analysis
            )

            # Step 4: Generate contextual follow-up questions
            follow_up_questions = self._generate_contextual_follow_up_questions(
                query, suggested_codes, analysis, conversation_history, context
            )

            processing_time = (time.time() - start_time) * 1000

            logger.info(
                f"Processed conversational query in {processing_time:.1f}ms, found {len(suggested_codes)} suggestions"
            )

            return {
                "query": query,
                "suggested_codes": suggested_codes,
                "detailed_suggestions": self._get_detailed_suggestions(
                    suggested_codes, query, search_results
                ),
                "follow_up_questions": follow_up_questions,
                "context": context or {},
                "conversation_context": conversation_context,
                "processing_time_ms": processing_time,
                "analysis": analysis,
            }

        except Exception as e:
            logger.error(f"Error processing conversational query: {e}")
            return {
                "query": query,
                "suggested_codes": [],
                "detailed_suggestions": [],
                "follow_up_questions": [],
                "context": context or {},
                "conversation_context": {},
                "processing_time_ms": 0,
                "error": str(e),
            }

    def _build_conversation_context(
        self, conversation_history: List[Dict[str, Any]], current_query: str
    ) -> Dict[str, Any]:
        """Build context from conversation history."""
        context = {
            "previous_queries": [],
            "previous_suggestions": [],
            "refinement_attempts": 0,
            "current_focus": None,
        }

        if not conversation_history:
            return context

        # Extract previous queries and suggestions
        for message in conversation_history[-5:]:  # Last 5 messages for context
            if message.get("type") == "user":
                context["previous_queries"].append(message.get("content", ""))
            elif message.get("type") == "assistant":
                suggestions = message.get("suggested_codes", [])
                if suggestions:
                    context["previous_suggestions"].extend(suggestions)

        # Count refinement attempts
        context["refinement_attempts"] = len(context["previous_queries"])

        # Determine current focus based on conversation
        if context["previous_suggestions"]:
            context["current_focus"] = "refining_suggestions"
        else:
            context["current_focus"] = "initial_search"

        return context

    def _build_contextual_search_query(
        self, query: str, conversation_context: Dict[str, Any]
    ) -> str:
        """Build a search query that incorporates conversation context."""
        if conversation_context.get("current_focus") == "refining_suggestions":
            # If refining, include previous suggestions in search
            previous_suggestions = conversation_context.get("previous_suggestions", [])
            if previous_suggestions:
                return f"{query} related to codes {', '.join(previous_suggestions[:3])}"

        return query

    def _generate_contextual_follow_up_questions(
        self,
        query: str,
        suggested_codes: List[str],
        analysis: Dict[str, Any],
        conversation_history: List[Dict[str, Any]],
        context: Optional[Dict[str, Any]],
    ) -> List[str]:
        """Generate follow-up questions that are contextually aware of the conversation."""
        try:
            if not suggested_codes:
                return []

            # Build conversation context for follow-up generation
            conversation_summary = self._summarize_conversation(conversation_history)

            # Use Gemini to generate contextual follow-up questions
            system_prompt = f"""
            You are a medical coding assistant helping a doctor find the right MBS code.
            
            Conversation context: {conversation_summary}
            Current query: {query}
            Suggested codes: {', '.join(suggested_codes)}
            
            Generate 3-5 follow-up questions that:
            1. Build on the conversation context
            2. Help narrow down the most appropriate code
            3. Are specific to the current suggestions
            4. Avoid repeating previous questions
            
            Return only the questions, one per line.
            """

            response = self.gemini_service.generate_structured_response(
                query, system_prompt
            )

            if response["success"]:
                questions = [
                    q.strip() for q in response["content"].split("\n") if q.strip()
                ]
                logger.info(
                    f"Generated {len(questions)} contextual follow-up questions"
                )
                return questions
            else:
                logger.warning(
                    f"Failed to generate contextual follow-up questions: {response.get('error', 'Unknown error')}"
                )
                return self._generate_basic_contextual_questions(
                    query, suggested_codes, conversation_history
                )

        except Exception as e:
            logger.error(f"Error generating contextual follow-up questions: {e}")
            return self._generate_basic_contextual_questions(
                query, suggested_codes, conversation_history
            )

    def _summarize_conversation(
        self, conversation_history: List[Dict[str, Any]]
    ) -> str:
        """Summarize the conversation history for context."""
        if not conversation_history:
            return "No previous conversation"

        summary_parts = []

        for message in conversation_history[-3:]:  # Last 3 messages
            if message.get("type") == "user":
                summary_parts.append(f"Doctor asked: {message.get('content', '')}")
            elif message.get("type") == "assistant":
                suggestions = message.get("suggested_codes", [])
                if suggestions:
                    summary_parts.append(
                        f"Suggested codes: {', '.join(suggestions[:3])}"
                    )

        return "; ".join(summary_parts)

    def _generate_basic_contextual_questions(
        self,
        query: str,
        suggested_codes: List[str],
        conversation_history: List[Dict[str, Any]],
    ) -> List[str]:
        """Generate basic contextual questions when AI is not available."""
        questions = []

        # Check if this is a refinement attempt
        if len(conversation_history) > 1:
            questions.extend(
                [
                    "Are any of these codes closer to what you're looking for?",
                    "Would you like me to search for something more specific?",
                    "Do any of these suggestions match your procedure better?",
                ]
            )
        else:
            # First-time questions
            query_lower = query.lower()

            if "consultation" in query_lower:
                questions.extend(
                    [
                        "Was this a standard, long, or very long consultation?",
                        "What was the primary reason for the consultation?",
                        "Did the consultation involve any significant mental health component?",
                    ]
                )
            elif "examination" in query_lower:
                questions.extend(
                    [
                        "What type of examination was performed?",
                        "Was this a comprehensive or focused examination?",
                        "Did the examination involve any specific body systems?",
                    ]
                )
            else:
                questions.extend(
                    [
                        "What was the primary reason for the procedure?",
                        "Were there any specific requirements or constraints?",
                        "What was the duration or complexity of the procedure?",
                    ]
                )

        return questions[:5]  # Limit to 5 questions

    def _perform_vector_search(
        self, query: str, analysis: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Perform vector search using the vector database."""
        try:
            # Perform main search
            search_results = self.vector_service.search(
                query=query,
                max_results=20,
            )

            # If we have analysis results, try additional targeted searches
            if analysis and "provider_type" in analysis and analysis["provider_type"]:
                provider_type = analysis["provider_type"]
                provider_results = self.vector_service.search(
                    query=f"{provider_type} {analysis.get('procedure_type', '')}",
                    max_results=5,
                )

                # Merge results, avoiding duplicates
                existing_ids = {result["id"] for result in search_results}
                for result in provider_results:
                    if result["id"] not in existing_ids:
                        search_results.append(result)

            logger.info(f"Found {len(search_results)} vector search results")
            return search_results

        except Exception as e:
            logger.error(f"Error performing vector search: {e}")
            return []

    def _generate_code_suggestions(
        self, query: str, search_results: List[Dict[str, Any]], analysis: Dict[str, Any]
    ) -> List[str]:
        """Generate MBS code suggestions based on search results."""
        try:
            if not search_results:
                return []

            # Extract item numbers from search results
            suggested_items = []
            for result in search_results[:10]:  # Limit to top 10
                item_num = result["metadata"].get("item_num")
                if item_num:
                    suggested_items.append(item_num)

            # Use Gemini to refine suggestions
            if suggested_items:
                gemini_suggestions = self.gemini_service.generate_follow_up_questions(
                    query=query, suggested_codes=suggested_items, context=analysis
                )

                # For now, return the original suggestions (Gemini refinement can be added later)
                all_suggestions = list(set(suggested_items))
            else:
                all_suggestions = []

            logger.info(f"Generated {len(all_suggestions)} code suggestions")
            return all_suggestions[:15]  # Limit to 15 suggestions

        except Exception as e:
            logger.error(f"Error generating code suggestions: {e}")
            return []

    def _generate_follow_up_questions(
        self,
        query: str,
        suggested_codes: List[str],
        analysis: Dict[str, Any],
        context: Optional[Dict[str, Any]],
    ) -> List[str]:
        """Generate follow-up questions to narrow down code selection."""
        try:
            if not suggested_codes:
                return []

            # Use Gemini to generate follow-up questions
            questions = self.gemini_service.generate_follow_up_questions(
                query=query, suggested_codes=suggested_codes, context=analysis
            )

            logger.info(f"Generated {len(questions)} follow-up questions")
            return questions

        except Exception as e:
            logger.error(f"Error generating follow-up questions: {e}")
            return []

    def _get_detailed_suggestions(
        self,
        suggested_codes: List[str],
        query: str,
        search_results: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """Get detailed suggestions for MBS codes."""
        suggestions = []

        for item_num in suggested_codes:
            try:
                # Get detailed information for this code
                item_data = fetch_item_aggregate(item_num)
                if not item_data or not item_data[0]:
                    continue

                item_row, rel_rows, con_rows = item_data
                description = item_row[4] or "No description available"

                # Find the search result for this item
                search_result = None
                for result in search_results:
                    if result.get("metadata", {}).get("item_num") == item_num:
                        search_result = result
                        break

                # Calculate confidence based on actual similarity
                confidence = self._calculate_confidence_score(
                    query, description, search_result
                )

                # Generate meaningful reasoning based on matching words
                reasoning = self._generate_meaningful_reasoning(
                    query, description, item_num
                )

                suggestion = {
                    "code": item_num,
                    "description": description,
                    "confidence": confidence,
                    "reasoning": reasoning,
                    "requirements": [],
                    "exclusions": [],
                }
                suggestions.append(suggestion)

            except Exception as e:
                logger.error(f"Error processing code suggestion {item_num}: {e}")
                continue

        return suggestions

    def _calculate_confidence_score(
        self, query: str, description: str, search_result: Dict[str, Any]
    ) -> float:
        """Calculate a realistic confidence score based on actual similarity."""
        try:
            # Get the similarity score from the search result
            similarity_score = search_result.get("similarity_score", 0.0)

            # Convert similarity to confidence percentage (0-100%)
            # Similarity scores are typically 0-1, so multiply by 100
            base_confidence = similarity_score * 100

            # Apply additional factors for more realistic scoring
            query_lower = query.lower()
            description_lower = description.lower()

            # Bonus for exact word matches
            query_words = set(query_lower.split())
            description_words = set(description_lower.split())
            common_words = query_words.intersection(description_words)

            # Filter meaningful words
            meaningful_words = [word for word in common_words if len(word) > 3]
            word_match_bonus = min(len(meaningful_words) * 5, 20)  # Max 20% bonus

            # Bonus for medical term matches
            medical_terms = [
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
            ]

            medical_match_bonus = 0
            for term in medical_terms:
                if term in query_lower and term in description_lower:
                    medical_match_bonus += 10

            medical_match_bonus = min(medical_match_bonus, 30)  # Max 30% bonus

            # Calculate final confidence
            final_confidence = base_confidence + word_match_bonus + medical_match_bonus

            # Cap at 95% to avoid unrealistic scores
            final_confidence = min(final_confidence, 95.0)

            # Ensure minimum of 10% for any result
            final_confidence = max(final_confidence, 10.0)

            return round(final_confidence, 1)

        except Exception as e:
            logger.error(f"Error calculating confidence score: {e}")
            return 50.0  # Default fallback

    def _generate_meaningful_reasoning(
        self, query: str, description: str, item_num: str
    ) -> str:
        """Generate meaningful reasoning showing why this code was suggested."""
        try:
            # Convert both to lowercase for comparison
            query_lower = query.lower()
            description_lower = description.lower()

            # Find matching words/phrases
            matching_terms = []

            # Common medical terms to look for
            medical_terms = [
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
            ]

            # Check for exact matches
            for term in medical_terms:
                if term in query_lower and term in description_lower:
                    matching_terms.append(term)

            # Check for partial matches (words that appear in both)
            query_words = set(query_lower.split())
            description_words = set(description_lower.split())
            common_words = query_words.intersection(description_words)

            # Filter out common words that aren't meaningful
            meaningful_words = [
                word
                for word in common_words
                if len(word) > 3
                and word
                not in [
                    "the",
                    "and",
                    "for",
                    "with",
                    "this",
                    "that",
                    "from",
                    "they",
                    "have",
                    "been",
                    "were",
                    "said",
                    "each",
                    "which",
                    "their",
                    "time",
                    "will",
                    "about",
                    "there",
                    "could",
                    "other",
                    "after",
                    "first",
                    "well",
                    "also",
                    "where",
                    "much",
                    "some",
                    "very",
                    "when",
                    "here",
                    "just",
                    "into",
                    "over",
                    "think",
                    "back",
                    "then",
                    "them",
                    "these",
                    "so",
                    "its",
                    "now",
                    "find",
                    "any",
                    "new",
                    "work",
                    "part",
                    "take",
                    "get",
                    "place",
                    "made",
                    "live",
                    "where",
                    "after",
                    "back",
                    "little",
                    "only",
                    "round",
                    "man",
                    "year",
                    "came",
                    "show",
                    "every",
                    "good",
                    "me",
                    "give",
                    "our",
                    "under",
                    "name",
                    "very",
                    "through",
                    "just",
                    "form",
                    "sentence",
                    "great",
                    "think",
                    "say",
                    "help",
                    "low",
                    "line",
                    "differ",
                    "turn",
                    "cause",
                    "much",
                    "mean",
                    "before",
                    "move",
                    "right",
                    "boy",
                    "old",
                    "too",
                    "same",
                    "she",
                    "all",
                    "there",
                    "when",
                    "up",
                    "use",
                    "word",
                    "how",
                    "said",
                    "an",
                    "each",
                    "which",
                    "she",
                    "do",
                    "how",
                    "their",
                    "if",
                    "will",
                    "up",
                    "other",
                    "about",
                    "out",
                    "many",
                    "then",
                    "them",
                    "can",
                    "only",
                    "other",
                    "new",
                    "some",
                    "what",
                    "time",
                    "very",
                    "when",
                    "much",
                    "then",
                    "no",
                    "way",
                    "could",
                    "people",
                    "my",
                    "than",
                    "first",
                    "water",
                    "been",
                    "call",
                    "who",
                    "oil",
                    "sit",
                    "now",
                    "find",
                    "long",
                    "down",
                    "day",
                    "did",
                    "get",
                    "come",
                    "made",
                    "may",
                    "part",
                ]
            ]

            matching_terms.extend(meaningful_words[:3])  # Limit to top 3

            # Remove duplicates and limit
            matching_terms = list(set(matching_terms))[:5]

            if matching_terms:
                if len(matching_terms) == 1:
                    reasoning = f"Matched based on: '{matching_terms[0]}'"
                elif len(matching_terms) == 2:
                    reasoning = f"Matched based on: '{matching_terms[0]}' and '{matching_terms[1]}'"
                else:
                    reasoning = f"Matched based on: '{', '.join(matching_terms[:-1])}', and '{matching_terms[-1]}'"
            else:
                # More specific fallback based on content analysis
                if (
                    "consultation" in query_lower
                    and "consultation" in description_lower
                ):
                    reasoning = "Matched based on consultation-related content"
                elif (
                    "examination" in query_lower and "examination" in description_lower
                ):
                    reasoning = "Matched based on examination-related content"
                elif "surgery" in query_lower and "surgery" in description_lower:
                    reasoning = "Matched based on surgical procedure content"
                elif (
                    "general practitioner" in query_lower
                    and "general practitioner" in description_lower
                ):
                    reasoning = "Matched based on general practitioner services"
                else:
                    # Analyze the type of content
                    if "professional attendance" in description_lower:
                        reasoning = "Matched based on professional attendance services"
                    elif "procedure" in description_lower:
                        reasoning = "Matched based on medical procedure content"
                    elif "treatment" in description_lower:
                        reasoning = "Matched based on treatment-related services"
                    else:
                        reasoning = "Matched based on medical service content"

            return reasoning

        except Exception as e:
            logger.error(f"Error generating meaningful reasoning: {e}")
            return f"Matched based on semantic similarity to your query"
