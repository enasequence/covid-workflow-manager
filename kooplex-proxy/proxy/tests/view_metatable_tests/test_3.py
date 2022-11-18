from sqlalchemy import Table, MetaData
from sqlalchemy.sql import text
from sqlalchemy_views import CreateView, DropView

from database import engine
import sqlalchemy as sa
import models


print(engine.table_names())

meta_view = Table('meta_view', MetaData())

definition_1 = text("""SELECT "ena_run", CASE WHEN ("clean_country" = 'USA') THEN ('United States') WHEN 
    NOT("clean_country" = 'USA') THEN ("clean_country") END AS "country_name", "clean_collection_date", 
    "date_isoyear" AS "date_year", "date_isoweek" AS "date_week"
    FROM meta
    WHERE NOT ("clean_collection_date" IS NULL)
    AND "clean_host" = 'Homo sapiens'
    AND "clean_collection_date" > CAST('2020-03-15' AS DATE)"""
)

definition_2 = text("SELECT * from meta")

req = sa.select(
    models.MetaTable.c.ena_run.label("ena_run"),
    models.MetaTable.c.collection_date.label("collection_date")
)

print(req)

req_result = engine.execute(req)
i = 0
for row in req_result:
    print(row)
    i += 1
    if i == 10:
        break

create_view = CreateView(meta_view, req, or_replace=True)
print(str(create_view.compile()).strip())

print(meta_view.columns)

with engine.connect() as conn:
    print(conn.execute(
        sa.select(meta_view.c.ena_run, meta_view.c.collection_date).limit(10)
    ).all())
