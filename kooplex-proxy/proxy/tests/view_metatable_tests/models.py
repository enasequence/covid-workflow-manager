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
    date_year = Column(DOUBLE_PRECISION, primary_key=True)
    date_week = Column(DOUBLE_PRECISION, primary_key=True)
    ecdc_covid_country_weekly_cases = Column(DOUBLE_PRECISION)
    ecdc_covid_country_weekly_deaths = Column(DOUBLE_PRECISION)


class UniqueVCFAppend(Base):
    __tablename__ = "unique_vcf_append"
    insertion_ts = Column(TIMESTAMP)
    ena_run = Column(VARCHAR, primary_key=True)
    snapshot = Column(VARCHAR)
    integrity = Column(INTEGER)


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


MetaTable = Table(
    "meta",
    METADATA,
    Column("ena_run", VARCHAR, primary_key=True),
    Column("collection_date", DATE, primary_key=True),
    Column("clean_country", TEXT, primary_key=True),
    Column("clean_host", TEXT, primary_key=True),
    Column("accession", TEXT),
    Column("sample_accession", TEXT, primary_key=True),
    Column("experiment_accession", TEXT, primary_key=True),
    Column("study_accession", TEXT, primary_key=True),
    Column("description", TEXT),
    Column("country", TEXT),
    Column("first_created", DATE, primary_key=True),
    Column("first_public", DATE, primary_key=True),
    Column("host", TEXT),
    Column("host_sex", TEXT),
    Column("host_tax_id", INTEGER),
    Column("host_body_site", TEXT),
    Column("bio_material", TEXT),
    Column("culture_collection", TEXT),
    Column("instrument_model", TEXT),
    Column("instrument_platform", TEXT),
    Column("library_layout", TEXT),
    Column("library_name", TEXT),
    Column("library_selection", TEXT),
    Column("library_source", TEXT),
    Column("library_strategy", TEXT),
    Column("sequencing_method", TEXT),
    Column("isolate", TEXT),
    Column("strain", TEXT),
    Column("base_count", DOUBLE_PRECISION),
    Column("collected_by", TEXT),
    Column("broker_name", TEXT),
    Column("center_name", TEXT),
    Column("sample_capture_status", TEXT),
    Column("fastq_ftp", TEXT),
    Column("collection_date_submitted", TEXT),
    Column("checklist", TEXT),
    Column("clean_collection_date", DATE, primary_key=True),
    Column("date_isoyear", DATE, primary_key=True),
    Column("date_isoweek", DATE, primary_key=True)
)


class Meta(Base):
    __table__ = MetaTable
    #__mapper_args__ = {'column_prefix': '_'}


class UniqueCovAppend(Base):
    __tablename__ = "unique_cov_append"
    insertion_ts = Column(TIMESTAMP)
    ena_run = Column(VARCHAR, primary_key=True)
    snapshot = Column(VARCHAR)
    integrity = Column(INTEGER)


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


class Operation(Base):
    __tablename__ = "operation"
    event_ts = Column(TIMESTAMP, primary_key=True)
    last_stage = Column(INTEGER)
    last_exit_code = Column(INTEGER,)
    stage = Column(INTEGER)
    exit_code = Column(INTEGER)
    extra_info = Column(TEXT)


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


class VCFAllAppend(Base):
    __tablename__ = "vcf_all_append"
    ena_run = Column(TEXT, primary_key=True)
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
