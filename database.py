
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# It will look for an environment variable named DATABASE_URL first
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "mysql+pymysql://root:Prathap%40007@localhost:3307/medical_db"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()