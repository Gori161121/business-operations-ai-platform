"""
Database configuration (ORM layer).

Defaults to a local SQLite file so the app runs with zero setup.
Set DATABASE_URL to a PostgreSQL DSN (see database/schema.sql) in production
or docker-compose.
"""

import os

from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./operations.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)


def init_db() -> None:
    """Create all tables. Importing models registers them on the metadata."""
    from backend import models  # noqa: F401
    SQLModel.metadata.create_all(engine)


def get_session():
    """FastAPI dependency yielding a database session."""
    with Session(engine) as session:
        yield session
