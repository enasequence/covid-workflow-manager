import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_SCHEMA = 'public'

SCHEMA_SET = {
    'public',
    'sandbox_public',
    'sandbox_private'
}

SQLALCHEMY_DATABASE_URL = f"postgresql://" \
                          f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@" \
                          f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'options': '-csearch_path={}'.format(POSTGRES_SCHEMA)})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
