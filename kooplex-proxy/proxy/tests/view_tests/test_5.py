from sqlalchemy_utils import create_view
from sqlalchemy import case, func

from models import METADATA
import models
import sqlalchemy as sa

from database import SessionLocal, engine
from sqlalchemy.orm import Session, aliased


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_new_cases_test(db: Session, skip: int = 0, limit: int = 100):

    expr = case([(models.Meta.clean_country == 'USA', 'United States'), ],
                else_=models.Meta.clean_country).label("clean_country_view")
    result_filter = db.query(models.Meta, expr).filter(
        models.Meta.clean_collection_date.isnot(None),
        models.Meta.clean_host == 'Homo sapiens',
        models.Meta.clean_collection_date > func.date('2020-03-15')
    )

    meta_view = create_view('meta_view', result_filter.selectable, METADATA)

    with engine.begin() as conn:
        METADATA.create_all(conn)

    print("TEST-1")
    print(meta_view.columns)
    with engine.connect() as conn:
        print(conn.execute(
            sa.select(meta_view.c.ena_run, meta_view.c.clean_country_view).limit(10)
        ).all())
    print("TEST-1--END")

    result_count = db.query(
        meta_view.c.clean_country_view,
        meta_view.c.date_isoyear,
        meta_view.c.date_isoweek,
        func.count('*').label('weekly_sample')
    ).group_by(
        meta_view.c.clean_country_view,
        meta_view.c.date_isoyear,
        meta_view.c.date_isoweek
    )

    print("TEST-2")
    result_count.limit(limit).all()
    print("TEST-2--END")

    lhs, rhs = aliased(result_count), aliased(result_filter)

    result = db.query(lhs, rhs).outerjoin(rhs)

    print("TEST-3")
    print(result.offset(skip).limit(limit).all())
    print("TEST-3--END")

    return


def read_new_cases_test(skip: int = 0, limit: int = 10):
    get_new_cases_test(next(get_db()), skip=skip, limit=limit)
    return


read_new_cases_test()
