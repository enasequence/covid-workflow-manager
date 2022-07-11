from sqlalchemy.orm import Session
from sqlalchemy import func

import models
from database import engine


def get_covid_country_weekly(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.CovidCountryWeekly).offset(skip).all()
    else:
        return db.query(models.CovidCountryWeekly).offset(skip).limit(limit).all()


def get_vcf_all(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.VCFAll).offset(skip).all()
    else:
        return db.query(models.VCFAll).offset(skip).limit(limit).all()


def get_cov(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.Cov).offset(skip).all()
    else:
        return db.query(models.Cov).offset(skip).limit(limit).all()


def get_meta(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.Meta).offset(skip).all()
    else:
        return db.query(models.Meta).offset(skip).limit(limit).all()


def get_sorted_meta(db: Session, date: str = '2020-03-15', skip: int = 0, limit: int = 100):
    query_obj = db.query(models.Meta).filter(
                    models.Meta.clean_collection_date > func.date(date)
                ).order_by(
                    models.Meta.clean_collection_date.asc(),
                    models.Meta.clean_country.asc(),
                    models.Meta.clean_host.asc()
                ).offset(skip)
    if limit == -1:
        return query_obj.all()
    else:
        return query_obj.limit(limit).all()


def get_lineage_def(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.LineageDef).offset(skip).all()
    else:
        return db.query(models.LineageDef).offset(skip).limit(limit).all()


def get_unique_cov(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.UniqueCov).offset(skip).all()
    else:
        return db.query(models.UniqueCov).offset(skip).limit(limit).all()


def get_unique_vcf(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.UniqueVCF).offset(skip).all()
    else:
        return db.query(models.UniqueVCF).offset(skip).limit(limit).all()


def get_country_samples(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_country_samples OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_lineage_def_description(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_lineage_def_description OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_lineage(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_lineage OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_new_cases(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_new_cases OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_variants_weekly(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_variants_weekly OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_worldplot_data(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_worldplot_data OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_table_description(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM table_description OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_column_description(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM column_description OFFSET {skip} LIMIT {limit};""").all()
    return outp
