from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import text

import models
from models import db_connect


def get_country_samples(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewCountrySamples
    return db.query(model).offset(skip).limit(limit).all()


def get_human_meta_mv(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewHumanMetaMv
    return db.query(model).offset(skip).limit(limit).all()


def get_human_meta_mv_jhd(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewHumanMetaMvJhd
    return db.query(model).offset(skip).limit(limit).all()


def get_lineage_def(db: Session, skip: int = 0, limit: int = 100):
    model = models.LineageDef
    return db.query(model).offset(skip).limit(limit).all()


def get_lineage(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewLineage
    return db.query(model).offset(skip).limit(limit).all()


def get_new_cases_jhd(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewNewCasesJhd
    return db.query(model).offset(skip).limit(limit).all()


def get_variants_weekly(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewVariantsWeekly
    return db.query(model).offset(skip).limit(limit).all()


def get_unique_ena_run_summary(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewUniqueEnaRunSum
    return db.query(model).offset(skip).limit(limit).all()


def filter_custom_browser_cov(db: Session, included: str, excluded: str, skip: int = 0,
                              limit: int = 100):
    global db_connect
    model = models.SProcFilterCustomBrowserCov
    model.call(session=db, included=included, excluded=excluded)
    outp = db.execute(
        text(f"""SELECT * FROM {db_connect.get_schema()}.filter_country_count() OFFSET {skip} LIMIT {limit};""")
    ).all()
    return outp


def filter_custom_browser_cov_time(db: Session, included: str, excluded: str, skip: int = 0,
                                   limit: int = 100):
    global db_connect
    model = models.SProcFilterCustomBrowserCovTime
    model.call(session=db, included=included, excluded=excluded)
    outp = db.execute(
        text(f"""SELECT * FROM {db_connect.get_schema()}.filter_country_count_time() OFFSET {skip} LIMIT {limit};""")
    ).all()
    return outp


def table_count(db: Session, table_name: str):
    model = models.TableCount
    outp = db.execute(
        text(f"""SELECT COUNT(*) FROM {model.get_schema()}.{table_name};""")
    ).all()
    return outp
