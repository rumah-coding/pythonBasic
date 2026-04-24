from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

from sqlalchemy import Column
from sqlalchemy.types import JSON
from sqlmodel import Field, SQLModel


class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    tagline: str
    description: str
    stack: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    links: list[dict[str, Any]] = Field(default_factory=list, sa_column=Column(JSON))
    featured: bool = Field(default=False, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)


class BlogPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    slug: str = Field(index=True, unique=True)
    summary: str
    content_md: str
    tags: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    published_at: datetime = Field(default_factory=datetime.utcnow, index=True)


class ContactMessage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    message: str
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)

