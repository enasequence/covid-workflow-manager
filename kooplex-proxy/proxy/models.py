from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, TEXT, TIMESTAMP, \
    VARCHAR, INTEGER, REAL, BOOLEAN, DATE
from database import Base


class CovidCountryWeekly(Base):
    __tablename__ = "ecdc_covid_country_weekly"
    iso_a3 = Column(TEXT, primary_key=True)
    iso_a2 = Column(TEXT, primary_key=True)
    country_name = Column(TEXT, primary_key=True)
    country_name_local = Column(TEXT, primary_key=True)
    date_year = Column(DOUBLE_PRECISION, primary_key=True)
    date_week = Column(DOUBLE_PRECISION, primary_key=True)
    ecdc_covid_country_weekly_cases = Column(DOUBLE_PRECISION,
                                             primary_key=True)
    ecdc_covid_country_weekly_deaths = Column(DOUBLE_PRECISION,
                                              primary_key=True)


class UniqueVCFAppend(Base):
    __tablename__ = "unique_vcf_append"
    insertion_ts = Column(TIMESTAMP, primary_key=True)
    ena_run = Column(VARCHAR, primary_key=True)
    snapshot = Column(VARCHAR, primary_key=True)
    integrity = Column(INTEGER, primary_key=True)


class VCFAll(Base):
    __tablename__ = "vcf_all"
    ena_run = Column(VARCHAR, primary_key=True)
    chrom = Column(TEXT, primary_key=True)
    pos = Column(INTEGER, primary_key=True)
    ref = Column(TEXT, primary_key=True)
    alt = Column(TEXT, primary_key=True)
    qual = Column(INTEGER, primary_key=True)
    filter = Column(TEXT, primary_key=True)
    dp = Column(INTEGER, primary_key=True)
    af = Column(REAL, primary_key=True)
    sb = Column(INTEGER, primary_key=True)
    count_ref_forward_base = Column(INTEGER, primary_key=True)
    count_ref_reverse_base = Column(INTEGER, primary_key=True)
    count_alt_forward_base = Column(INTEGER, primary_key=True)
    count_alt_reverse_base = Column(INTEGER, primary_key=True)
    hrun = Column(INTEGER, primary_key=True)
    indel = Column(BOOLEAN, primary_key=True)
    lof = Column(TEXT, primary_key=True)
    nmd = Column(TEXT, primary_key=True)
    ann_num = Column(INTEGER, primary_key=True)
    annotation = Column(TEXT, primary_key=True)
    annotation_impact = Column(TEXT, primary_key=True)
    gene_name = Column(TEXT, primary_key=True)
    gene_id = Column(TEXT, primary_key=True)
    feature_type = Column(TEXT, primary_key=True)
    feature_id = Column(TEXT, primary_key=True)
    transcript_biotype = Column(TEXT, primary_key=True)
    rank_ = Column(TEXT, primary_key=True)
    hgvs_c = Column(TEXT, primary_key=True)
    hgvs_p = Column(TEXT, primary_key=True)
    cdna_pos__cdna_length = Column(TEXT, primary_key=True)
    cds_pos__cds_length = Column(TEXT, primary_key=True)
    aa_pos__aa_length = Column(TEXT, primary_key=True)
    distance = Column(INTEGER, primary_key=True)
    errors_warnings_info = Column(TEXT, primary_key=True)


class Cov(Base):
    __tablename__ = "cov"
    ena_run = Column(VARCHAR, primary_key=True)
    pos = Column(INTEGER, primary_key=True)
    coverage = Column(INTEGER, primary_key=True)


class Meta(Base):
    __tablename__ = "meta"
    ena_run = Column(VARCHAR, primary_key=True)
    collection_date = Column(DATE, primary_key=True)
    clean_country = Column(TEXT, primary_key=True)
    clean_host = Column(TEXT, primary_key=True)
    accession = Column(TEXT, primary_key=True)
    sample_accession = Column(TEXT, primary_key=True)
    experiment_accession = Column(TEXT, primary_key=True)
    study_accession = Column(TEXT, primary_key=True)
    description = Column(TEXT, primary_key=True)
    country = Column(TEXT, primary_key=True)
    first_created = Column(DATE, primary_key=True)
    first_public = Column(DATE, primary_key=True)
    host = Column(TEXT, primary_key=True)
    host_sex = Column(TEXT, primary_key=True)
    host_tax_id = Column(INTEGER, primary_key=True)
    host_body_site = Column(TEXT, primary_key=True)
    bio_material = Column(TEXT, primary_key=True)
    culture_collection = Column(TEXT, primary_key=True)
    instrument_model = Column(TEXT, primary_key=True)
    instrument_platform = Column(TEXT, primary_key=True)
    library_layout = Column(TEXT, primary_key=True)
    library_name = Column(TEXT, primary_key=True)
    library_selection = Column(TEXT, primary_key=True)
    library_source = Column(TEXT, primary_key=True)
    library_strategy = Column(TEXT, primary_key=True)
    sequencing_method = Column(TEXT, primary_key=True)
    isolate = Column(TEXT, primary_key=True)
    strain = Column(TEXT, primary_key=True)
    base_count = Column(DOUBLE_PRECISION, primary_key=True)
    collected_by = Column(TEXT, primary_key=True)
    broker_name = Column(TEXT, primary_key=True)
    center_name = Column(TEXT, primary_key=True)
    sample_capture_status = Column(TEXT, primary_key=True)
    fastq_ftp = Column(TEXT, primary_key=True)
    collection_date_submitted = Column(TEXT, primary_key=True)
    checklist = Column(TEXT, primary_key=True)
    clean_collection_date = Column(DATE, primary_key=True)
    date_isoweek = Column(INTEGER, primary_key=True)
    date_isoyear = Column(INTEGER, primary_key=True)


class UniqueCovAppend(Base):
    __tablename__ = "unique_cov_append"
    insertion_ts = Column(TIMESTAMP, primary_key=True)
    ena_run = Column(VARCHAR, primary_key=True)
    snapshot = Column(VARCHAR, primary_key=True)
    integrity = Column(INTEGER, primary_key=True)


class LineageDef(Base):
    __tablename__ = "lineage_def"
    variant_id = Column(TEXT, primary_key=True)
    pango = Column(TEXT, primary_key=True)
    nextstrain = Column(TEXT, primary_key=True)
    ref_pos_alt = Column(TEXT, primary_key=True)
    codon_change = Column(TEXT, primary_key=True)
    gene = Column(TEXT, primary_key=True)
    pos = Column(DOUBLE_PRECISION, primary_key=True)
    predicted_effect = Column(TEXT, primary_key=True)
    protein = Column(TEXT, primary_key=True)
    protein_codon_position = Column(DOUBLE_PRECISION, primary_key=True)
    ref = Column(TEXT, primary_key=True)
    type = Column(TEXT, primary_key=True)
    alt = Column(TEXT, primary_key=True)
    amino_acid_change = Column(TEXT, primary_key=True)
    description = Column(TEXT, primary_key=True)
    snp_codon_position = Column(TEXT, primary_key=True)


class Operation(Base):
    __tablename__ = "operation"
    event_ts = Column(TIMESTAMP, primary_key=True)
    last_stage = Column(INTEGER, primary_key=True)
    last_exit_code = Column(INTEGER, primary_key=True)
    stage = Column(INTEGER, primary_key=True)
    exit_code = Column(INTEGER, primary_key=True)
    extra_info = Column(TEXT, primary_key=True)


class UniqueCov(Base):
    __tablename__ = "unique_cov"
    insertion_ts = Column(TIMESTAMP, primary_key=True)
    ena_run = Column(VARCHAR, primary_key=True)
    snapshot = Column(VARCHAR, primary_key=True)
    integrity = Column(INTEGER, primary_key=True)


class UniqueVCF(Base):
    __tablename__ = "unique_vcf"
    insertion_ts = Column(TIMESTAMP, primary_key=True)
    ena_run = Column(VARCHAR, primary_key=True)
    snapshot = Column(VARCHAR, primary_key=True)
    integrity = Column(INTEGER, primary_key=True)


class VCFAllAppend(Base):
    __tablename__ = "vcf_all_append"
    ena_run = Column(TEXT, primary_key=True)
    chrom = Column(TEXT, primary_key=True)
    pos = Column(INTEGER, primary_key=True)
    ref = Column(TEXT, primary_key=True)
    alt = Column(TEXT, primary_key=True)
    qual = Column(INTEGER, primary_key=True)
    filter = Column(TEXT, primary_key=True)
    dp = Column(INTEGER, primary_key=True)
    af = Column(REAL, primary_key=True)
    sb = Column(INTEGER, primary_key=True)
    count_ref_forward_base = Column(INTEGER, primary_key=True)
    count_ref_reverse_base = Column(INTEGER, primary_key=True)
    count_alt_forward_base = Column(INTEGER, primary_key=True)
    count_alt_reverse_base = Column(INTEGER, primary_key=True)
    hrun = Column(INTEGER, primary_key=True)
    indel = Column(BOOLEAN, primary_key=True)
    lof = Column(TEXT, primary_key=True)
    nmd = Column(TEXT, primary_key=True)
    ann_num = Column(INTEGER, primary_key=True)
    annotation = Column(TEXT, primary_key=True)
    annotation_impact = Column(TEXT, primary_key=True)
    gene_name = Column(TEXT, primary_key=True)
    gene_id = Column(TEXT, primary_key=True)
    feature_type = Column(TEXT, primary_key=True)
    feature_id = Column(TEXT, primary_key=True)
    transcript_biotype = Column(TEXT, primary_key=True)
    rank_ = Column(TEXT, primary_key=True)
    hgvs_c = Column(TEXT, primary_key=True)
    hgvs_p = Column(TEXT, primary_key=True)
    cdna_pos__cdna_length = Column(TEXT, primary_key=True)
    cds_pos__cds_length = Column(TEXT, primary_key=True)
    aa_pos__aa_length = Column(TEXT, primary_key=True)
    distance = Column(INTEGER, primary_key=True)
    errors_warnings_info = Column(TEXT, primary_key=True)


class CountrySamples(Base):
    __tablename__ = "Meta"
    __table_args__ = {'extend_existing': True}
    clean_country = Meta.clean_country
    n_sample = Column(Integer, primary_key=True)


class LineageDefSelectedFields(Base):
    __tablename__ = "lineage_def"
    __table_args__ = {'extend_existing': True}
    variant_id = Column(TEXT, primary_key=True)
    pango = Column(TEXT, primary_key=True)
    nextstrain = Column(TEXT, primary_key=True)
    description = Column(TEXT, primary_key=True)
