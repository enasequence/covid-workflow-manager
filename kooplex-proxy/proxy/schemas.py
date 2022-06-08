from datetime import date

from pydantic import BaseModel
from typing import Optional


class CovidCountryWeekly(BaseModel):
    iso_a3: Optional[str]
    iso_a2: Optional[str]
    country_name: Optional[str]
    country_name_local: Optional[str]
    date_year: Optional[float]
    date_week: Optional[float]
    ecdc_covid_country_weekly_cases: Optional[float]
    ecdc_covid_country_weekly_deaths: Optional[float]

    class Config:
        orm_mode = True


class VCFAll(BaseModel):
    ena_run: Optional[str]
    chrom: Optional[str]
    pos: Optional[int]
    ref: Optional[str]
    alt: Optional[str]
    qual: Optional[int]
    filter: Optional[str]
    dp: Optional[int]
    af: Optional[float]
    sb: Optional[int]
    count_ref_forward_base: Optional[int]
    count_ref_reverse_base: Optional[int]
    count_alt_forward_base: Optional[int]
    count_alt_reverse_base: Optional[int]
    hrun: Optional[int]
    indel: Optional[bool]
    lof: Optional[str]
    nmd: Optional[str]
    ann_num: Optional[int]
    annotation: Optional[str]
    annotation_impact: Optional[str]
    gene_name: Optional[str]
    gene_id: Optional[str]
    feature_type: Optional[str]
    feature_id: Optional[str]
    transcript_biotype: Optional[str]
    rank_: Optional[str]
    hgvs_c: Optional[str]
    hgvs_p: Optional[str]
    cdna_pos__cdna_length: Optional[str]
    cds_pos__cds_length: Optional[str]
    aa_pos__aa_length: Optional[str]
    distance: Optional[int]
    errors_warnings_info: Optional[str]

    class Config:
        orm_mode = True


class Cov(BaseModel):
    ena_run: Optional[str]
    pos: Optional[int]
    coverage: Optional[int]

    class Config:
        orm_mode = True


class Meta(BaseModel):
    ena_run: Optional[str]
    collection_date: Optional[date]
    clean_country: Optional[str]
    clean_host: Optional[str]
    accession: Optional[str]
    sample_accession: Optional[str]
    experiment_accession: Optional[str]
    study_accession: Optional[str]
    description: Optional[str]
    country: Optional[str]
    first_created: Optional[date]
    first_public: Optional[date]
    host: Optional[str]
    host_sex: Optional[str]
    host_tax_id: Optional[int]
    host_body_site: Optional[str]
    bio_material: Optional[str]
    culture_collection: Optional[str]
    instrument_model: Optional[str]
    instrument_platform: Optional[str]
    library_layout: Optional[str]
    library_name: Optional[str]
    library_selection: Optional[str]
    library_source: Optional[str]
    library_strategy: Optional[str]
    sequencing_method: Optional[str]
    isolate: Optional[str]
    strain: Optional[str]
    base_count: Optional[float]
    collected_by: Optional[str]
    broker_name: Optional[str]
    center_name: Optional[str]
    sample_capture_status: Optional[str]
    fastq_ftp: Optional[str]
    collection_date_submitted: Optional[str]
    checklist: Optional[str]
    clean_collection_date: Optional[date]
    date_isoweek: Optional[date]
    date_isoyear: Optional[date]

    class Config:
        orm_mode = True


class LineageDef(BaseModel):
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


class UniqueCov(BaseModel):
    insertion_ts: Optional[date]
    ena_run: Optional[str]
    snapshot: Optional[str]
    integrity: Optional[int]

    class Config:
        orm_mode = True


class UniqueVCF(BaseModel):
    insertion_ts: Optional[date]
    ena_run: Optional[str]
    snapshot: Optional[str]
    integrity: Optional[int]

    class Config:
        orm_mode = True


class CountrySamples(BaseModel):
    clean_country: str
    n_sample: str
    log_n_sample: str


class LineageDefDesc(BaseModel):
    variant_id: str
    pango: str
    description: str


class Lineage(BaseModel):
    clean_collection_date: date
    clean_country: str
    variant_id: str
    n: int
    n_all: int
    pct: float


class NewCases(BaseModel):
    country_name: str
    date_year: int
    date_week: int
    weekly_sample: int
    iso_a3: Optional[str]
    iso_a2: Optional[str]
    country_name_local: Optional[str]
    population: Optional[float]
    ecdc_covid_country_weekly_cases: Optional[int]
    ecdc_covid_country_weekly_deaths: Optional[int]


class VariantsWeekly(BaseModel):
    country_name: str
    date_year: int
    date_week: int
    variant_id: str
    weekly_variant_sample: int


class WorldplotData(BaseModel):
    Country: str
    date_year: int
    date_week: int
    weekly_sample: int


class CheckViews(BaseModel):
    attrelid: int
    attname: str
