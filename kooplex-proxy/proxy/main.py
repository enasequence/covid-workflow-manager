from typing import List

from fastapi import FastAPI, Depends

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


@app.get("/sorted_meta/", response_model=List[schemas.Meta])
def read_sorted_meta(text_request: str = '', skip: int = 0, limit: int = 100):
    meta = crud.get_sorted_meta(next(get_db()), text_request=text_request, skip=skip, limit=limit)
    return meta


@app.get("/lineage_def/", response_model=List[schemas.LineageDef])
def read_lineage_def(skip: int = 0, limit: int = 100):
    lineage_def = crud.get_lineage_def(next(get_db()), skip=skip, limit=limit)
    return lineage_def


@app.get("/unique_cov/", response_model=List[schemas.UniqueCov])
def read_unique_cov(skip: int = 0, limit: int = 100):
    unique_cov = crud.get_unique_cov(next(get_db()), skip=skip, limit=limit)
    return unique_cov


@app.get("/unique_vcf/", response_model=List[schemas.UniqueVCF])
def read_unique_vcf(skip: int = 0, limit: int = 100):
    unique_vcf = crud.get_unique_vcf(next(get_db()), skip=skip, limit=limit)
    return unique_vcf


@app.get("/country_samples/", response_model=List[schemas.CountrySamples])
def read_country_samples(skip: int = 0, limit: int = 100):
    country_samples = crud.get_country_samples(skip=skip, limit=limit)
    return country_samples


@app.get("/lineage_def_description/", response_model=List[schemas.LineageDefDesc])
def read_lineage_def_description(skip: int = 0, limit: int = 100):
    lineage_def_description = crud.get_lineage_def_description(skip=skip, limit=limit)
    return lineage_def_description


@app.get("/lineage/", response_model=List[schemas.Lineage])
def read_lineage(skip: int = 0, limit: int = 100):
    lineage = crud.get_lineage(skip=skip, limit=limit)
    return lineage


@app.get("/new_cases/", response_model=List[schemas.NewCases])
def read_new_cases(skip: int = 0, limit: int = 100):
    new_cases = crud.get_new_cases(skip=skip, limit=limit)
    return new_cases


@app.get("/variants_weekly/", response_model=List[schemas.VariantsWeekly])
def read_variants_weekly(skip: int = 0, limit: int = 100):
    variants_weekly = crud.get_variants_weekly(skip=skip, limit=limit)
    return variants_weekly


@app.get("/worldplot_data/", response_model=List[schemas.WorldplotData])
def read_worldplot_data(skip: int = 0, limit: int = 100):
    worldplot_data = crud.get_worldplot_data(skip=skip, limit=limit)
    return worldplot_data


@app.get("/table_description/", response_model=List[schemas.TableDescription])
def read_table_description(skip: int = 0, limit: int = 100):
    table_description = crud.get_table_description(skip=skip, limit=limit)
    return table_description


@app.get("/column_description/", response_model=List[schemas.ColumnDescription])
def read_column_description(skip: int = 0, limit: int = 100):
    column_description = crud.get_column_description(skip=skip, limit=limit)
    return column_description
