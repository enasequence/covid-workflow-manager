from sqlalchemy.orm import Session
from sqlalchemy.sql import text

import models
from database import engine


def get_covid_country_weekly(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CovidCountryWeekly).offset(skip).limit(limit).all()


def get_vcf_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.VCFAll).offset(skip).limit(limit).all()


def get_cov(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cov).offset(skip).limit(limit).all()


def get_meta(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meta).offset(skip).limit(limit).all()


def get_lineage_def(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LineageDef).offset(skip).limit(limit).all()


def get_unique_cov(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UniqueCov).offset(skip).limit(limit).all()


def get_unique_vcf(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UniqueVCF).offset(skip).limit(limit).all()


def get_country_samples(skip: int = 0, limit: int = 100):
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_country_samples OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_lineage_def_description(skip: int = 0, limit: int = 100):
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_lineage_def_description OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_lineage(skip: int = 0, limit: int = 100):
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_lineage OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_new_cases(skip: int = 0, limit: int = 100):
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_new_cases OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_variants_weekly(skip: int = 0, limit: int = 100):
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_variants_weekly OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_worldplot_data(skip: int = 0, limit: int = 100):
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_worldplot_data OFFSET {skip} LIMIT {limit};""").all()
    return outp


def check_view(view_name: str = 'app_country_samples'):
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM pg_attribute WHERE attrelid = '{view_name}'::regclass;""")
    return outp
