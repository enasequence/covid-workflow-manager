from sqlalchemy.schema import DDLElement
from sqlalchemy.ext import compiler
from sqlalchemy.sql import table
import sqlalchemy as sa

from database import SessionLocal, engine

import models
from models import METADATA


class CreateView(DDLElement):
    def __init__(self, name, selectable):
        self.name = name
        self.selectable = selectable


class DropView(DDLElement):
    def __init__(self, name):
        self.name = name


@compiler.compiles(CreateView)
def _create_view(element, compiler, **kw):
    return "CREATE VIEW %s AS %s" % (
        element.name,
        compiler.sql_compiler.process(element.selectable, literal_binds=True),
    )


@compiler.compiles(DropView)
def _drop_view(element, compiler, **kw):
    return "DROP VIEW %s" % (element.name)


def view_exists(ddl, target, connection, **kw):
    return ddl.name in sa.inspect(connection).get_view_names()


def view_doesnt_exist(ddl, target, connection, **kw):
    return not view_exists(ddl, target, connection, **kw)


def view(name, metadata, selectable):
    t = table(name)

    t._columns._populate_separate_keys(
        col._make_proxy(t) for col in selectable.selected_columns
    )

    sa.event.listen(
        metadata,
        "after_create",
        CreateView(name, selectable).execute_if(callable_=view_doesnt_exist),
    )
    sa.event.listen(
        metadata, "before_drop", DropView(name).execute_if(callable_=view_exists)
    )
    return t


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_table_names():
    print(engine.table_names())


def get_new_cases_test():

    print("TEST-1")
    print(type(models.MetaTable))
    print(models.MetaTable.columns)
    print("TEST-1--END")

    print("TEST-2")
    req = sa.select(
              models.MetaTable.c.ena_run.label("ena_run"),
              models.MetaTable.c.collection_date.label("collection_date")
          )
    print(type(req))
    print(req)
    print("TEST-2--END")
    print("TEST-3")
    req_result = engine.execute(req)
    i = 0
    for row in req_result:
        print(row)
        i += 1
        if i == 10:
            break
    print("TEST-3--END")

    meta_view = view("meta_view", METADATA, req)

    with engine.begin() as conn:
        METADATA.create_all(conn)

    print("TEST-4")
    with engine.connect() as conn:
        print(conn.execute(
            sa.select(meta_view.c.ena_run, meta_view.c.collection_date).limit(10)
        ).all())
    print("TEST-4--END")

    return


def read_new_cases_test():
    get_new_cases_test()
    return


get_table_names()

read_new_cases_test()
