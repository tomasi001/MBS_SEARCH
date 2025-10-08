#!/bin/bash
# AI Server Deployment Script
# This script sets up a clean environment with only AI server dependencies

echo "Setting up AI Server environment..."

# Create a temporary pyproject.toml with only AI dependencies
cat > pyproject_ai_temp.toml << EOF
[tool.poetry]
name = "mbs-clarity-ai"
version = "0.1.0"
description = "MBS Clarity AI Server - Gemini API and NLP processing"
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
# HTTP client for proxying
httpx = "^0.27.2"
# AI/ML dependencies - Gemini only
google-generativeai = "^0.8.5"
# Configuration
pydantic-settings = "^2.10.1"
python-multipart = "^0.0.20"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
EOF

# Install dependencies using the temporary pyproject.toml
poetry install --no-root

# Start the AI server
poetry run python production/ai_server.py


