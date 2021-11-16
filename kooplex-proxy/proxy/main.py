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
def read_covid_country_weekly(skip: int = 0, limit: int = 100,
                              db: Session = Depends(get_db)):
    covid_country_weekly = crud.get_covid_country_weekly(db, skip=skip,
                                                         limit=limit)
    return covid_country_weekly


@app.get("/vcf_all/", response_model=List[schemas.VCFAll])
def read_vcf_all(skip: int = 0, limit: int = 100,
                 db: Session = Depends(get_db)):
    vcf_all = crud.get_vcf_all(db, skip=skip, limit=limit)
    return vcf_all


@app.get("/cov/", response_model=List[schemas.Cov])
def read_cov(skip: int = 0, limit: int = 100,
             db: Session = Depends(get_db)):
    cov = crud.get_cov(db, skip=skip, limit=limit)
    return cov


@app.get("/meta/", response_model=List[schemas.Meta])
def read_meta(skip: int = 0, limit: int = 100,
              db: Session = Depends(get_db)):
    meta = crud.get_meta(db, skip=skip, limit=limit)
    return meta


@app.get("/lineage_def/", response_model=List[schemas.LineageDef])
def read_lineage_def(skip: int = 0, limit: int = 100,
                     db: Session = Depends(get_db)):
    lineage_def = crud.get_lineage_def(db, skip=skip, limit=limit)
    return lineage_def


@app.get("/operation/", response_model=List[schemas.Operation])
def read_operation(skip: int = 0, limit: int = 100,
                   db: Session = Depends(get_db)):
    operation = crud.get_operation(db, skip=skip, limit=limit)
    return operation


@app.get("/unique_cov/", response_model=List[schemas.UniqueCov])
def read_unique_cov(skip: int = 0, limit: int = 100,
                    db: Session = Depends(get_db)):
    unique_cov = crud.get_unique_cov(db, skip=skip, limit=limit)
    return unique_cov


@app.get("/unique_vcf/", response_model=List[schemas.UniqueVCF])
def read_unique_vcf(skip: int = 0, limit: int = 100,
                    db: Session = Depends(get_db)):
    unique_vcf = crud.get_unique_vcf(db, skip=skip, limit=limit)
    return unique_vcf


@app.get("/country_samples/", response_model=List[schemas.CountrySamples])
def read_country_samples(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_country_samples(db, skip=skip, limit=limit)


@app.get("/get-lineage_def/", response_model=List[schemas.LineageDefSelectedFields])
def read_lineage_def_some_fields(skip: int = 0, limit: int = 100,
                                 db: Session = Depends(get_db)):
    lineage_def_some_fields = crud.get_lineage_def_some_fields(db, skip=skip, limit=limit)
    return lineage_def_some_fields


@app.get("/get-lineage0/", response_model=List[schemas.Lineage0])
def read_lineage0(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lineage0 = crud.get_lineage0(db, skip=skip, limit=limit)
    return lineage0


@app.get("/get-lineage/", response_model=List[schemas.Lineage])
def read_lineage(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lineage = crud.get_lineage(db, skip=skip, limit=limit)
    return lineage


@app.get("/variants_weekly/", response_model=List[schemas.VariantsWeekly])
def read_variants_weekly(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lineage = crud.get_variants_weekly(db, skip=skip, limit=limit)
    return lineage


@app.get("/unique_ena_run_summary/", response_model=List[schemas.UniqueEnaRunSummary])
def read_unique_ena_run_summary(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    unique_ena_run_summary = crud.get_unique_ena_run_summary(db, skip=skip, limit=limit)
    return unique_ena_run_summary


@app.get("/lineage/", response_model=List[schemas.LineageView])
def read_lineage(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lineage = crud.get_lineage_view(db, skip=skip, limit=limit)
    return lineage


@app.get("/ebi_weekly_samples/", response_model=List[schemas.EbiWeeklySamples])
def read_ebi_weekly_samples(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ebi_weekly_samples = crud.get_ebi_weekly_samples(db, skip=skip, limit=limit)
    return ebi_weekly_samples
