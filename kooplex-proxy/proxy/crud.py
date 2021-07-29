from operator import and_

from sqlalchemy import null, func, select
from sqlalchemy.orm import Session
from typing import List

import models


def get_covid_country_weekly(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CovidCountryWeekly).offset(skip).limit(limit).all()


def get_unique_vcf_append(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UniqueVCFAppend).offset(skip).limit(limit).all()


def get_vcf_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.VCFAll).offset(skip).limit(limit).all()


def get_cov(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cov).offset(skip).limit(limit).all()


def get_meta(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meta).offset(skip).limit(limit).all()


def get_unique_cov_append(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UniqueCovAppend).offset(skip).limit(limit).all()


def get_lineage_def(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LineageDef).offset(skip).limit(limit).all()


def get_operation(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Operation).offset(skip).limit(limit).all()


def get_unique_cov(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UniqueCov).offset(skip).limit(limit).all()


def get_unique_vcf(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UniqueVCF).offset(skip).limit(limit).all()


def get_vcf_all_append(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.VCFAllAppend).offset(skip).limit(limit).all()


def get_country_samples(db: Session, skip: int = 0, limit: int = 100) -> List[models.CountrySamples]:
    stmt = db.query(models.Meta.clean_country, func.count('*').label('n_sample')).filter(
        and_(models.Meta.clean_host == 'Homo sapiens',
             models.Meta.collection_date.isnot(None))).group_by(models.Meta.clean_country)
    return stmt.offset(skip).limit(limit).all()


def get_lineage_def_some_fields(db: Session, skip: int = 0, limit: int = 100) -> List[models.LineageDefSelectedFields]:
    return db.query(models.LineageDef.variant_id, models.LineageDef.pango, models.LineageDef.nextstrain,
                    models.LineageDef.description).offset(skip).limit(limit).all()
