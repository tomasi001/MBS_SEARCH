# Lean Deployment Guide - Ultra-Optimized for Free Tier

## Overview

This guide uses Render's **Root Directory** and **Build Filters** to deploy only the essential files each server needs, reducing repository size by ~70% per server.

## Architecture Benefits

- **Vector Server**: Only ~5MB of files (vs 50MB+ full repo)
- **AI Server**: Only ~3MB of files (vs 50MB+ full repo)
- **Frontend Server**: Only ~15MB of files (vs 50MB+ full repo)
- **Faster builds**: Less files to clone and process
- **Lower memory usage**: Minimal file system footprint
- **Faster deployments**: Reduced transfer times

## Deployment Strategy

### 🟢 Vector Server (Deploy First)

**Service Name**: `mbs-vector-server`

**Render Configuration**:

- **Root Directory**: `production/`
- **Build Command**: `cp pyproject_vector.toml pyproject.toml && poetry install --only=main`
- **Start Command**: `poetry run python vector_server.py`
- **Health Check Path**: `/health`

**Build Filters**:

- **Included Paths**:
  - `vector_server.py`
  - `pyproject_vector.toml`
  - `../config.py`
- **Ignored Paths**: `*` (everything else)

**Environment Variables**:

- `USE_LOCAL_EMBEDDINGS=true`
- `LOCAL_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2`
- `CHROMA_PERSIST_DIRECTORY=./chroma_db`
- `DEBUG=false`

**Files Deployed**: ~5MB

- Vector server code
- Vector dependencies
- Configuration only

---

### 🟡 AI Server (Deploy Second)

**Service Name**: `mbs-ai-server`

**Render Configuration**:

- **Root Directory**: `production/`
- **Build Command**: `cp pyproject_ai.toml pyproject.toml && poetry install --only=main`
- **Start Command**: `poetry run python ai_server.py`
- **Health Check Path**: `/health`

**Build Filters**:

- **Included Paths**:
  - `ai_server.py`
  - `pyproject_ai.toml`
  - `../config.py`
  - `../services/gemini_service.py`
- **Ignored Paths**: `*` (everything else)

**Environment Variables**:

- `GEMINI_API_KEY=your_gemini_api_key`
- `VECTOR_SERVER_URL=https://mbs-vector-server.onrender.com`
- `FRONTEND_SERVER_URL=https://mbs-frontend-server.onrender.com`
- `DEBUG=false`

**Files Deployed**: ~3MB

- AI server code
- Gemini service only
- AI dependencies
- Configuration only

---

### 🔵 Frontend Server (Deploy Last)

**Service Name**: `mbs-frontend-server`

**Render Configuration**:

- **Root Directory**: `production/`
- **Build Command**: `cp pyproject_frontend.toml pyproject.toml && poetry install --only=main`
- **Start Command**: `poetry run python frontend_server.py`
- **Health Check Path**: `/health`

**Build Filters**:

- **Included Paths**:
  - `frontend_server.py`
  - `pyproject_frontend.toml`
  - `../config.py`
  - `../templates/`
  - `../src/`
  - `../mbs.db`
- **Ignored Paths**: `*` (everything else)

**Environment Variables**:

- `AI_SERVER_URL=https://mbs-ai-server.onrender.com`
- `VECTOR_SERVER_URL=https://mbs-vector-server.onrender.com`
- `MBS_DB_PATH=mbs.db`
- `DEBUG=false`

**Files Deployed**: ~15MB

- Frontend server code
- HTML templates
- Database module
- SQLite database
- Frontend dependencies
- Configuration only

## Manual Render Configuration

Since `render.yaml` files aren't automatically applied, configure each service manually:

### Vector Server Setup

1. Create new Render web service
2. Connect to GitHub repository
3. Set **Root Directory** to `production/`
4. Set **Build Command** to `cp pyproject_vector.toml pyproject.toml && poetry install --only=main`
5. Set **Start Command** to `poetry run python vector_server.py`
6. Set **Health Check Path** to `/health`
7. Configure **Build Filters**:
   - **Included Paths**: `vector_server.py`, `pyproject_vector.toml`, `../config.py`
   - **Ignored Paths**: `*`
8. Add environment variables

### AI Server Setup

1. Create new Render web service
2. Connect to GitHub repository
3. Set **Root Directory** to `production/`
4. Set **Build Command** to `cp pyproject_ai.toml pyproject.toml && poetry install --only=main`
5. Set **Start Command** to `poetry run python ai_server.py`
6. Set **Health Check Path** to `/health`
7. Configure **Build Filters**:
   - **Included Paths**: `ai_server.py`, `pyproject_ai.toml`, `../config.py`, `../services/gemini_service.py`
   - **Ignored Paths**: `*`
8. Add environment variables

### Frontend Server Setup

1. Create new Render web service
2. Connect to GitHub repository
3. Set **Root Directory** to `production/`
4. Set **Build Command** to `cp pyproject_frontend.toml pyproject.toml && poetry install --only=main`
5. Set **Start Command** to `poetry run python frontend_server.py`
6. Set **Health Check Path** to `/health`
7. Configure **Build Filters**:
   - **Included Paths**: `frontend_server.py`, `pyproject_frontend.toml`, `../config.py`, `../templates/`, `../src/`, `../mbs.db`
   - **Ignored Paths**: `*`
8. Add environment variables

## File Structure After Deployment

### Vector Server (Root: production/)

```
production/
├── vector_server.py
├── pyproject_vector.toml
└── ../config.py
```

### AI Server (Root: production/)

```
production/
├── ai_server.py
├── pyproject_ai.toml
├── ../config.py
└── ../services/gemini_service.py
```

### Frontend Server (Root: production/)

```
production/
├── frontend_server.py
├── pyproject_frontend.toml
├── ../config.py
├── ../templates/enhanced_chat_ui.py
├── ../src/mbs_clarity/
└── ../mbs.db
```

## Benefits

1. **Ultra-Lean Deployments**: 70% smaller file transfers
2. **Faster Builds**: Minimal files to process
3. **Lower Memory Usage**: Reduced file system footprint
4. **Faster Deployments**: Quicker clone and build times
5. **Free Tier Optimized**: Each server uses minimal resources
6. **Clean Separation**: No unnecessary files per server
7. **Poetry Consistency**: Maintains Poetry dependency management
8. **Render Native**: Uses Render's built-in optimization features

## Testing

After deployment, test each server:

```bash
# Test Vector Server
curl https://mbs-vector-server.onrender.com/health

# Test AI Server
curl https://mbs-ai-server.onrender.com/health

# Test Frontend Server
curl https://mbs-frontend-server.onrender.com/health

# Test Inter-Server Communication
curl https://mbs-frontend-server.onrender.com/api/ai/status

# Test MBS Code Lookup
curl "https://mbs-frontend-server.onrender.com/api/items?codes=23"
```

This approach gives you the **leanest possible deployment** while maintaining full functionality! 🚀
