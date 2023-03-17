import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from database import engine
from sqlalchemy import text


def test_current_schema():
    with engine.connect() as conn:
        schema = conn.execute(text("SELECT current_schema();")).all()
        print(f"current schema\n{schema}\n")
        assert len(schema) == 1
        assert schema[0][0] == 'sandbox_public'


def test_current_public_mviews():
    with engine.connect() as conn:
        mviews = conn.execute(
            text("SELECT schemaname, matviewname FROM pg_matviews WHERE schemaname = 'sandbox_public';")
        ).all()
        print(f"schemaname-matviewname\n{mviews}\n")


test_current_schema()
test_current_public_mviews()
