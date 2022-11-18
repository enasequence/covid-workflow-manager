from sqlalchemy.orm import Session

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


def get_sorted_meta(db: Session, skip: int = 0, limit: int = 100):
    request = f"SELECT * FROM meta WHERE (NOT((clean_country) IS NULL)) ORDER BY " \
              f"clean_collection_date, clean_country, clean_host OFFSET {skip} LIMIT {limit};"

    with engine.connect() as conn:
        outp = conn.execute(request).all()
    return outp


def get_lineage_def(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LineageDef).offset(skip).limit(limit).all()


def get_unique_cov(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UniqueCov).offset(skip).limit(limit).all()


def get_unique_vcf(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UniqueVCF).offset(skip).limit(limit).all()


def get_country_samples(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.View_country_samples).offset(skip).limit(limit).all()


def get_lineage_def_description(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.View_lineage_def_description).offset(skip).limit(limit).all()

def get_lineage(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.View_lineage).offset(skip).limit(limit).all()


def get_new_cases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.View_new_cases).offset(skip).limit(limit).all()


def get_variants_weekly(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.View_variants_weekly).offset(skip).limit(limit).all()


def get_worldplot_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.View_worldplot_data).offset(skip).limit(limit).all()


def get_table_description(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.View_table_description).offset(skip).limit(limit).all()


def get_column_description(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.View_column_description).offset(skip).limit(limit).all()
