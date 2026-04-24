## Backend (FastAPI)

### Run

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Env

Copy `.env.example` to `.env` if you want to customize.

