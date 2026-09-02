import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # Default fallback to SQLite if no DATABASE_URL environment variable is set on Render
    DATABASE_URL = "sqlite:///./medical.db"
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    # Handle PostgreSQL URL format if using PostgreSQL on Render
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()