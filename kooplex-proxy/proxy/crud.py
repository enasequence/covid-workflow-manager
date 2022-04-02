from sqlalchemy.orm import Session
from sqlalchemy.sql import text

import models
from database import engine

import getpass


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


def get_new_cases(skip: int = 0, limit: int = 100):

    text_request = text("""CREATE OR REPLACE VIEW app_new_cases_view AS
        WITH tmp_meta1 as (
            SELECT "ena_run", CASE WHEN ("clean_country" = 'USA') THEN ('United States') WHEN NOT("clean_country" = 'USA') 
            THEN ("clean_country") END AS "country_name", "clean_collection_date", "date_isoyear" AS "date_year", 
            "date_isoweek" AS "date_week"
            FROM meta
            WHERE NOT ("clean_collection_date" IS NULL)
            AND "clean_host" = 'Homo sapiens'
            AND "clean_collection_date" > CAST('2020-03-15' AS DATE) 
        )
        , tmp_grouped as (
            SELECT "country_name", "date_year", "date_week", COUNT(*) AS "weekly_sample"
            FROM tmp_meta1
            GROUP BY "country_name", "date_year", "date_week"
        )
        SELECT "LHS"."country_name" AS "country_name", "LHS"."date_year" AS "date_year", "LHS"."date_week" AS "date_week", 
        "LHS"."weekly_sample" AS "weekly_sample", "RHS"."iso_a3" AS "iso_a3", "RHS"."iso_a2" AS "iso_a2", 
        "RHS"."country_name_local" AS "country_name_local", "RHS"."population" AS "population", 
        "RHS"."ecdc_covid_country_weekly_cases" AS "ecdc_covid_country_weekly_cases", 
        "RHS"."ecdc_covid_country_weekly_deaths" AS "ecdc_covid_country_weekly_deaths"
        FROM tmp_grouped as "LHS"
        LEFT JOIN "ecdc_covid_country_weekly" AS "RHS"
        ON ("LHS"."country_name" = "RHS"."country_name" AND "LHS"."date_year" = "RHS"."date_year" AND 
        "LHS"."date_week" = "RHS"."date_week");""")

    with engine.connect() as conn:
        conn.execute(text_request)
        outp = conn.execute(f"""SELECT * FROM app_new_cases_view OFFSET {skip} LIMIT {limit};""").all()
        conn.execute("""DROP VIEW app_new_cases_view;""")

    return outp


def get_worldplot_data(skip: int = 0, limit: int = 100):

    text_request = text("""CREATE OR REPLACE VIEW app_worldplot_data_view AS
        WITH tmp_meta1 as (
            SELECT "ena_run", CASE WHEN ("clean_country" = 'USA') THEN ('United States') WHEN 
            NOT("clean_country" = 'USA') THEN ("clean_country") END AS "Country", "clean_collection_date", 
            "date_isoyear" AS "date_year", "date_isoweek" AS "date_week"
            FROM meta
            WHERE NOT ("clean_collection_date" IS NULL)
            AND NOT ("clean_country" IS NULL)
            AND "clean_host" = 'Homo sapiens'
            AND "clean_collection_date" > CAST('2020-03-15' AS DATE)
            AND "clean_collection_date" < CURRENT_DATE
        ) 
        SELECT "Country", "date_year", "date_week", COUNT(*) AS "weekly_sample"
        FROM tmp_meta1
        GROUP BY "Country", "date_year", "date_week";""")

    with engine.connect() as conn:
        conn.execute(text_request)
        outp = conn.execute(f"""SELECT * FROM app_worldplot_data_view OFFSET {skip} LIMIT {limit};""").all()
        conn.execute("""DROP VIEW app_worldplot_data_view;""")

    return outp
