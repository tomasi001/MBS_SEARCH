# Poetry-Based Deployment Strategy

## Why Poetry is Better Than pip

### **1. Consistency with Your Project**

- Your project already uses Poetry (`pyproject.toml`, `poetry.lock`)
- You explicitly requested Poetry commands (`poetry add`, `poetry lock`)
- Maintains consistency across development and production

### **2. Better Dependency Management**

- **Automatic dependency resolution** - Poetry handles conflicts
- **Reproducible builds** - `poetry.lock` ensures exact versions
- **Virtual environment management** - Poetry manages environments automatically
- **Dependency groups** - Can separate dev, test, and production dependencies

### **3. Render Native Support**

- Render has built-in Poetry support
- Poetry is the default Python dependency manager on Render
- No need to switch to pip

## Optimized Poetry Deployment Strategy

### **Option 1: Use Existing pyproject.toml (Recommended)**

Since your current `pyproject.toml` already has all dependencies, we can use it for all servers:

```bash
# All servers use the same build command
Build Command: poetry install --only=main
Start Command: poetry run python production/[server_name].py
```

**Benefits:**

- ✅ Simple and consistent
- ✅ Uses your existing Poetry setup
- ✅ Render will only install main dependencies (excludes dev dependencies)
- ✅ All servers get the same environment

**Drawbacks:**

- ❌ All servers install all dependencies (including heavy ML libraries)

### **Option 2: Separate pyproject.toml Files (Advanced)**

Create separate Poetry projects for each server:

```bash
# Vector Server
Build Command: cd production && poetry install --only=main -f pyproject_vector.toml
Start Command: cd production && poetry run python vector_server.py

# AI Server
Build Command: cd production && poetry install --only=main -f pyproject_ai.toml
Start Command: cd production && poetry run python ai_server.py

# Frontend Server
Build Command: cd production && poetry install --only=main -f pyproject_frontend.toml
Start Command: cd production && poetry run python frontend_server.py
```

**Benefits:**

- ✅ True dependency separation
- ✅ Minimal dependencies per server
- ✅ Fastest build times

**Drawbacks:**

- ❌ More complex setup
- ❌ Multiple Poetry projects to maintain
- ❌ Potential path issues

## Recommended Approach

**Use Option 1** with your existing `pyproject.toml` because:

1. **Simplicity** - One Poetry project, consistent setup
2. **Reliability** - Uses your tested dependency configuration
3. **Maintainability** - Single source of truth for dependencies
4. **Render Compatibility** - Standard Poetry deployment pattern

The optimization comes from:

- **`--only=main`** - Excludes dev dependencies
- **Poetry's caching** - Render caches Poetry dependencies
- **Virtual environment efficiency** - Poetry manages environments optimally

## Deployment Commands

### **All Servers (Recommended)**

```bash
Build Command: poetry install --only=main
Start Command: poetry run python production/[server_name].py
```

### **Environment Variables**

```bash
# Vector Server
USE_LOCAL_EMBEDDINGS=true
LOCAL_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
CHROMA_PERSIST_DIRECTORY=./chroma_db

# AI Server
GEMINI_API_KEY=your_gemini_api_key
VECTOR_SERVER_URL=https://mbs-vector-server.onrender.com

# Frontend Server
AI_SERVER_URL=https://mbs-ai-server.onrender.com
VECTOR_SERVER_URL=https://mbs-vector-server.onrender.com
```

## Why This is Better Than pip

1. **Consistency** - Matches your development environment
2. **Reliability** - Poetry handles dependency resolution better
3. **Reproducibility** - `poetry.lock` ensures exact versions
4. **Simplicity** - One command, one configuration
5. **Render Native** - Built-in support, no workarounds needed

The key insight is that **Poetry itself is the optimization** - it's more efficient than pip for dependency management, and Render's caching makes repeated builds fast.
