# Render Deployment Guide

## Quick Steps:

1. **Push to GitHub**: Commit and push all files to your GitHub repository

2. **Go to Render.com**: Sign up/login with GitHub

3. **Create Web Service**:

   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Name: `mbs-ai-assistant`
   - Environment: `Python`
   - Plan: `Free`

4. **Configure**:

   - Build Command: `poetry install --only=main`
   - Start Command: `poetry run python api/main.py`

5. **Environment Variables**:

   - `GEMINI_API_KEY`: Your Gemini API key
   - `USE_LOCAL_EMBEDDINGS`: `true`

6. **Deploy**: Click "Create Web Service"

## Files Created:

- `requirements.txt` - Python dependencies (backup)
- `render.yaml` - Render configuration
- `pyproject.toml` - Poetry configuration (primary)
- `.gitignore` - Excludes unnecessary files

## Notes:

- Uses Poetry for dependency management (Render's default)
- Auto-populates vector database on first run
- Optimized for Render free tier
- SQLite + ChromaDB (no external databases needed)
- Simplified startup (no custom scripts needed)
