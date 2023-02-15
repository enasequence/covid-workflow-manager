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
        print(schema)
        assert len(schema) == 1
        assert schema[0][0] == 'public'


test_current_schema()
