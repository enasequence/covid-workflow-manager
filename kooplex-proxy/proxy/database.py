from sqlalchemy.ext.declarative import declarative_base
import os


POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_SCHEMA_KEY = 'public'

ALLOWED_SCHEMAS = {
    'public': 'datahub_0',
    'schema_1': 'sandbox_public',
    'schema_2': 'sandbox_private'
}

SQLALCHEMY_DATABASE_URL = f"postgresql://" \
                          f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@" \
                          f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

Base = declarative_base()
