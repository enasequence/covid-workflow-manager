from sqlalchemy.orm import Session
import models


def get_covid_country_weekly(db: Session):
    return db.query(models.CovidCountryWeekly).all()


def get_unique_vcf_append(db: Session):
    return db.query(models.UniqueVCFAppend).all()


def get_vcf_all(db: Session):
    return db.query(models.VCFAll).all()


def get_cov(db: Session):
    return db.query(models.Cov).all()


def get_meta(db: Session):
    return db.query(models.Meta).all()


def get_unique_cov_append(db: Session):
    return db.query(models.UniqueCovAppend).all()


def get_lineage_def(db: Session):
    return db.query(models.LineageDef).all()


def get_operation(db: Session):
    return db.query(models.Operation).all()


def get_unique_cov(db: Session):
    return db.query(models.UniqueCov).all()


def get_unique_vcf(db: Session):
    return db.query(models.UniqueVCF).all()


def get_vcf_all_append(db: Session):
    return db.query(models.VCFAllAppend).all()
