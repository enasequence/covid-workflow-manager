import sys
from operator import and_

from sqlalchemy import null, func, select, case, literal_column, text, cast, DATE
from sqlalchemy.orm import Session
from typing import List

from sqlalchemy.sql.functions import count

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
             models.Meta.collection_date is not None)).group_by(models.Meta.clean_country)
    return stmt.offset(skip).limit(limit).all()


def get_lineage_def_some_fields(db: Session, skip: int = 0, limit: int = 100) -> List[models.LineageDefSelectedFields]:
    return db.query(models.LineageDef.variant_id, models.LineageDef.pango, models.LineageDef.type_variant,
                    models.LineageDef.description).offset(skip).limit(limit).all()


def get_lineage0(db: Session, skip: int = 0, limit: int = 100) -> List[models.Lineage0]:
    stmt = db.query(models.Meta.clean_collection_date, case([(models.Meta.clean_country == 'USA', "'United States'")],
                                                            else_=models.Meta.clean_country).label('clean_country'),
                    func.count('*').label('n')).filter(models.Meta.clean_host == 'Homo sapiens'
                                                       ).filter(models.Meta.collection_date is not None) \
        .filter(func.DATE(
        models.Meta.clean_collection_date) > cast(
        '2020-01-01', DATE)).group_by(
        models.Meta.clean_collection_date, models.Meta.clean_country)
    return stmt.offset(skip).limit(limit).all()


def get_lineage(db: Session, skip: int = 0, limit: int = 100) -> List[models.Lineage]:
    stmt = db.query(models.Meta.clean_collection_date, case([(models.Meta.clean_country == 'USA', "'United States'")],
                                                            else_=models.Meta.clean_country).label('clean_country'),
                    models.LineageDef.variant_id,
                    func.count('*').label('n')).filter(models.Meta.clean_host == 'Homo sapiens'
                                                       ).join(models.LineageDef,
                                                              models.Meta.ena_run == models.LineageDef.variant_id).filter(
        models.Meta.collection_date is not None).filter(func.DATE(
        models.Meta.clean_collection_date) > cast(
        '2020-01-01', DATE)).group_by(
        models.Meta.clean_collection_date, models.Meta.clean_country, models.LineageDef.variant_id)
    return stmt.offset(skip).limit(limit).all()


def get_variants_weekly(db: Session, skip: int = 0, limit: int = 100) -> List[models.VariantsWeekly]:
    stmt = db.query(case([(models.Meta.clean_country == 'USA', "'United States'")],
                         else_=models.Meta.clean_country).label('clean_country').label('country_name'),
                    models.Meta.date_isoyear, models.Meta.date_isoweek, models.LineageDef.variant_id,
                    func.count('*').label('n')).filter(models.Meta.clean_host == 'Homo sapiens'
                                                       ).join(models.LineageDef,
                                                              models.Meta.ena_run == models.LineageDef.variant_id).filter(
        models.Meta.collection_date is not None).filter(func.DATE(models.Meta.clean_collection_date) > cast(
        '2020-03-15', DATE)).group_by(models.Meta.clean_country, models.Meta.date_isoyear, models.Meta.date_isoweek,
                                      models.LineageDef.variant_id)
    return stmt.offset(skip).limit(limit).all()
