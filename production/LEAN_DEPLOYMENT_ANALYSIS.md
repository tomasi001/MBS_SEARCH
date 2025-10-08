# Lean Deployment Analysis - File Requirements by Server

## File Dependency Analysis

### 🟢 Vector Server Requirements

**Core Files Needed:**

- `production/vector_server.py` - Main server file
- `production/pyproject_vector.toml` - Dependencies
- `config.py` - Configuration settings
- `src/mbs_clarity/` - Database module (if needed)

**Imports Analysis:**

```python
# From vector_server.py
from config import settings  # Needs config.py
# No other local imports - self-contained!
```

**Files NOT Needed:**

- `production/ai_server.py` ❌
- `production/frontend_server.py` ❌
- `services/gemini_service.py` ❌
- `services/nlp_service.py` ❌
- `templates/enhanced_chat_ui.py` ❌
- `mbs.db` ❌
- `chroma_db/` ❌ (will be created fresh)

### 🟡 AI Server Requirements

**Core Files Needed:**

- `production/ai_server.py` - Main server file
- `production/pyproject_ai.toml` - Dependencies
- `config.py` - Configuration settings
- `services/gemini_service.py` - Gemini API service

**Imports Analysis:**

```python
# From ai_server.py
from config import settings  # Needs config.py
from services.gemini_service import GeminiService  # Needs services/
```

**Files NOT Needed:**

- `production/vector_server.py` ❌
- `production/frontend_server.py` ❌
- `services/vector_service.py` ❌
- `services/nlp_service.py` ❌
- `templates/enhanced_chat_ui.py` ❌
- `src/mbs_clarity/` ❌
- `mbs.db` ❌
- `chroma_db/` ❌

### 🔵 Frontend Server Requirements

**Core Files Needed:**

- `production/frontend_server.py` - Main server file
- `production/pyproject_frontend.toml` - Dependencies
- `config.py` - Configuration settings
- `templates/enhanced_chat_ui.py` - HTML UI
- `src/mbs_clarity/` - Database module
- `mbs.db` - SQLite database

**Imports Analysis:**

```python
# From frontend_server.py
from config import settings  # Needs config.py
from templates.enhanced_chat_ui import ENHANCED_CHAT_UI  # Needs templates/
from src.mbs_clarity.db import fetch_item_aggregate  # Needs src/
```

**Files NOT Needed:**

- `production/vector_server.py` ❌
- `production/ai_server.py` ❌
- `services/` ❌ (all services)
- `chroma_db/` ❌

## Render Build Filter Strategy

### Option 1: Root Directory + Build Filters

**Vector Server:**

- **Root Directory**: `production/`
- **Included Paths**:
  - `vector_server.py`
  - `pyproject_vector.toml`
  - `../config.py`
  - `../src/` (if needed)
- **Ignored Paths**: Everything else

**AI Server:**

- **Root Directory**: `production/`
- **Included Paths**:
  - `ai_server.py`
  - `pyproject_ai.toml`
  - `../config.py`
  - `../services/gemini_service.py`
- **Ignored Paths**: Everything else

**Frontend Server:**

- **Root Directory**: `production/`
- **Included Paths**:
  - `frontend_server.py`
  - `pyproject_frontend.toml`
  - `../config.py`
  - `../templates/`
  - `../src/`
  - `../mbs.db`
- **Ignored Paths**: Everything else

### Option 2: Separate Git Branches/Repos

Create separate minimal repositories for each server with only required files.

### Option 3: Build Script Approach

Use build scripts that copy only required files to a temporary directory.

## Recommended Approach: Root Directory + Build Filters

This is the cleanest approach using Render's native features:

### Vector Server Configuration

```yaml
Root Directory: production/
Build Filters:
  Included Paths:
    - vector_server.py
    - pyproject_vector.toml
    - ../config.py
  Ignored Paths:
    - "*"
    - "!vector_server.py"
    - "!pyproject_vector.toml"
    - "!../config.py"
```

### AI Server Configuration

```yaml
Root Directory: production/
Build Filters:
  Included Paths:
    - ai_server.py
    - pyproject_ai.toml
    - ../config.py
    - ../services/gemini_service.py
  Ignored Paths:
    - "*"
    - "!ai_server.py"
    - "!pyproject_ai.toml"
    - "!../config.py"
    - "!../services/gemini_service.py"
```

### Frontend Server Configuration

```yaml
Root Directory: production/
Build Filters:
  Included Paths:
    - frontend_server.py
    - pyproject_frontend.toml
    - ../config.py
    - ../templates/
    - ../src/
    - ../mbs.db
  Ignored Paths:
    - "*"
    - "!frontend_server.py"
    - "!pyproject_frontend.toml"
    - "!../config.py"
    - "!../templates/"
    - "!../src/"
    - "!../mbs.db"
```

## File Size Reduction

**Current Repository Size**: ~50MB+ (with all files)
**Optimized Sizes**:

- Vector Server: ~5MB (only vector files + config)
- AI Server: ~3MB (only AI files + config)
- Frontend Server: ~15MB (includes database + UI)

**Total Reduction**: ~70% smaller deployments per server
