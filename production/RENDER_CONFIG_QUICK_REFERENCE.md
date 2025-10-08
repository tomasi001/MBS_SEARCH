# Render Configuration Quick Reference

## Manual Configuration for Each Server

### 🟢 Vector Server (Deploy First)

**Service Name**: `mbs-vector-server`

**Build Command**:

```bash
poetry install --only=main --no-root
```

**Start Command**:

```bash
poetry run python production/vector_server.py
```

**Health Check Path**: `/health`

**Environment Variables**:

- `USE_LOCAL_EMBEDDINGS=true`
- `LOCAL_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2`
- `CHROMA_PERSIST_DIRECTORY=./chroma_db`
- `DEBUG=false`

**Dependencies**: ~500MB (ChromaDB, sentence-transformers, FastAPI)

---

### 🟡 AI Server (Deploy Second)

**Service Name**: `mbs-ai-server`

**Build Command**:

```bash
poetry install --only=main --no-root
```

**Start Command**:

```bash
poetry run python production/ai_server.py
```

**Health Check Path**: `/health`

**Environment Variables**:

- `GEMINI_API_KEY=your_gemini_api_key`
- `VECTOR_SERVER_URL=https://mbs-vector-server.onrender.com`
- `FRONTEND_SERVER_URL=https://mbs-frontend-server.onrender.com`
- `DEBUG=false`

**Dependencies**: ~50MB (Google Generative AI, FastAPI, httpx)

---

### 🔵 Frontend Server (Deploy Last)

**Service Name**: `mbs-frontend-server`

**Build Command**:

```bash
poetry install --only=main --no-root
```

**Start Command**:

```bash
poetry run python production/frontend_server.py
```

**Health Check Path**: `/health`

**Environment Variables**:

- `AI_SERVER_URL=https://mbs-ai-server.onrender.com`
- `VECTOR_SERVER_URL=https://mbs-vector-server.onrender.com`
- `MBS_DB_PATH=mbs.db`
- `DEBUG=false`

**Dependencies**: ~30MB (FastAPI, httpx, pandas, lxml)

---

## Deployment Order

1. **Vector Server** → Get URL → Update AI Server env vars
2. **AI Server** → Get URL → Update Frontend Server env vars
3. **Frontend Server** → Final URL for users

## Testing Commands

```bash
# Test each server health
curl https://mbs-vector-server.onrender.com/health
curl https://mbs-ai-server.onrender.com/health
curl https://mbs-frontend-server.onrender.com/health

# Test inter-server communication
curl https://mbs-frontend-server.onrender.com/api/ai/status

# Test MBS code lookup
curl "https://mbs-frontend-server.onrender.com/api/items?codes=23"

# Test AI processing
curl -X POST "https://mbs-frontend-server.onrender.com/api/ai/natural-language" \
  -H "Content-Type: application/json" \
  -d '{"query": "I need a consultation for chest pain"}'
```

## Benefits

- **90%+ reduction** in dependency downloads
- **Faster builds** on free tier
- **Lower memory usage** per server
- **Better resource allocation**
- **Easier debugging** and maintenance
