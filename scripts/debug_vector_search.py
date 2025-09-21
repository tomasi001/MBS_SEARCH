#!/usr/bin/env python3
"""
Debug script to test vector search functionality.
"""

import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_vector_search():
    """Test vector search functionality."""
    try:
        from config import settings
        from services.vector_service import VectorService

        print("🔄 Testing vector search...")

        # Initialize vector service
        vector_service = VectorService()

        # Test a simple search
        query = "general practitioner consultation"
        print(f"🔍 Testing query: '{query}'")

        results = vector_service.search(query, max_results=5)

        print(f"✅ Search completed!")
        print(f"📊 Found {len(results)} results")

        if results:
            print("🎯 Top results:")
            for i, result in enumerate(results[:3]):
                print(f"  {i+1}. {result.get('content', 'No content')[:100]}...")
                print(f"     Similarity: {result.get('similarity_score', 0):.3f}")
        else:
            print("❌ No results found")

        # Check collection stats
        stats = vector_service.get_collection_stats()
        print(f"📈 Collection stats: {stats}")

        return True

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Main function."""
    print("🔍 MBS AI Assistant - Vector Search Debug")
    print("=" * 50)

    if test_vector_search():
        print("\n🎉 Vector search test completed!")
    else:
        print("\n⚠️  Vector search test failed.")


if __name__ == "__main__":
    main()
