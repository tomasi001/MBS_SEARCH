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

   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python start.py`

5. **Environment Variables**:

   - `GEMINI_API_KEY`: Your Gemini API key
   - `USE_LOCAL_EMBEDDINGS`: `true`
   - `RENDER`: `true`

6. **Deploy**: Click "Create Web Service"

## Files Created:

- `requirements.txt` - Python dependencies
- `render.yaml` - Render configuration
- `start.py` - Production startup script
- `.gitignore` - Excludes unnecessary files

## Notes:

- Uses local embeddings (no API costs)
- Auto-populates vector database on first run
- Optimized for Render free tier
- SQLite + ChromaDB (no external databases needed)
