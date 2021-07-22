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


@app.get("/covid_country_weekly/", response_model=List[
    schemas.CovidCountryWeekly])
def read_covid_country_weekly(db: Session = Depends(get_db)):
    covid_country_weekly = crud.get_covid_country_weekly(db)
    return covid_country_weekly


@app.get("/unique_vcf_append/", response_model=List[schemas.UniqueVCFAppend])
def read_unique_vcf_append(db: Session = Depends(get_db)):
    unique_vcf_append = crud.get_unique_vcf_append(db)
    return unique_vcf_append


@app.get("/vcf_all/", response_model=List[schemas.VCFAll])
def read_vcf_all(db: Session = Depends(get_db)):
    vcf_all = crud.get_vcf_all(db)
    return vcf_all


@app.get("/cov/", response_model=List[schemas.Cov])
def read_cov(db: Session = Depends(get_db)):
    cov = crud.get_cov(db)
    return cov


@app.get("/meta/", response_model=List[schemas.Meta])
def read_meta(db: Session = Depends(get_db)):
    meta = crud.get_meta(db)
    return meta


@app.get("/unique_cov_append/", response_model=List[schemas.UniqueCovAppend])
def read_unique_cov_append(db: Session = Depends(get_db)):
    unique_cov_append = crud.get_unique_cov_append(db)
    return unique_cov_append


@app.get("/lineage_def/", response_model=List[schemas.LineageDef])
def read_lineage_def(db: Session = Depends(get_db)):
    lineage_def = crud.get_lineage_def(db)
    return lineage_def


@app.get("/operation/", response_model=List[schemas.Operation])
def read_operation(db: Session = Depends(get_db)):
    operation = crud.get_operation(db)
    return operation


@app.get("/unique_cov/", response_model=List[schemas.UniqueCov])
def read_unique_cov(db: Session = Depends(get_db)):
    unique_cov = crud.get_unique_cov(db)
    return unique_cov


@app.get("/unique_vcf/", response_model=List[schemas.UniqueVCF])
def read_unique_vcf(db: Session = Depends(get_db)):
    unique_vcf = crud.get_unique_vcf(db)
    return unique_vcf


@app.get("/vcf_all_append/", response_model=List[schemas.VCFAllAppend])
def read_vcf_all_append(db: Session = Depends(get_db)):
    vcf_all_append = crud.get_vcf_all_append(db)
    return vcf_all_append
