"""
Configuration settings for MBS AI Assistant MVP using Gemini.
"""

import os
from typing import Optional
from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings for MBS AI Assistant."""

    # Gemini Configuration
    GEMINI_API_KEY: str = Field(..., description="Google Gemini API key")
    GEMINI_MODEL_NAME: str = Field("gemini-2.5-flash", description="Gemini model name")
    GEMINI_EMBEDDING_MODEL: str = Field(
        "models/embedding-001", description="Gemini embedding model"
    )

    # Fallback Configuration
    USE_LOCAL_EMBEDDINGS: bool = Field(
        False,
        description="Use local sentence-transformers instead of Gemini embeddings",
    )
    LOCAL_EMBEDDING_MODEL: str = Field(
        "sentence-transformers/all-MiniLM-L6-v2", description="Local embedding model"
    )

    # ChromaDB Configuration
    CHROMA_PERSIST_DIRECTORY: str = Field(
        "./chroma_db", description="ChromaDB persistence directory"
    )

    # Application Configuration
    ENVIRONMENT: str = Field(
        "development", description="Environment (development/production)"
    )
    DEBUG: bool = Field(True, description="Debug mode")

    # API Configuration
    API_HOST: str = Field("127.0.0.1", description="API host")
    API_PORT: int = Field(8000, description="API port")

    # Database Configuration
    MBS_DB_PATH: str = Field("mbs.db", description="Path to MBS SQLite database")

    @field_validator("API_PORT", mode="before")
    @classmethod
    def validate_api_port(cls, v):
        """Handle PORT environment variable from Render."""
        if isinstance(v, str) and v.startswith("$"):
            # Handle environment variable references like $PORT
            port_value = os.getenv(v[1:], "8000")
            return int(port_value)
        return int(v)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()
