"""
Natural language search service for MBS Clarity AI assistant.

This module handles natural language queries from doctors and converts them
into relevant MBS code suggestions using AI-powered search and analysis.
"""

import logging
import time
from typing import Any, Dict, List, Optional, Tuple

from mbs_clarity.ai_models import (
    AIConfig,
    ChatContext,
    CodeSuggestion,
    NaturalLanguageQuery,
    SearchRequest,
    SearchResponse,
    SearchResult,
    SearchType,
)
from mbs_clarity.db import fetch_item_aggregate
from mbs_clarity.openai_service import OpenAIService
from mbs_clarity.vector_db import VectorDatabaseService

logger = logging.getLogger(__name__)


class NaturalLanguageSearchService:
    """Service for natural language MBS code search."""

    def __init__(self, config: AIConfig):
        """Initialize the natural language search service."""
        self.config = config
        self.vector_db = VectorDatabaseService(config)
        self.openai_service = OpenAIService(config)
        self._initialize_services()

    def _initialize_services(self) -> None:
        """Initialize vector database and OpenAI services."""
        try:
            # Ensure vector database is populated
            self.vector_db.populate_vector_db()
            logger.info("Natural language search service initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize natural language search service: {e}")
            raise

    def process_natural_language_query(
        self, query: str, context: Optional[ChatContext] = None
    ) -> NaturalLanguageQuery:
        """Process a natural language query from a doctor."""
        logger.info(f"Processing natural language query: '{query}'")

        start_time = time.time()

        try:
            # Step 1: Analyze the query using AI (with fallback)
            try:
                analysis = self.openai_service.analyze_medical_query(query)
            except RuntimeError:
                # Fallback analysis when OpenAI is not available
                analysis = self._basic_query_analysis(query)

            # Step 2: Perform semantic search
            search_results = self._perform_semantic_search(query, analysis)

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

            return NaturalLanguageQuery(
                query=query,
                context=context,
                follow_up_questions=follow_up_questions,
                suggested_codes=suggested_codes,
            )

        except Exception as e:
            logger.error(f"Error processing natural language query: {e}")
            return NaturalLanguageQuery(
                query=query, context=context, follow_up_questions=[], suggested_codes=[]
            )

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

        # Extract location
        if "consulting rooms" in query_lower:
            analysis["location"] = "consulting rooms"
        elif "hospital" in query_lower:
            analysis["location"] = "hospital"

        return analysis

    def _perform_semantic_search(
        self, query: str, analysis: Dict[str, Any]
    ) -> List[SearchResult]:
        """Perform semantic search using the vector database."""
        try:
            # Use hybrid search for better results
            search_results = self.vector_db.search(
                query=query,
                search_type=SearchType.HYBRID,
                max_results=self.config.max_search_results,
            )

            # If we have analysis results, try additional targeted searches
            if analysis and "body_part" in analysis:
                body_part = analysis["body_part"]
                if body_part:
                    # Search for body part specific results
                    body_part_results = self.vector_db.search(
                        query=f"{body_part} {analysis.get('procedure_type', '')}",
                        search_type=SearchType.SEMANTIC,
                        max_results=5,
                    )

                    # Merge results, avoiding duplicates
                    existing_items = {result.item_num for result in search_results}
                    for result in body_part_results:
                        if result.item_num not in existing_items:
                            search_results.append(result)

            logger.info(f"Found {len(search_results)} semantic search results")
            return search_results

        except Exception as e:
            logger.error(f"Error performing semantic search: {e}")
            return []

    def _generate_code_suggestions(
        self, query: str, search_results: List[SearchResult], analysis: Dict[str, Any]
    ) -> List[str]:
        """Generate MBS code suggestions based on search results."""
        try:
            if not search_results:
                return []

            # Extract item numbers from search results
            suggested_items = []
            for result in search_results[:10]:  # Limit to top 10
                suggested_items.append(result.item_num)

            # Use AI to refine suggestions
            if self.openai_service.client:
                ai_suggestions = self.openai_service.suggest_related_codes(
                    query=query,
                    current_codes=suggested_items,
                    search_results=[
                        {"item_num": r.item_num, "content": r.content, "score": r.score}
                        for r in search_results
                    ],
                )

                # Combine AI suggestions with search results
                all_suggestions = list(set(suggested_items + ai_suggestions))
            else:
                all_suggestions = suggested_items

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
        context: Optional[ChatContext],
    ) -> List[str]:
        """Generate follow-up questions to narrow down code selection."""
        try:
            if not suggested_codes:
                return []

            # Use OpenAI to generate follow-up questions
            if self.openai_service.client:
                questions = self.openai_service.generate_follow_up_questions(
                    query=query, suggested_codes=suggested_codes, context=analysis
                )
            else:
                # Fallback to basic questions
                questions = self._generate_basic_follow_up_questions(analysis)

            logger.info(f"Generated {len(questions)} follow-up questions")
            return questions

        except Exception as e:
            logger.error(f"Error generating follow-up questions: {e}")
            return []

    def _generate_basic_follow_up_questions(
        self, analysis: Dict[str, Any]
    ) -> List[str]:
        """Generate basic follow-up questions when AI is not available."""
        questions = []

        if not analysis.get("body_part"):
            questions.append("Which body part or organ was involved?")

        if not analysis.get("procedure_type"):
            questions.append("What type of procedure was performed?")

        if not analysis.get("specific_details"):
            questions.append(
                "Were there any specific details (left/right, duration, complexity)?"
            )

        if not analysis.get("patient_characteristics"):
            questions.append(
                "What were the patient's characteristics (age, condition)?"
            )

        if not analysis.get("provider_type"):
            questions.append("What type of provider performed the procedure?")

        return questions[:5]  # Limit to 5 questions

    def get_detailed_code_suggestions(
        self, suggested_codes: List[str], query: str
    ) -> List[CodeSuggestion]:
        """Get detailed suggestions for MBS codes."""
        suggestions = []

        for item_num in suggested_codes:
            try:
                # Get full item details
                item_data = fetch_item_aggregate(item_num)
                if not item_data:
                    continue

                # Calculate confidence score based on relevance
                confidence = self._calculate_confidence_score(item_data, query)

                # Generate reasoning
                reasoning = self._generate_reasoning(item_data, query)

                # Extract requirements and exclusions
                requirements = self._extract_requirements(item_data)
                exclusions = self._extract_exclusions(item_data)

                suggestions.append(
                    CodeSuggestion(
                        item_num=item_num,
                        confidence=confidence,
                        reasoning=reasoning,
                        requirements=requirements,
                        exclusions=exclusions,
                        follow_up_questions=[],
                    )
                )

            except Exception as e:
                logger.error(f"Error processing code suggestion {item_num}: {e}")
                continue

        # Sort by confidence score
        suggestions.sort(key=lambda x: x.confidence, reverse=True)

        logger.info(f"Generated {len(suggestions)} detailed code suggestions")
        return suggestions

    def _calculate_confidence_score(
        self, item_data: Dict[str, Any], query: str
    ) -> float:
        """Calculate confidence score for a code suggestion."""
        try:
            score = 0.5  # Base score

            description = item_data.get("description", "").lower()
            query_lower = query.lower()

            # Check for keyword matches
            query_words = query_lower.split()
            description_words = description.split()

            matches = sum(1 for word in query_words if word in description_words)
            if query_words:
                keyword_score = matches / len(query_words)
                score += keyword_score * 0.3

            # Check for constraint matches
            constraints = item_data.get("constraints", [])
            constraint_matches = 0
            for constraint in constraints:
                constraint_text = constraint.get("value", "").lower()
                if any(word in constraint_text for word in query_words):
                    constraint_matches += 1

            if constraints:
                constraint_score = constraint_matches / len(constraints)
                score += constraint_score * 0.2

            return min(score, 1.0)  # Cap at 1.0

        except Exception as e:
            logger.error(f"Error calculating confidence score: {e}")
            return 0.5

    def _generate_reasoning(self, item_data: Dict[str, Any], query: str) -> str:
        """Generate reasoning for why this code was suggested."""
        try:
            description = item_data.get("description", "")
            constraints = item_data.get("constraints", [])

            reasoning_parts = []

            # Add description match
            if description:
                reasoning_parts.append(f"Description matches: {description[:100]}...")

            # Add relevant constraints
            relevant_constraints = []
            query_lower = query.lower()
            for constraint in constraints:
                constraint_text = constraint.get("value", "").lower()
                if any(word in constraint_text for word in query_lower.split()):
                    relevant_constraints.append(
                        f"{constraint.get('constraint_type', '')}: {constraint.get('value', '')}"
                    )

            if relevant_constraints:
                reasoning_parts.append(
                    f"Relevant constraints: {', '.join(relevant_constraints[:3])}"
                )

            return (
                " | ".join(reasoning_parts)
                if reasoning_parts
                else "General match based on search results"
            )

        except Exception as e:
            logger.error(f"Error generating reasoning: {e}")
            return "Match based on search results"

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

    def search_with_filters(self, request: SearchRequest) -> SearchResponse:
        """Perform a search with filters and return structured response."""
        logger.info(f"Searching with filters: {request.filters}")

        start_time = time.time()

        try:
            # Perform the search
            results = self.vector_db.search(
                query=request.query,
                search_type=request.search_type,
                max_results=request.max_results,
                filters=request.filters,
            )

            # Convert to SearchResult objects if needed
            search_results = []
            for result in results:
                if isinstance(result, SearchResult):
                    search_results.append(result)
                else:
                    # Convert dict to SearchResult
                    search_results.append(
                        SearchResult(
                            item_num=result.get("item_num", ""),
                            score=result.get("score", 0.0),
                            content=result.get("content", ""),
                            chunk_type=result.get("chunk_type", ""),
                            metadata=result.get("metadata", {}),
                        )
                    )

            search_time = (time.time() - start_time) * 1000

            return SearchResponse(
                results=search_results,
                total_found=len(search_results),
                search_time_ms=search_time,
                suggestions=[],
                follow_up_questions=[],
            )

        except Exception as e:
            logger.error(f"Error in filtered search: {e}")
            return SearchResponse(
                results=[],
                total_found=0,
                search_time_ms=0.0,
                suggestions=[],
                follow_up_questions=[],
            )
