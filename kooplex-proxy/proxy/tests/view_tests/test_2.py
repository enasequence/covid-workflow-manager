from sqlalchemy.schema import DDLElement
from sqlalchemy.ext import compiler
from sqlalchemy.sql import table
import sqlalchemy as sa

from sqlalchemy.orm import Session, aliased
from sqlalchemy import case, func
from sqlalchemy import and_

from database import SessionLocal, engine

from sqlalchemy.orm import Session
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


def get_new_cases_test(db: Session, limit: int = 100):

    expr = case([(models.Meta.clean_country == 'USA', 'United States'), ],
                else_=models.Meta.clean_country).label("clean_country")
    result_filter = db.query(models.Meta, expr).filter(
        models.Meta.clean_collection_date.isnot(None),
        models.Meta.clean_host == 'Homo sapiens',
        models.Meta.clean_collection_date > func.date('2020-03-15')
    )

    print("TEST-1")
    print(result_filter)
    print(result_filter.limit(limit).all())
    print("TEST-1--END")

    meta_view = view("meta_view", METADATA, result_filter.statement)

    with engine.begin() as conn:
        METADATA.create_all(conn)

    print("TEST-2")
    print(meta_view.columns)
    with engine.connect() as conn:
        print(conn.execute(
            sa.select(meta_view.c.ena_run, meta_view.c.clean_country).limit(10)
        ).all())
    print("TEST-2--END")

    result_count = db.query(
        meta_view.c.clean_country,
        meta_view.c.date_isoyear,
        meta_view.c.date_isoweek,
        func.count('*').label('weekly_sample')
    ).group_by(
        meta_view.c.clean_country,
        meta_view.c.date_isoyear,
        meta_view.c.date_isoweek
    )

    print("TEST-3")
    print(result_count.limit(limit).all())
    print("TEST-3--END")

    print("TEST-4")
    print(type(result_count), type(result_filter))
    #lhs, rhs = aliased(result_count), aliased(result_filter)
    #result = db.query(lhs, rhs).outerjoin(rhs)
    #print(result.offset(skip).limit(limit).all())

    lhs, rhs = aliased(result_count.subquery()), aliased(result_filter.subquery())

    result = db.query(lhs, rhs).outerjoin(
        rhs,
        and_(
            lhs.c.date_isoyear == rhs.c.date_isoyear,
            lhs.c.clean_country_view == rhs.c.clean_country,
            lhs.c.date_isoweek == rhs.c.date_isoweek
        )
    )

    print(result.limit(limit).all())
    print("TEST-4--END")

    return


def read_new_cases_test(limit: int = 10):
    get_new_cases_test(next(get_db()), limit=limit)
    return


get_table_names()

read_new_cases_test()
