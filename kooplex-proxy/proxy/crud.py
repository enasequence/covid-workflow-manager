from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta

import models
from database import SCHEMA_SET


def schema_changing(model: DeclarativeMeta, endp_schema: str):
    current_schema = model.get_schema()
    if current_schema != endp_schema:
        if endp_schema in SCHEMA_SET:
            model.set_schema(schema_name=endp_schema)
            print(f"-- Changing schema from '{current_schema}' to '{endp_schema}' for the endpoint: country_samples --")
            return 0
        else:
            print(f"This schema is unavailable for using, please use one of these schemas: {SCHEMA_SET}")
            return 1
    return 0


def get_country_samples(db: Session, skip: int = 0, limit: int = 100, endp_schema='sandbox_public'):
    model = models.MViewCountrySamples
    exit_code = schema_changing(model=model, endp_schema=endp_schema)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_human_meta_mv(db: Session, skip: int = 0, limit: int = 100, endp_schema='sandbox_public'):
    model = models.MViewHumanMetaMv
    exit_code = schema_changing(model=model, endp_schema=endp_schema)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_human_meta_mv_jhd(db: Session, skip: int = 0, limit: int = 100, endp_schema='sandbox_public'):
    model = models.MViewHumanMetaMvJhd
    exit_code = schema_changing(model=model, endp_schema=endp_schema)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_lineage_def(db: Session, skip: int = 0, limit: int = 100, endp_schema='sandbox_public'):
    model = models.LineageDef
    exit_code = schema_changing(model=model, endp_schema=endp_schema)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_lineage(db: Session, skip: int = 0, limit: int = 100, endp_schema='sandbox_public'):
    model = models.MViewLineage
    exit_code = schema_changing(model=model, endp_schema=endp_schema)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_new_cases_jhd(db: Session, skip: int = 0, limit: int = 100, endp_schema='sandbox_public'):
    model = models.MViewNewCasesJhd
    exit_code = schema_changing(model=model, endp_schema=endp_schema)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_variants_weekly(db: Session, skip: int = 0, limit: int = 100, endp_schema='sandbox_public'):
    model = models.MViewVariantsWeekly
    exit_code = schema_changing(model=model, endp_schema=endp_schema)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()
