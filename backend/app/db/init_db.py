import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv

from .base import Base

# Load environment variable for local development
load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable not set.")

engine = create_engine(
    DATABASE_URL,
    poolclass=NullPool,   # Use NullPool for cloud managed DB (like Supabase)
    future=True,
    echo=False
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True
)

def get_db():
    """Dependency for FastAPI routes to get a session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
