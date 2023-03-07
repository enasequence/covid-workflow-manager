from sqlalchemy.orm import Session
from sqlalchemy import text

import models
from database import engine


def get_country_samples(db: Session, skip: int = 0, limit: int = 100):
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
