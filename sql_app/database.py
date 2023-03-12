import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app/database2.db"
database_url = os.environ["DATABASE_URL"]
user = os.environ["DATABASE_USER_NAME"]
password = os.environ["DATABASE_PASSWORD"]
port = int(os.environ["DATABASE_PORT"])


SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="postgresql",
    username = user,
    password=password,
    port = port,
    host = 'localhost',
    database = 'postgres'
)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
