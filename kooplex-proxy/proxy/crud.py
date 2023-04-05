from sqlalchemy.orm import Session

import models
from database import SCHEMA_SET


def get_country_samples(db: Session, skip: int = 0, limit: int = 100, endp_schema='sandbox_public'):

    current_schema = models.MViewCountrySamples.get_schema()
    if current_schema != endp_schema and endp_schema in SCHEMA_SET:
        models.MViewCountrySamples.set_schema(schema_name=endp_schema)
        print(f"Changing schema from {current_schema} to {endp_schema} for the endpoint: country_samples\n")

    return db.query(models.MViewCountrySamples).offset(skip).limit(limit).all()


def get_human_meta_mv(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MViewHumanMetaMv).offset(skip).limit(limit).all()


def get_human_meta_mv_jhd(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MViewHumanMetaMvJhd).offset(skip).limit(limit).all()


def get_lineage_def(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LineageDef).offset(skip).limit(limit).all()


def get_lineage(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MViewLineage).offset(skip).limit(limit).all()


def get_new_cases_jhd(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MViewNewCasesJhd).offset(skip).limit(limit).all()


def get_variants_weekly(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MViewVariantsWeekly).offset(skip).limit(limit).all()
