# MBS AI Assistant - Production Deployment Guide

This guide explains how to deploy the MBS AI Assistant across three separate servers to work within free tier constraints.

## Architecture Overview

The system is split into three microservices:

1. **Frontend Server** - Web UI, API orchestration, MBS code lookup
2. **AI Server** - Gemini API, natural language processing
3. **Vector Server** - ChromaDB, sentence-transformers, semantic search

## Deployment Steps

### Step 1: Deploy Vector Server (Heaviest Dependencies)

1. Create a new Render web service
2. Connect to your GitHub repository
3. Use these settings:

   - **Build Command**: `poetry install --only=main`
   - **Start Command**: `poetry run python production/vector_server.py`
   - **Health Check Path**: `/health`
   - **Environment Variables**:
     - `USE_LOCAL_EMBEDDINGS=true`
     - `LOCAL_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2`
     - `CHROMA_PERSIST_DIRECTORY=./chroma_db`
     - `DEBUG=false`

4. Wait for deployment to complete and note the URL (e.g., `https://mbs-vector-server.onrender.com`)

### Step 2: Deploy AI Server

1. Create a new Render web service
2. Connect to your GitHub repository
3. Use these settings:

   - **Build Command**: `poetry install --only=main`
   - **Start Command**: `poetry run python production/ai_server.py`
   - **Health Check Path**: `/health`
   - **Environment Variables**:
     - `GEMINI_API_KEY=your_gemini_api_key`
     - `VECTOR_SERVER_URL=https://mbs-vector-server.onrender.com`
     - `FRONTEND_SERVER_URL=https://mbs-frontend-server.onrender.com`
     - `DEBUG=false`

4. Wait for deployment to complete and note the URL (e.g., `https://mbs-ai-server.onrender.com`)

### Step 3: Deploy Frontend Server

1. Create a new Render web service
2. Connect to your GitHub repository
3. Use these settings:

   - **Build Command**: `poetry install --only=main`
   - **Start Command**: `poetry run python production/frontend_server.py`
   - **Health Check Path**: `/health`
   - **Environment Variables**:
     - `AI_SERVER_URL=https://mbs-ai-server.onrender.com`
     - `VECTOR_SERVER_URL=https://mbs-vector-server.onrender.com`
     - `MBS_DB_PATH=mbs.db`
     - `DEBUG=false`

4. Wait for deployment to complete and note the URL (e.g., `https://mbs-frontend-server.onrender.com`)

## Testing the Deployment

1. **Check Frontend Server**: Visit `https://mbs-frontend-server.onrender.com`
2. **Check Health Status**: Visit `https://mbs-frontend-server.onrender.com/api/ai/status`
3. **Test MBS Code Search**: Try searching for codes like 23, 36, 104
4. **Test AI Features**: Try natural language queries

## Service Communication

The servers communicate via HTTP:

- **Frontend → AI Server**: Natural language queries, conversational AI
- **Frontend → Vector Server**: Semantic search requests
- **AI Server → Vector Server**: Vector search for AI processing

## Environment Variables

### Frontend Server

- `AI_SERVER_URL` - URL of the AI server
- `VECTOR_SERVER_URL` - URL of the vector server
- `MBS_DB_PATH` - Path to SQLite database

### AI Server

- `GEMINI_API_KEY` - Google Gemini API key
- `VECTOR_SERVER_URL` - URL of the vector server
- `FRONTEND_SERVER_URL` - URL of the frontend server

### Vector Server

- `USE_LOCAL_EMBEDDINGS` - Use local sentence-transformers
- `LOCAL_EMBEDDING_MODEL` - Model name for embeddings
- `CHROMA_PERSIST_DIRECTORY` - ChromaDB storage directory

## Troubleshooting

### Common Issues

1. **Service Unavailable Errors**: Check that all three servers are running and URLs are correct
2. **Vector Search Fails**: Ensure ChromaDB is properly initialized on the vector server
3. **AI Processing Fails**: Check Gemini API key and network connectivity
4. **MBS Code Lookup Fails**: Ensure SQLite database is available on frontend server

### Health Checks

Each server provides a `/health` endpoint:

- Frontend: `https://mbs-frontend-server.onrender.com/health`
- AI: `https://mbs-ai-server.onrender.com/health`
- Vector: `https://mbs-vector-server.onrender.com/health`

### Logs

Check Render logs for each service to diagnose issues:

- Look for startup errors
- Check service communication failures
- Monitor memory usage (free tier has limits)

## Benefits of This Architecture

1. **Free Tier Compatible**: Each service fits within free tier limits
2. **Scalable**: Can upgrade individual services as needed
3. **Fault Tolerant**: If one service fails, others continue working
4. **Maintainable**: Clear separation of concerns
5. **Cost Effective**: Only pay for what you need

## Future Enhancements

- Add load balancing for high traffic
- Implement service discovery
- Add monitoring and alerting
- Consider containerization with Docker
- Add caching layers for better performance
