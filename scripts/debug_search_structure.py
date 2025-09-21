#!/usr/bin/env python3
"""
Debug script to examine vector search results structure.
"""

import os
import sys
import json

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def debug_search_results():
    """Debug the structure of search results."""
    try:
        from config import settings
        from services.vector_service import VectorService

        print("🔄 Debugging search results structure...")

        # Initialize vector service
        vector_service = VectorService()

        # Test a simple search
        query = "general practitioner consultation"
        print(f"🔍 Testing query: '{query}'")

        results = vector_service.search(query, max_results=3)

        print(f"✅ Search completed!")
        print(f"📊 Found {len(results)} results")

        if results:
            print("\n🎯 First result structure:")
            first_result = results[0]
            print(f"Keys: {list(first_result.keys())}")
            print(f"Metadata: {first_result.get('metadata', {})}")
            print(f"Content: {first_result.get('content', '')[:200]}...")

            print("\n🔍 Looking for item_num in metadata:")
            metadata = first_result.get("metadata", {})
            if "item_num" in metadata:
                print(f"✅ Found item_num: {metadata['item_num']}")
            else:
                print("❌ No item_num found in metadata")
                print(f"Available metadata keys: {list(metadata.keys())}")

        return True

    except Exception as e:
        print(f"❌ Debug failed: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Main function."""
    print("🔍 MBS AI Assistant - Search Results Debug")
    print("=" * 50)

    if debug_search_results():
        print("\n🎉 Debug completed!")
    else:
        print("\n⚠️  Debug failed.")


if __name__ == "__main__":
    main()
