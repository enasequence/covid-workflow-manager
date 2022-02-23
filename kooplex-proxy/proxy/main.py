from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

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


@app.get("/covid_country_weekly/", response_model=List[schemas.CovidCountryWeekly])
def read_covid_country_weekly(skip: int = 0, limit: int = 100):
    covid_country_weekly = crud.get_covid_country_weekly(next(get_db()), skip=skip, limit=limit)
    return covid_country_weekly


@app.get("/unique_vcf_append/", response_model=List[schemas.UniqueVCFAppend])
def read_unique_vcf_append(skip: int = 0, limit: int = 100):
    unique_vcf_append = crud.get_unique_vcf_append(next(get_db()), skip=skip, limit=limit)
    return unique_vcf_append


@app.get("/vcf_all/", response_model=List[schemas.VCFAll])
def read_vcf_all(skip: int = 0, limit: int = 100):
    vcf_all = crud.get_vcf_all(next(get_db()), skip=skip, limit=limit)
    return vcf_all


@app.get("/cov/", response_model=List[schemas.Cov])
def read_cov(skip: int = 0, limit: int = 100):
    cov = crud.get_cov(next(get_db()), skip=skip, limit=limit)
    return cov


@app.get("/meta/", response_model=List[schemas.Meta])
def read_meta(skip: int = 0, limit: int = 100):
    meta = crud.get_meta(next(get_db()), skip=skip, limit=limit)
    return meta


@app.get("/unique_cov_append/", response_model=List[schemas.UniqueCovAppend])
def read_unique_cov_append(skip: int = 0, limit: int = 100):
    unique_cov_append = crud.get_unique_cov_append(next(get_db()), skip=skip, limit=limit)
    return unique_cov_append


@app.get("/lineage_def/", response_model=List[schemas.LineageDef])
def read_lineage_def(skip: int = 0, limit: int = 100):
    lineage_def = crud.get_lineage_def(next(get_db()), skip=skip, limit=limit)
    return lineage_def


@app.get("/operation/", response_model=List[schemas.Operation])
def read_operation(skip: int = 0, limit: int = 100):
    operation = crud.get_operation(next(get_db()), skip=skip, limit=limit)
    return operation


@app.get("/unique_cov/", response_model=List[schemas.UniqueCov])
def read_unique_cov(skip: int = 0, limit: int = 100):
    unique_cov = crud.get_unique_cov(next(get_db()), skip=skip, limit=limit)
    return unique_cov


@app.get("/unique_vcf/", response_model=List[schemas.UniqueVCF])
def read_unique_vcf(skip: int = 0, limit: int = 100):
    unique_vcf = crud.get_unique_vcf(next(get_db()), skip=skip, limit=limit)
    return unique_vcf


@app.get("/vcf_all_append/", response_model=List[schemas.VCFAllAppend])
def read_vcf_all_append(skip: int = 0, limit: int = 100):
    vcf_all_append = crud.get_vcf_all_append(next(get_db()), skip=skip, limit=limit)
    return vcf_all_append


@app.get("/new_cases/", response_model=List[schemas.NewCases])
def read_new_cases(skip: int = 0, limit: int = 100):
    new_cases = crud.get_new_cases(next(get_db()), skip=skip, limit=limit)
    return new_cases


@app.get("/worldplot_data/", response_model=List[schemas.NewCases])
def read_worldplot_data(skip: int = 0, limit: int = 100):
    worldplot_data = crud.get_worldplot_data(next(get_db()), skip=skip, limit=limit)
    return worldplot_data
