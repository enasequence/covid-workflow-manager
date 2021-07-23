from sqlalchemy import null, func, select
from sqlalchemy.orm import Session

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


def get_country_samples(db: Session):
    stmt = select(models.Meta.clean_country, func.count()).select_from(
        select(models.Meta).select_from(models.Meta)).groupby(
        models.Meta.clean_country)
    return db.execute(stmt)


def get_lineage_def_some_fields(db: Session):
    return db.query(models.LineageDefSelectedFields).all()


def new_cases(db: Session):
    db.execute('SELECT clean_collection_date, clean_country, variant_id, COUNT(*) AS n'
               'FROM (SELECT ena_run, collection_date, clean_country, clean_collection_date,variant_id'
               'FROM (SELECT LHS.ena_run AS ena_run, LHS.collection_date AS collection_date, LHS.clean_country AS clean_country, LHS.clean_collection_date AS clean_collection_date, RHS.variant_id AS variant_id, RHS.n AS n, RHS.required_mutation AS required_mutation'
               'FROM (SELECT ena_run, collection_date, clean_country, clean_collection_date'
               'FROM (SELECT *'
               'FROM (SELECT ena_run, collection_date, CASE WHEN (clean_country = USA) THEN (United States) WHEN NOT(clean_country = USA) '
               'THEN (clean_country) END AS clean_country, clean_host, accession, sample_accession, experiment_accession, study_accession, description, country, first_created, first_public, host, host_sex, host_tax_id, host_body_site, bio_material, culture_collection, '
               'instrument_model, instrument_platform, library_layout, library_name, library_selection, library_source, library_strategy, sequencing_method, isolate, strain, base_count, collected_by, broker_name, center_name, sample_capture_status, fastq_ftp, collection_date_submitted, '
               'checklist, clean_collection_date, date_isoweek, date_isoyear'
               'FROM meta) "dbplyr_359"'
               'WHERE (NOT(((clean_collection_date) IS NULL)))) "dbplyr_360"'
               'WHERE (clean_host = Homo sapiens)) LHS'
               'INNER JOIN lineage AS RHS'
               'ON (LHS.ena_run = RHS.ena_run) ) "dbplyr_361") "dbplyr_362"'
               'WHERE (clean_collection_date > CAST(2020-01-01 AS DATE)) GROUP BY clean_collection_date, clean_country, variant_id')
