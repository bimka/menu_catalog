import os
import socket

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# host = os.getenv("DB_HOST", "0.0.0.0")
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:postgres@0.0.0.0:5432/postgres"

# addr = socket.gethostbyname('db')
# SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:postgres@{addr}:5432/postgres"
# SQLALCHEMY_DATABASE_URL = os.getenv("DB_NAME_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
