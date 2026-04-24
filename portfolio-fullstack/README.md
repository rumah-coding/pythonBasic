## Portfolio Fullstack (React + FastAPI)

### 1) Run backend

```bash
cd portfolio-fullstack/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open API docs at `http://127.0.0.1:8000/docs`.

### 2) Run frontend

```bash
cd portfolio-fullstack/frontend
npm install
npm run dev
```

Frontend expects backend at `http://127.0.0.1:8000` by default.

Optional env override:

Create `portfolio-fullstack/frontend/.env`:

```bash
VITE_API_BASE=http://127.0.0.1:8000
```

