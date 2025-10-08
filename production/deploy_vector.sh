#!/bin/bash
# Vector Server Deployment Script
# This script sets up a clean environment with only vector server dependencies

echo "Setting up Vector Server environment..."

# Create a temporary pyproject.toml with only vector dependencies
cat > pyproject_vector_temp.toml << EOF
[tool.poetry]
name = "mbs-clarity-vector"
version = "0.1.0"
description = "MBS Clarity Vector Server - ChromaDB and semantic search"
authors = ["Thomas Shields <you@example.com>"]
readme = "README.md"
packages = [
  { include = "mbs_clarity", from = "src" }
]

[tool.poetry.dependencies]
python = ">=3.11,<3.13"
# Web framework
fastapi = "^0.117.1"
uvicorn = {extras = ["standard"], version = "^0.36.0"}
gunicorn = "^23.0.0"
# Vector database and embeddings - HEAVY DEPENDENCIES
chromadb = "^1.1.0"
sentence-transformers = "^5.1.0"
# Configuration
pydantic-settings = "^2.10.1"
python-multipart = "^0.0.20"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
EOF

# Install dependencies using the temporary pyproject.toml
poetry install --no-root

# Start the vector server
poetry run python production/vector_server.py


