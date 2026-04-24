from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlmodel import Session

from .crud import create_contact_message, list_posts, list_projects
from .db import get_session
from .schemas import BlogPostOut, ContactIn, ProjectOut

router = APIRouter(prefix="/api")


@router.get("/projects", response_model=list[ProjectOut])
def get_projects(session: Session = Depends(get_session)):
    return list_projects(session)


@router.get("/posts", response_model=list[BlogPostOut])
def get_posts(session: Session = Depends(get_session)):
    return list_posts(session)


@router.post("/contact")
def post_contact(payload: ContactIn, session: Session = Depends(get_session)):
    create_contact_message(session, name=payload.name, email=payload.email, message=payload.message)
    return {"ok": True}

