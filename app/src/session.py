import os
import socket

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

# SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL")
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@172.21.0.2:5432/postgres"
# addr = socket.gethostbyname('db')
# SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:postgres@{addr}:5432/postgres"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@db:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
