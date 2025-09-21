#!/usr/bin/env python3
"""
Script to reset and repopulate the vector database with local embeddings.

This resolves the embedding dimension mismatch issue.
"""

import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def reset_vector_database():
    """Reset the vector database to use local embeddings."""
    try:
        from config import settings
        from services.vector_service import VectorService

        print("🔄 Resetting vector database for local embeddings...")

        # Initialize vector service
        vector_service = VectorService()

        # Reset the collection
        print("🗑️  Clearing existing vector database...")
        vector_service.reset_collection()

        print("✅ Vector database reset successfully!")
        print("💡 The database is now ready for local embeddings (384 dimensions)")
        print("📝 You can now repopulate it using the populate script")

        return True

    except Exception as e:
        print(f"❌ Reset failed: {e}")
        return False


def main():
    """Main function."""
    print("🔄 MBS AI Assistant - Vector Database Reset")
    print("=" * 50)

    if reset_vector_database():
        print("\n🎉 Vector database reset complete!")
        print("💡 Next steps:")
        print("   1. Run: poetry run python scripts/populate_mbs_data.py")
        print("   2. The system will use local embeddings (no API limits)")
    else:
        print("\n⚠️  Reset failed. Check the logs for details.")


if __name__ == "__main__":
    main()
