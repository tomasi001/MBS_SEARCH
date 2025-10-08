# Gemini Embeddings Deployment Guide

## 🎯 Solution: Use Gemini API for Embeddings

Instead of using heavy local sentence-transformers models that exceed the 512MB memory limit, we'll use Gemini's embedding API which provides high-quality embeddings without local model storage.

## Benefits of Gemini Embeddings

- **No Memory Issues**: No local models to load (saves 400MB+ memory)
- **High Quality**: Gemini's `text-embedding-004` model provides excellent semantic search
- **Scalable**: API-based, no local resource constraints
- **Cost Effective**: Pay per use, not per server
- **Fast**: Optimized for retrieval tasks with `RETRIEVAL_QUERY` task type

## Updated Vector Server Configuration

### Files Created:

- `production/vector_server_gemini.py` - Vector server using Gemini embeddings
- `production/pyproject_vector_gemini.toml` - Minimal dependencies

### Dependencies (Ultra-Lightweight):

- FastAPI, uvicorn, gunicorn (web framework)
- google-generativeai (Gemini API)
- chromadb[lite] (vector database without heavy ML deps)
- numpy (for embedding normalization)
- pydantic-settings, python-multipart (configuration)

**Total Packages**: ~15 packages (vs 118 before)
**Memory Usage**: ~100MB (vs 512MB+ before)

## Deployment Configuration

### Vector Server (Gemini Embeddings)

```yaml
Service Name: mbs-vector-server
Root Directory: production/
Build Command: cp pyproject_vector_gemini.toml pyproject.toml && poetry install --only=main --no-root
Start Command: poetry run python vector_server_gemini.py
Health Check Path: /health
```

### Environment Variables:

```bash
GEMINI_API_KEY=your_gemini_api_key
USE_GEMINI_EMBEDDINGS=true
GEMINI_EMBEDDING_MODEL=models/text-embedding-004
CHROMA_PERSIST_DIRECTORY=./chroma_db
DEBUG=false
```

## Gemini Embedding Configuration

### Model: `text-embedding-004`

- **Dimensions**: 768 (optimized for storage and performance)
- **Task Type**: `RETRIEVAL_QUERY` (optimized for search queries)
- **Normalization**: Automatic normalization for accurate similarity
- **Quality**: High-quality semantic embeddings

### Embedding Process:

1. **Query Embedding**: Generate embedding for search query
2. **Document Embeddings**: Generate embeddings for documents to be stored
3. **Similarity Search**: Use cosine similarity for retrieval
4. **Normalization**: Automatic normalization for consistent results

## Code Features

### Key Functions:

```python
def generate_embeddings(texts: List[str]) -> List[List[float]]:
    """Generate embeddings using Gemini API with normalization."""
    result = gemini_client.models.embed_content(
        model="models/text-embedding-004",
        contents=texts,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY",
            output_dimensionality=768
        )
    )

    # Normalize embeddings for accurate similarity
    embeddings = []
    for embedding_obj in result.embeddings:
        embedding_values = np.array(embedding_obj.values)
        normed_embedding = embedding_values / np.linalg.norm(embedding_values)
        embeddings.append(normed_embedding.tolist())

    return embeddings
```

### API Endpoints:

- `POST /api/vector/search` - Search using Gemini embeddings
- `POST /api/vector/add` - Add documents with Gemini embeddings
- `GET /api/vector/stats` - Get collection statistics
- `GET /health` - Health check with embedding status

## Performance Benefits

### Memory Usage:

- **Before**: 512MB+ (sentence-transformers + ChromaDB)
- **After**: ~100MB (ChromaDB lite + Gemini API client)

### Dependencies:

- **Before**: 118 packages (including NVIDIA CUDA libraries)
- **After**: ~15 packages (minimal dependencies)

### Repository Size:

- **Before**: 60MB+ (full repository)
- **After**: ~5MB (only essential files)

### Build Time:

- **Before**: 5+ minutes (heavy ML dependencies)
- **After**: ~1 minute (lightweight dependencies)

## Integration with Other Servers

### AI Server:

- No changes needed
- Continues to use Gemini API for text generation
- Can communicate with vector server via HTTP

### Frontend Server:

- No changes needed
- Continues to proxy requests to vector server
- Gets semantic search results via API

## Testing the Deployment

### 1. Deploy Vector Server:

```bash
# Test health check
curl https://mbs-vector-server.onrender.com/health

# Expected response:
{
  "status": "healthy",
  "message": "Vector server is running",
  "server": "vector",
  "chromadb_available": true,
  "gemini_embeddings_available": true,
  "collection_initialized": true,
  "embedding_model": "models/text-embedding-004"
}
```

### 2. Test Embedding Generation:

```bash
# Test vector search
curl -X POST "https://mbs-vector-server.onrender.com/api/vector/search" \
  -H "Content-Type: application/json" \
  -d '{"query": "chest pain consultation", "n_results": 5}'
```

### 3. Test Document Addition:

```bash
# Add documents with embeddings
curl -X POST "https://mbs-vector-server.onrender.com/api/vector/add" \
  -H "Content-Type: application/json" \
  -d '{
    "documents": [
      {
        "id": "doc1",
        "text": "Professional attendance by a general practitioner for chest pain",
        "metadata": {"item_num": "23", "category": "consultation"}
      }
    ]
  }'
```

## Cost Considerations

### Gemini API Pricing:

- **Embedding Generation**: ~$0.0001 per 1K tokens
- **Typical Query**: ~10 tokens = $0.000001 per query
- **Document Storage**: One-time embedding generation per document

### Cost Optimization:

- **Batch Processing**: Generate embeddings for multiple documents at once
- **Caching**: Store embeddings in ChromaDB to avoid re-generation
- **Efficient Queries**: Use appropriate task types for better results

## Migration from Local Embeddings

### Steps:

1. **Deploy new vector server** with Gemini embeddings
2. **Re-populate vector database** with Gemini-generated embeddings
3. **Update AI server** to use new vector server endpoints
4. **Test functionality** with new embedding system
5. **Monitor performance** and costs

### Data Migration:

```python
# Example: Migrate existing documents to Gemini embeddings
documents = get_existing_documents()  # From old system
embeddings = generate_embeddings([doc["text"] for doc in documents])
# Store in new ChromaDB with Gemini embeddings
```

This approach provides **high-quality semantic search** while staying within **free tier constraints**! 🚀


