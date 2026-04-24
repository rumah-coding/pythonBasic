from __future__ import annotations

from datetime import datetime
from typing import Any

from sqlmodel import SQLModel


class ProjectOut(SQLModel):
    id: int
    name: str
    tagline: str
    description: str
    stack: list[str]
    links: list[dict[str, Any]]
    featured: bool
    created_at: datetime


class BlogPostOut(SQLModel):
    id: int
    title: str
    slug: str
    summary: str
    content_md: str
    tags: list[str]
    published_at: datetime


class ContactIn(SQLModel):
    name: str
    email: str
    message: str

