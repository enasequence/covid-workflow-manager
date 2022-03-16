from sqlalchemy.orm import Session
from sqlalchemy import case, func
from sqlalchemy.sql import alias
from sqlalchemy.orm import load_only
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


def get_new_cases(db: Session, skip: int = 0, limit: int = 100):

    expr = case([(models.Meta.clean_country == 'USA', 'United States'), ],
               else_=models.Meta.clean_country).label("clean_country")
    result_filter = db.query(models.Meta, expr).filter(
        models.Meta.clean_collection_date.isnot(None),
        models.Meta.clean_host == 'Homo sapiens',
        models.Meta.clean_collection_date > func.date('2020-03-15')
    )

    result_count = db.query(
        models.Meta.country_name,
        models.Meta.date_year,
        models.Meta.date_week,
        func.count('*').label('weekly_sample')
    ).select_from(alias(result_filter))

    result_groupby = db.query(
        models.Meta
    ).group_by(
        models.Meta.country_name,
        models.Meta.date_year,
        models.Meta.date_week
    ).select_from(alias(result_count))

    lhs, rhs = aliased(result_groupby), aliased(result_filter)

    result = outerjoin(
        lhs, lhs.country_name == rhs.country_name
    ).outerjoin(lhs, lhs.date_year == rhs.date_year).outerjoin(lhs, lhs.date_week == rhs.date_week)

    return result.offset(skip).limit(limit).all()


def get_worldplot_data(db: Session, skip: int = 0, limit: int = 100):

    expr = case([(models.Meta.clean_country == 'USA', 'United States'), ],
                else_=models.Meta.clean_country).label("clean_country")
    result_filter = db.query(models.Meta, expr).filter(
        models.Meta.clean_collection_date.isnot(None),
        models.Meta.clean_host == 'Homo sapiens',
        models.Meta.clean_collection_date > func.date('2020-03-15'),
        models.Meta.clean_collection_date < func.current_date())

    result_count = db.query(
        models.Meta.country_name,
        models.Meta.date_year,
        models.Meta.date_week,
        func.count('*').label('weekly_sample')
    ).select_from(alias(result_filter))

    result = db.query(
        models.Meta
    ).group_by(
        models.Meta.country_name,
        models.Meta.date_year,
        models.Meta.date_week
    ).select_from(alias(result_count))

    return result.offset(skip).limit(limit).all()
