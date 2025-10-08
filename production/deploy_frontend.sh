#!/bin/bash
# Frontend Server Deployment Script
# This script sets up a clean environment with only frontend server dependencies

echo "Setting up Frontend Server environment..."

# Create a temporary pyproject.toml with only frontend dependencies
cat > pyproject_frontend_temp.toml << EOF
[tool.poetry]
name = "mbs-clarity-frontend"
version = "0.1.0"
description = "MBS Clarity Frontend Server - Web UI and API orchestration"
authors = ["Thomas Shields <you@example.com>"]
readme = "README.md"
packages = [
  { include = "mbs_clarity", from = "src" }
]

[tool.poetry.dependencies]
python = ">=3.11,<3.13"
# Web framework and serving
fastapi = "^0.117.1"
uvicorn = {extras = ["standard"], version = "^0.36.0"}
gunicorn = "^23.0.0"
# HTTP client for proxying
httpx = "^0.27.2"
# Data processing
pandas = "^2.3.2"
lxml = "^6.0.1"
# Configuration
pydantic-settings = "^2.10.1"
python-multipart = "^0.0.20"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
EOF

# Install dependencies using the temporary pyproject.toml
poetry install --no-root

# Start the frontend server
poetry run python production/frontend_server.py
