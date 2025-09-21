#!/usr/bin/env python3
"""
Debug script to test the entire NLP pipeline.
"""

import os
import sys
import json

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def debug_nlp_pipeline():
    """Debug the entire NLP pipeline."""
    try:
        from config import settings
        from services.nlp_service import NLPService

        print("🔄 Debugging NLP pipeline...")

        # Initialize NLP service
        nlp_service = NLPService()

        # Test query
        query = "general practitioner consultation"
        print(f"🔍 Testing query: '{query}'")

        # Step 1: Test analysis
        print("\n📊 Step 1: Testing query analysis...")
        analysis = nlp_service.gemini_service.analyze_medical_query(query)
        print(f"Analysis result: {analysis}")

        # Step 2: Test vector search
        print("\n🔍 Step 2: Testing vector search...")
        search_results = nlp_service._perform_vector_search(query, analysis)
        print(f"Found {len(search_results)} search results")

        if search_results:
            print("First result metadata:")
            print(json.dumps(search_results[0]["metadata"], indent=2))

        # Step 3: Test code suggestions
        print("\n💡 Step 3: Testing code suggestions...")
        suggested_codes = nlp_service._generate_code_suggestions(
            query, search_results, analysis
        )
        print(f"Generated {len(suggested_codes)} code suggestions: {suggested_codes}")

        # Step 4: Test follow-up questions
        print("\n❓ Step 4: Testing follow-up questions...")
        follow_up_questions = nlp_service._generate_follow_up_questions(
            query, suggested_codes, analysis, None
        )
        print(f"Generated {len(follow_up_questions)} follow-up questions")

        # Step 5: Test full pipeline
        print("\n🚀 Step 5: Testing full pipeline...")
        result = nlp_service.process_natural_language_query(query)
        print(f"Full pipeline result:")
        print(f"  Suggested codes: {len(result.get('suggested_codes', []))}")
        print(f"  Follow-up questions: {len(result.get('follow_up_questions', []))}")
        print(f"  Processing time: {result.get('processing_time_ms', 0):.1f}ms")

        return True

    except Exception as e:
        print(f"❌ Debug failed: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Main function."""
    print("🔍 MBS AI Assistant - NLP Pipeline Debug")
    print("=" * 50)

    if debug_nlp_pipeline():
        print("\n🎉 Debug completed!")
    else:
        print("\n⚠️  Debug failed.")


if __name__ == "__main__":
    main()
