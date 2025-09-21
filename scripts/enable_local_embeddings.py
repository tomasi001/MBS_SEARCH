#!/usr/bin/env python3
"""
Script to enable local embeddings and test the MBS AI Assistant.

This script helps resolve Gemini API quota issues by switching to local embeddings.
"""

import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def enable_local_embeddings():
    """Enable local embeddings in the .env file."""
    env_file = ".env"

    # Read current .env file
    env_content = ""
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            env_content = f.read()

    # Add local embeddings configuration
    if "USE_LOCAL_EMBEDDINGS" not in env_content:
        env_content += "\n# Local Embeddings Configuration\n"
        env_content += "USE_LOCAL_EMBEDDINGS=true\n"
        env_content += "LOCAL_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2\n"

        with open(env_file, "w") as f:
            f.write(env_content)

        print("✅ Local embeddings enabled in .env file")
    else:
        print("ℹ️  Local embeddings already configured")


def test_system():
    """Test the system with local embeddings."""
    try:
        from config import settings
        from services.vector_service import VectorService
        from services.nlp_service import NLPService

        print("🔄 Testing system with local embeddings...")

        # Initialize services
        vector_service = VectorService()
        nlp_service = NLPService()

        # Test a simple query
        query = "general practitioner consultation"
        print(f"🔍 Testing query: '{query}'")

        result = nlp_service.process_natural_language_query(query)

        print(f"✅ Query processed successfully!")
        print(f"📊 Found {len(result.get('suggested_codes', []))} suggested codes")
        print(
            f"❓ Generated {len(result.get('follow_up_questions', []))} follow-up questions"
        )
        print(f"⏱️  Processing time: {result.get('processing_time_ms', 0):.1f}ms")

        if result.get("suggested_codes"):
            print(f"🎯 Suggested codes: {', '.join(result['suggested_codes'][:3])}...")

        return True

    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


def main():
    """Main function."""
    print("🚀 MBS AI Assistant - Local Embeddings Setup")
    print("=" * 50)

    # Enable local embeddings
    enable_local_embeddings()

    # Test the system
    if test_system():
        print("\n🎉 System is working correctly with local embeddings!")
        print("💡 You can now use the AI search without hitting Gemini API limits.")
    else:
        print("\n⚠️  System test failed. Check the logs for details.")
        print(
            "💡 You may need to install sentence-transformers: poetry add sentence-transformers"
        )


if __name__ == "__main__":
    main()
