import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

# Look for DATABASE_URL environment variable, fallback to local MySQL Workbench
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