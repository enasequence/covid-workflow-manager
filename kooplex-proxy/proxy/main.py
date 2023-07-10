from typing import List

from fastapi import FastAPI, HTTPException

import crud
import schemas
from database import ALLOWED_SCHEMAS, POSTGRES_SCHEMA_KEY

from models import db_connect

app = FastAPI(openapi_prefix="/api")


# Dependency
def get_schema_name(schema_key):
    if not schema_key:
        schema_key = POSTGRES_SCHEMA_KEY
    elif schema_key not in ALLOWED_SCHEMAS:
        keys = '/'.join(list(ALLOWED_SCHEMAS.keys()))
        print(f"This schema key '{schema_key}' is "
              f"unavailable for using, please "
              f"use one of these schema keys: {keys}")
        return None

    schema_name = ALLOWED_SCHEMAS[schema_key]
    return schema_name


def get_db(schema_name):

    if schema_name is None:
        raise HTTPException(status_code=500,
                            detail=f"Schema name is empty")

    global db_connect
    obj = db_connect.connect(schema_name=schema_name)
    db = obj()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/country_samples/", response_model=List[schemas.MView_CountrySamples])
def read_country_samples(schema_key='', skip: int = 0, limit: int = 100):
    db = get_db(get_schema_name(schema_key))
    country_samples = crud.get_country_samples(next(db), skip=skip, limit=limit)
    return country_samples


@app.get("/human_meta_mv/", response_model=List[schemas.MView_HumanMetaMv])
def read_human_meta_mv(schema_key='', skip: int = 0, limit: int = 100):
    db = get_db(get_schema_name(schema_key))
    meta = crud.get_human_meta_mv(next(db), skip=skip, limit=limit)
    return meta


@app.get("/human_meta_mv_jhd/", response_model=List[schemas.MView_HumanMetaMvJhd])
def read_human_meta_mv_jhd(schema_key='', skip: int = 0, limit: int = 100):
    db = get_db(get_schema_name(schema_key))
    meta = crud.get_human_meta_mv_jhd(next(db), skip=skip, limit=limit)
    return meta


@app.get("/lineage_def/", response_model=List[schemas.Table_LineageDef])
def read_lineage_def(schema_key='', skip: int = 0, limit: int = 100):
    db = get_db(get_schema_name(schema_key))
    lineage_def = crud.get_lineage_def(next(db), skip=skip, limit=limit)
    return lineage_def


@app.get("/lineage/", response_model=List[schemas.MView_Lineage])
def read_lineage(schema_key='', skip: int = 0, limit: int = 100):
    db = get_db(get_schema_name(schema_key))
    lineage = crud.get_lineage(next(db), skip=skip, limit=limit)
    return lineage


@app.get("/new_cases_jhd/", response_model=List[schemas.MView_NewCasesJhd])
def read_new_cases_jhd(schema_key='', skip: int = 0, limit: int = 100):
    db = get_db(get_schema_name(schema_key))
    new_cases = crud.get_new_cases_jhd(next(db), skip=skip, limit=limit)
    return new_cases


@app.get("/variants_weekly/", response_model=List[schemas.MView_VariantsWeekly])
def read_variants_weekly(schema_key='', skip: int = 0, limit: int = 100):
    db = get_db(get_schema_name(schema_key))
    variants_weekly = crud.get_variants_weekly(next(db), skip=skip, limit=limit)
    return variants_weekly


@app.get("/unique_ena_run_summary/", response_model=List[schemas.MView_UniqueEnaRunSum])
def read_unique_ena_run_sum(schema_key='', skip: int = 0, limit: int = 100):
    db = get_db(get_schema_name(schema_key))
    unique_ena_run_sum = crud.get_unique_ena_run_summary(
        next(db), skip=skip, limit=limit
    )
    return unique_ena_run_sum


@app.get("/filter_custom_browser_cov/", response_model=List[schemas.SProc_FilterCustomBrowserCov])
def filter_custom_browser_cov(included: str, excluded: str, schema_key='', skip: int = 0, limit: int = 100):
    schema_name = get_schema_name(schema_key)

    custom_browser_cov = crud.filter_custom_browser_cov(
        schema=schema_name, included=included, excluded=excluded, skip=skip, limit=limit
    )
    custom_browser_cov = [
        schemas.SProc_FilterCustomBrowserCov(country=item[0], count=item[1]) for item in custom_browser_cov
    ]

    return custom_browser_cov


@app.get("/filter_custom_browser_cov_time/", response_model=List[schemas.SProc_FilterCustomBrowserCovTime])
def filter_custom_browser_cov_time(included: str, excluded: str, schema_key='', skip: int = 0, limit: int = 100):
    schema_name = get_schema_name(schema_key)

    custom_browser_cov = crud.filter_custom_browser_cov_time(
        schema=schema_name, included=included, excluded=excluded, skip=skip, limit=limit
    )

    custom_browser_cov = [
        schemas.SProc_FilterCustomBrowserCovTime(
            collection_date=item[0], country=item[1], other_count=item[2], variant_count=item[3]
        ) for item in custom_browser_cov
    ]

    return custom_browser_cov


@app.get("/filter_custom_browser/", response_model=List[schemas.SProc_FilterCustomBrowser])
def filter_custom_browser_cov(included: str, excluded: str, schema_key='', skip: int = 0, limit: int = 100):
    schema_name = get_schema_name(schema_key)

    custom_browser_cov = crud.filter_custom_browser(
        schema=schema_name, included=included, excluded=excluded, skip=skip, limit=limit
    )
    custom_browser_cov = [
        schemas.SProc_FilterCustomBrowser(country=item[0], count=item[1]) for item in custom_browser_cov
    ]

    return custom_browser_cov


@app.get("/filter_custom_browser_time/", response_model=List[schemas.SProc_FilterCustomBrowserTime])
def filter_custom_browser_cov_time(included: str, excluded: str, schema_key='', skip: int = 0, limit: int = 100):
    schema_name = get_schema_name(schema_key)

    custom_browser_cov = crud.filter_custom_browser_time(
        schema=schema_name, included=included, excluded=excluded, skip=skip, limit=limit
    )

    custom_browser_cov = [
        schemas.SProc_FilterCustomBrowserTime(
            collection_date=item[0], country=item[1], other_count=item[2], variant_count=item[3]
        ) for item in custom_browser_cov
    ]

    return custom_browser_cov
