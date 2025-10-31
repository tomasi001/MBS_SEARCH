# Repository Cleanup Migration Plan

## Dependencies Analysis

### Vector Server (`production/vector_server_gemini.py`)

- **Standalone** - No project-specific imports
- Only uses standard libraries and external packages (FastAPI, ChromaDB, Gemini, numpy)
- Uses `chroma_db/` directory (created at runtime)

### AI Server (`production/ai_server.py`)

- Imports:
  - `config.settings` → `config.py`
  - `services.gemini_service.GeminiService` → `services/gemini_service.py`
- `services/gemini_service.py` imports:
  - `config.settings` → `config.py`

### Frontend Server (`production/frontend_server.py`)

- Imports:
  - `config.settings` → `config.py`
  - `templates.enhanced_chat_ui.ENHANCED_CHAT_UI` → `templates/enhanced_chat_ui.py`
  - `src.mbs_clarity.db.fetch_item_aggregate` → `src/mbs_clarity/db.py`
  - `src.mbs_clarity.compatibility_checker.check_mbs_compatibility` → `src/mbs_clarity/compatibility_checker.py`
- `src/mbs_clarity/compatibility_checker.py` imports:
  - `src.mbs_clarity.db.fetch_item_aggregate` → `src/mbs_clarity/db.py`
- `src/mbs_clarity/db.py` - Uses standard library only (os, sqlite3)

## Required Files List

### Core Server Files

- `production/vector_server_gemini.py`
- `production/ai_server.py`
- `production/frontend_server.py`

### Configuration

- `config.py`

### Services

- `services/gemini_service.py`
- `services/__init__.py` (create if missing)

### Templates

- `templates/enhanced_chat_ui.py`

### Source Code

- `src/mbs_clarity/__init__.py`
- `src/mbs_clarity/db.py`
- `src/mbs_clarity/compatibility_checker.py`

### Database

- `mbs.db` (SQLite database file)

### Deployment Configuration

- `production/pyproject_ai.toml`
- `production/pyproject_vector_gemini.toml`
- `production/pyproject_frontend.toml`
- `runtime.txt`

### Git & Project Files

- `.gitignore`
- `README.md` (optional, for documentation)

## Directory Structure for New Repo

```
mbs-clarity-clean/
├── production/
│   ├── vector_server_gemini.py
│   ├── ai_server.py
│   ├── frontend_server.py
│   ├── pyproject_ai.toml
│   ├── pyproject_vector_gemini.toml
│   └── pyproject_frontend.toml
├── config.py
├── services/
│   ├── __init__.py
│   └── gemini_service.py
├── templates/
│   └── enhanced_chat_ui.py
├── src/
│   └── mbs_clarity/
│       ├── __init__.py
│       ├── db.py
│       └── compatibility_checker.py
├── mbs.db
├── runtime.txt
├── .gitignore
└── README.md
```

## Notes

- `chroma_db/` directory will be created at runtime by ChromaDB
- No need to copy test files, scripts, or other bloat
- All deployment configs remain the same (3 separate Render services)
