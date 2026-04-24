from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()


def env(key: str, default: str) -> str:
    val = os.getenv(key)
    return default if val is None or val.strip() == "" else val.strip()


APP_NAME = env("APP_NAME", "Portfolio API")
DATABASE_URL = env("DATABASE_URL", "sqlite:///./portfolio.db")
FRONTEND_ORIGIN = env("FRONTEND_ORIGIN", "http://127.0.0.1:5173")

