from sqlalchemy.orm import Session
from sqlalchemy import func
import re
from dateutil.parser import parse

import models
from database import engine


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


def get_covid_country_weekly(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.CovidCountryWeekly).offset(skip).all()
    else:
        return db.query(models.CovidCountryWeekly).offset(skip).limit(limit).all()


def get_vcf_all(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.VCFAll).offset(skip).all()
    else:
        return db.query(models.VCFAll).offset(skip).limit(limit).all()


def get_cov(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.Cov).offset(skip).all()
    else:
        return db.query(models.Cov).offset(skip).limit(limit).all()


def get_meta(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.Meta).offset(skip).all()
    else:
        return db.query(models.Meta).offset(skip).limit(limit).all()


def get_sorted_meta(db: Session, text_request: str = '', skip: int = 0, limit: int = 100):
    print(f"Current text_request is: {text_request}\n")
    sql_request = ' '
    if len(text_request) != 0:
        text_request_spl = text_request.split('&')

        sql_request_spl = list()

        for el in text_request_spl:
            print(f"Current text_request element is: {el}\n")
            outp = list(re.findall('\s*(\w+)\s*([!==<=>=]+)\s*(\'.*\')', el)[0])
            if is_date(outp[2]) is True:
                outp[2] = f'CAST({outp[2]} AS DATE)'
            sql_request_spl.append(' '.join(outp))

        sql_request = ' ' + 'AND ' + ' AND '.join(sql_request_spl) + ' '

    if limit == -1:
        limit = 'NULL'

    final_request = f"SELECT * FROM meta WHERE (NOT((clean_country) IS NULL)){sql_request}ORDER BY " \
                    f"clean_collection_date, clean_country, clean_host OFFSET {skip} LIMIT {limit};"

    print(f"Your request is: {final_request}\n")

    with engine.connect() as conn:
        outp = conn.execute(final_request).all()
    return outp


def get_lineage_def(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.LineageDef).offset(skip).all()
    else:
        return db.query(models.LineageDef).offset(skip).limit(limit).all()


def get_unique_cov(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.UniqueCov).offset(skip).all()
    else:
        return db.query(models.UniqueCov).offset(skip).limit(limit).all()


def get_unique_vcf(db: Session, skip: int = 0, limit: int = 100):
    if limit == -1:
        return db.query(models.UniqueVCF).offset(skip).all()
    else:
        return db.query(models.UniqueVCF).offset(skip).limit(limit).all()


def get_country_samples(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_country_samples OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_lineage_def_description(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_lineage_def_description OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_lineage(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_lineage OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_new_cases(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_new_cases OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_variants_weekly(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_variants_weekly OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_worldplot_data(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM app_worldplot_data OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_table_description(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM table_description OFFSET {skip} LIMIT {limit};""").all()
    return outp


def get_column_description(skip: int = 0, limit: int = 100):
    if limit == -1:
        limit = 'NULL'
    with engine.connect() as conn:
        outp = conn.execute(f"""SELECT * FROM column_description OFFSET {skip} LIMIT {limit};""").all()
    return outp
