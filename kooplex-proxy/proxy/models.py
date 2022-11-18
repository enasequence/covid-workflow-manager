from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, MetaData
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, TEXT, TIMESTAMP, \
    VARCHAR, INTEGER, REAL, BOOLEAN, DATE
from database import Base

METADATA = MetaData()


class CovidCountryWeekly(Base):
    __tablename__ = "ecdc_covid_country_weekly"
    iso_a3 = Column(TEXT)
    iso_a2 = Column(TEXT)
    country_name = Column(TEXT, primary_key=True)
    country_name_local = Column(TEXT, primary_key=True)
    population = Column(INTEGER, primary_key=True)
    date_year = Column(INTEGER, primary_key=True)
    date_week = Column(INTEGER, primary_key=True)
    ecdc_covid_country_weekly_cases = Column(INTEGER)
    ecdc_covid_country_weekly_deaths = Column(INTEGER)


class VCFAll(Base):
    __tablename__ = "vcf_all"
    ena_run = Column(VARCHAR, primary_key=True)
    chrom = Column(TEXT, primary_key=True)
    pos = Column(INTEGER, primary_key=True)
    ref = Column(TEXT)
    alt = Column(TEXT)
    qual = Column(INTEGER)
    filter = Column(TEXT)
    dp = Column(INTEGER)
    af = Column(REAL)
    sb = Column(INTEGER)
    count_ref_forward_base = Column(INTEGER)
    count_ref_reverse_base = Column(INTEGER)
    count_alt_forward_base = Column(INTEGER)
    count_alt_reverse_base = Column(INTEGER)
    hrun = Column(INTEGER)
    indel = Column(BOOLEAN)
    lof = Column(TEXT)
    nmd = Column(TEXT)
    ann_num = Column(INTEGER)
    annotation = Column(TEXT)
    annotation_impact = Column(TEXT)
    gene_name = Column(TEXT)
    gene_id = Column(TEXT)
    feature_type = Column(TEXT)
    feature_id = Column(TEXT)
    transcript_biotype = Column(TEXT)
    rank_ = Column(TEXT)
    hgvs_c = Column(TEXT)
    hgvs_p = Column(TEXT)
    cdna_pos__cdna_length = Column(TEXT)
    cds_pos__cds_length = Column(TEXT)
    aa_pos__aa_length = Column(TEXT)
    distance = Column(INTEGER)
    errors_warnings_info = Column(TEXT)


class Cov(Base):
    __tablename__ = "cov"
    ena_run = Column(VARCHAR, primary_key=True)
    pos = Column(INTEGER)
    coverage = Column(INTEGER)


class Meta(Base):
    __tablename__ = "meta"
    ena_run = Column(VARCHAR, primary_key=True)
    collection_date = Column(DATE, primary_key=True)
    clean_country = Column(TEXT, primary_key=True)
    clean_host = Column(TEXT, primary_key=True)
    accession = Column(TEXT)
    sample_accession = Column(TEXT, primary_key=True)
    experiment_accession = Column(TEXT, primary_key=True)
    study_accession = Column(TEXT, primary_key=True)
    description = Column(TEXT)
    country = Column(TEXT)
    first_created = Column(DATE, primary_key=True)
    first_public = Column(DATE, primary_key=True)
    host = Column(TEXT)
    host_sex = Column(TEXT)
    host_tax_id = Column(INTEGER)
    host_body_site = Column(TEXT)
    bio_material = Column(TEXT)
    culture_collection = Column(TEXT)
    instrument_model = Column(TEXT)
    instrument_platform = Column(TEXT)
    library_layout = Column(TEXT)
    library_name = Column(TEXT)
    library_selection = Column(TEXT)
    library_source = Column(TEXT)
    library_strategy = Column(TEXT)
    sequencing_method = Column(TEXT)
    isolate = Column(TEXT)
    strain = Column(TEXT)
    base_count = Column(DOUBLE_PRECISION)
    collected_by = Column(TEXT)
    broker_name = Column(TEXT)
    center_name = Column(TEXT)
    sample_capture_status = Column(TEXT)
    fastq_ftp = Column(TEXT)
    collection_date_submitted = Column(TEXT)
    checklist = Column(TEXT)
    clean_collection_date = Column(DATE, primary_key=True)
    date_isoweek = Column(DATE, primary_key=True)
    date_isoyear = Column(DATE, primary_key=True)


class LineageDef(Base):
    __tablename__ = "lineage_def"
    variant_id = Column(TEXT, primary_key=True)
    pango = Column(TEXT, primary_key=True)
    type_variant = Column(TEXT)
    amino_acid_change = Column(TEXT)
    protein_codon_position = Column(TEXT, primary_key=True)
    ref_protein = Column(TEXT)
    alt_protein = Column(TEXT)
    gene = Column(TEXT, primary_key=True)
    effect = Column(TEXT)
    snpeff_original_mut = Column(TEXT, primary_key=True)
    ref_pos_alt = Column(TEXT)
    ref = Column(TEXT)
    alt = Column(TEXT)
    pos = Column(DOUBLE_PRECISION, primary_key=True)
    description = Column(TEXT)


class UniqueCov(Base):
    __tablename__ = "unique_cov"
    insertion_ts = Column(TIMESTAMP)
    ena_run = Column(VARCHAR, primary_key=True)
    snapshot = Column(VARCHAR)
    integrity = Column(INTEGER)


class UniqueVCF(Base):
    __tablename__ = "unique_vcf"
    insertion_ts = Column(TIMESTAMP)
    ena_run = Column(VARCHAR, primary_key=True)
    snapshot = Column(VARCHAR)
    integrity = Column(INTEGER)


class View_country_samples(Base):
    __tablename__ = "app_country_samples"
    clean_country = Column(VARCHAR, primary_key=True)
    n_sample = Column(INTEGER)
    log_n_sample = Column(DOUBLE_PRECISION)


class View_lineage_def_description(Base):
    __tablename__ = "app_lineage_def_description"
    variant_id = Column(VARCHAR, primary_key=True)
    pango = Column(VARCHAR)
    description = Column(VARCHAR)


class View_lineage(Base):
    __tablename__ = "app_lineage"
    clean_collection_date = Column(DATE, primary_key=True)
    clean_country = Column(VARCHAR)
    variant_id = Column(VARCHAR)
    n = Column(INTEGER)
    n_all = Column(INTEGER)
    pct = Column(DOUBLE_PRECISION)


class View_new_cases(Base):
    __tablename__ = "app_new_cases"
    country_name = Column(VARCHAR, primary_key=True)
    date_year = Column(INTEGER, primary_key=True)
    date_week = Column(INTEGER, primary_key=True)
    weekly_sample = Column(INTEGER)
    iso_a3 = Column(VARCHAR)
    iso_a2 = Column(VARCHAR)
    country_name_local = Column(VARCHAR)
    population = Column(INTEGER)
    ecdc_covid_country_weekly_cases = Column(INTEGER)
    ecdc_covid_country_weekly_deaths = Column(INTEGER)


class View_variants_weekly(Base):
    __tablename__ = "app_variants_weekly"
    country_name = Column(VARCHAR, primary_key=True)
    date_year = Column(INTEGER, primary_key=True)
    date_week = Column(INTEGER, primary_key=True)
    variant_id = Column(VARCHAR)
    weekly_variant_sample = Column(INTEGER)


class View_worldplot_data(Base):
    __tablename__ = "app_worldplot_data"
    Country = Column(VARCHAR, primary_key=True)
    date_year = Column(INTEGER, primary_key=True)
    date_week = Column(INTEGER, primary_key=True)
    weekly_sample = Column(INTEGER)


class View_table_description(Base):
    __tablename__ = "table_description"
    type = Column(VARCHAR)
    table_name = Column(VARCHAR, primary_key=True)
    title = Column(VARCHAR, primary_key=True)
    description = Column(VARCHAR)


class View_column_description(Base):
    __tablename__ = "column_description"
    table_name = Column(VARCHAR, primary_key=True)
    column_name = Column(VARCHAR, primary_key=True)
    description = Column(VARCHAR)
