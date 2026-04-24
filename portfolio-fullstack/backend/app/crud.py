from __future__ import annotations

from datetime import datetime

from sqlmodel import Session, select

from .models import BlogPost, ContactMessage, Project


def list_projects(session: Session) -> list[Project]:
    return list(session.exec(select(Project).order_by(Project.featured.desc(), Project.created_at.desc())))


def list_posts(session: Session) -> list[BlogPost]:
    return list(session.exec(select(BlogPost).order_by(BlogPost.published_at.desc())))


def create_contact_message(session: Session, *, name: str, email: str, message: str) -> ContactMessage:
    m = ContactMessage(name=name, email=email, message=message)
    session.add(m)
    session.commit()
    session.refresh(m)
    return m


def seed_if_empty(session: Session) -> None:
    has_project = session.exec(select(Project.id)).first() is not None
    has_post = session.exec(select(BlogPost.id)).first() is not None
    if has_project and has_post:
        return

    if not has_project:
        session.add(
            Project(
                name="Portfolio Fullstack",
                tagline="React + FastAPI + SQLite",
                description="Portfolio template dengan API backend, contact form tersimpan di DB, dan UI modern.",
                stack=["React", "Tailwind", "FastAPI", "SQLModel", "SQLite"],
                links=[
                    {"label": "Source", "url": "https://github.com/"},
                    {"label": "Demo", "url": "https://example.com"},
                ],
                featured=True,
                created_at=datetime.utcnow(),
            )
        )
        session.add(
            Project(
                name="API Starter",
                tagline="REST API yang rapi + docs otomatis",
                description="Contoh struktur backend yang mudah dikembangkan untuk proyek lain.",
                stack=["FastAPI", "Pydantic", "SQLite"],
                links=[{"label": "Docs", "url": "http://127.0.0.1:8001/docs"}],
                featured=False,
                created_at=datetime.utcnow(),
            )
        )

    if not has_post:
        session.add(
            BlogPost(
                title="Kenapa FastAPI enak untuk portfolio",
                slug="kenapa-fastapi",
                summary="Ringkas: cepat, type-safe, docs otomatis, dan cocok buat showcase backend.",
                content_md="# Kenapa FastAPI\n\nFastAPI itu cepat dipakai, punya OpenAPI docs otomatis, dan enak untuk API kecil-menengah.\n",
                tags=["fastapi", "python", "backend"],
                published_at=datetime.utcnow(),
            )
        )

    session.commit()

