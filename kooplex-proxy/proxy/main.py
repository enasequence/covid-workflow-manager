from typing import List

from fastapi import FastAPI

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(openapi_prefix="/api")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/country_samples/", response_model=List[schemas.MView_CountrySamples])
def read_country_samples(schema_key='', skip: int = 0, limit: int = 100):
    country_samples = crud.get_country_samples(next(get_db()), endp_schema_key=schema_key, skip=skip, limit=limit)
    return country_samples


@app.get("/human_meta_mv/", response_model=List[schemas.MView_HumanMetaMv])
def read_human_meta_mv(schema_key='', skip: int = 0, limit: int = 100):
    meta = crud.get_human_meta_mv(next(get_db()), endp_schema_key=schema_key, skip=skip, limit=limit)
    return meta


@app.get("/human_meta_mv_jhd/", response_model=List[schemas.MView_HumanMetaMvJhd])
def read_human_meta_mv_jhd(schema_key='', skip: int = 0, limit: int = 100):
    meta = crud.get_human_meta_mv_jhd(next(get_db()), endp_schema_key=schema_key, skip=skip, limit=limit)
    return meta


@app.get("/lineage_def/", response_model=List[schemas.Table_LineageDef])
def read_lineage_def(schema_key='', skip: int = 0, limit: int = 100):
    lineage_def = crud.get_lineage_def(next(get_db()), endp_schema_key=schema_key, skip=skip, limit=limit)
    return lineage_def


@app.get("/lineage/", response_model=List[schemas.MView_Lineage])
def read_lineage(schema_key='', skip: int = 0, limit: int = 100):
    lineage = crud.get_lineage(next(get_db()), endp_schema_key=schema_key, skip=skip, limit=limit)
    return lineage


@app.get("/new_cases_jhd/", response_model=List[schemas.MView_NewCasesJhd])
def read_new_cases_jhd(schema_key='', skip: int = 0, limit: int = 100):
    new_cases = crud.get_new_cases_jhd(next(get_db()), endp_schema_key=schema_key, skip=skip, limit=limit)
    return new_cases


@app.get("/variants_weekly/", response_model=List[schemas.MView_VariantsWeekly])
def read_variants_weekly(schema_key='', skip: int = 0, limit: int = 100):
    variants_weekly = crud.get_variants_weekly(next(get_db()), endp_schema_key=schema_key, skip=skip, limit=limit)
    return variants_weekly


@app.get("/unique_ena_run_summary/", response_model=List[schemas.MView_UniqueEnaRunSum])
def read_unique_ena_run_sum(schema_key='', skip: int = 0, limit: int = 100):
    unique_ena_run_sum = crud.get_unique_ena_run_summary(
        next(get_db()), endp_schema_key=schema_key, skip=skip, limit=limit
    )
    return unique_ena_run_sum


@app.get("/filter_custom_browser_cov/", response_model=List[schemas.SProc_FilterCustomBrowserCov])
def filter_custom_browser_cov(included: str, excluded: str, schema_key='', skip: int = 0, limit: int = 100):
    custom_browser_cov = crud.filter_custom_browser_cov(
        next(get_db()), included=included, excluded=excluded, endp_schema_key=schema_key, skip=skip, limit=limit
    )
    return custom_browser_cov


@app.get("/filter_custom_browser_cov_time/", response_model=List[schemas.SProc_FilterCustomBrowserCovTime])
def filter_custom_browser_cov_time(included: str, excluded: str, schema_key='', skip: int = 0, limit: int = 100):
    custom_browser_cov_time = crud.filter_custom_browser_cov_time(
        next(get_db()), included=included, excluded=excluded, endp_schema_key=schema_key, skip=skip, limit=limit
    )
    return custom_browser_cov_time


@app.get("/table_count/", response_model=List[schemas.Table_Count])
def table_count(table_name, schema_key=''):
    table_count_result = crud.table_count(next(get_db()), table_name=table_name, endp_schema_key=schema_key)
    return table_count_result
