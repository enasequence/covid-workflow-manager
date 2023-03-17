from sqlalchemy_utils import create_view

from models import METADATA
import models
import sqlalchemy as sa

from database import engine


req = sa.select(
    models.MetaTable.c.ena_run.label("ena_run"),
    models.MetaTable.c.collection_date.label("clean_country")
)

meta_view = create_view('meta_view', req, METADATA)

with engine.begin() as conn:
    METADATA.create_all(conn)

with engine.connect() as conn:
    print(conn.execute(
        sa.select(meta_view.c.ena_run, meta_view.c.clean_country).limit(10)
    ).all())
