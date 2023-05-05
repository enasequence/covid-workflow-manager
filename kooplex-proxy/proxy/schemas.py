from datetime import date

from pydantic import BaseModel
from typing import Optional


class MView_CountrySamples(BaseModel):
    country: Optional[str]
    n_sample: Optional[int]
    log_n_sample: Optional[float]
    relative_n_sample: Optional[float]
    relative_log_n_sample: Optional[float]

    class Config:
        orm_mode = True


class MView_HumanMetaMv(BaseModel):
    country_name: Optional[str]
    date: Optional[date]
    date_year: Optional[float]
    date_week: Optional[float]
    weekly_sample: Optional[int]

    class Config:
        orm_mode = True


class MView_HumanMetaMvJhd(BaseModel):
    country_name: Optional[str]
    date: Optional[date]
    date_year: Optional[float]
    date_week: Optional[float]
    weekly_sample: Optional[int]
    cases: Optional[int]
    pct: Optional[int]

    class Config:
        orm_mode = True


class Table_LineageDef(BaseModel):
    variant_id: Optional[str]
    pango: Optional[str]
    type_variant: Optional[str]
    amino_acid_change: Optional[str]
    protein_codon_position: Optional[float]
    ref_protein: Optional[str]
    alt_protein: Optional[str]
    gene: Optional[str]
    effect: Optional[str]
    snpeff_original_mut: Optional[str]
    ref_pos_alt: Optional[str]
    ref: Optional[str]
    alt: Optional[str]
    pos: Optional[float]
    description: Optional[str]

    class Config:
        orm_mode = True


class MView_Lineage(BaseModel):
    collection_date: Optional[date]
    country: Optional[str]
    variant_id: Optional[str]
    n: Optional[int]
    n_all: Optional[int]
    pct: Optional[float]

    class Config:
        orm_mode = True


class MView_NewCasesJhd(BaseModel):
    country_name: Optional[str]
    date: Optional[date]
    date_year: Optional[float]
    date_week: Optional[float]
    weekly_sample: Optional[int]
    cases: Optional[int]

    class Config:
        orm_mode = True


class MView_VariantsWeekly(BaseModel):
    country_name: Optional[str]
    date_year: Optional[float]
    date_week: Optional[float]
    variant_id: Optional[str]
    weekly_variant_sample: Optional[int]

    class Config:
        orm_mode = True


class MView_UniqueEnaRunSum(BaseModel):
    table_name: Optional[str]
    count: Optional[int]

    class Config:
        orm_mode = True


class SProc_FilterCustomBrowserCov(BaseModel):
    country: Optional[str]
    count: Optional[int]

    class Config:
        orm_mode = True


class SProc_FilterCustomBrowserCovTime(BaseModel):
    collection_date: Optional[date]
    country: Optional[str]
    other_count: Optional[int]
    variant_count: Optional[int]

    class Config:
        orm_mode = True


class Table_Count(BaseModel):
    count: Optional[int]

    class Config:
        orm_mode = True
