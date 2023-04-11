from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta

import models
from database import ALLOWED_SCHEMAS


def schema_changing(model: DeclarativeMeta, endpoint_name: str, endp_schema_key: str):
    current_schema = model.get_schema()

    if not endp_schema_key:
        endp_schema = ALLOWED_SCHEMAS.get('schema_1')
    elif endp_schema_key not in ALLOWED_SCHEMAS:
        values = '/'.join(list(ALLOWED_SCHEMAS.values()))
        print(f"This schema is unavailable for using, please use one of these schemas: {values}")
        return 1
    else:
        endp_schema = ALLOWED_SCHEMAS[endp_schema_key]

    if current_schema != endp_schema:
        model.set_schema(schema_name=endp_schema)
        print(f"-- Changing schema from '{current_schema}' to '{endp_schema}' for the endpoint: {endpoint_name} --")
        return 0
    else:
        return 0


def get_country_samples(db: Session, endp_schema_key: str, skip: int = 0, limit: int = 100):
    model = models.MViewCountrySamples
    exit_code = schema_changing(model=model, endpoint_name='country_samples', endp_schema_key=endp_schema_key)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_human_meta_mv(db: Session, endp_schema_key: str, skip: int = 0, limit: int = 100):
    model = models.MViewHumanMetaMv
    exit_code = schema_changing(model=model, endpoint_name='human_meta_mv', endp_schema_key=endp_schema_key)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_human_meta_mv_jhd(db: Session, endp_schema_key: str, skip: int = 0, limit: int = 100):
    model = models.MViewHumanMetaMvJhd
    exit_code = schema_changing(model=model, endpoint_name='human_meta_mv_jhd', endp_schema_key=endp_schema_key)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_lineage_def(db: Session, endp_schema_key: str, skip: int = 0, limit: int = 100):
    model = models.LineageDef
    exit_code = schema_changing(model=model, endpoint_name='lineage_def', endp_schema_key=endp_schema_key)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_lineage(db: Session, endp_schema_key: str, skip: int = 0, limit: int = 100):
    model = models.MViewLineage
    exit_code = schema_changing(model=model, endpoint_name='lineage', endp_schema_key=endp_schema_key)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_new_cases_jhd(db: Session, endp_schema_key: str, skip: int = 0, limit: int = 100):
    model = models.MViewNewCasesJhd
    exit_code = schema_changing(model=model, endpoint_name='new_cases_jhd', endp_schema_key=endp_schema_key)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_variants_weekly(db: Session, endp_schema_key: str, skip: int = 0, limit: int = 100):
    model = models.MViewVariantsWeekly
    exit_code = schema_changing(model=model, endpoint_name='variants_weekly', endp_schema_key=endp_schema_key)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()


def get_unique_ena_run_sum(db: Session, endp_schema_key: str, skip: int = 0, limit: int = 100):
    model = models.MViewUniqueEnaRunSum
    exit_code = schema_changing(model=model, endpoint_name='unique_ena_run_sum', endp_schema_key=endp_schema_key)
    if exit_code == 0:
        return db.query(model).offset(skip).limit(limit).all()
    return list()
