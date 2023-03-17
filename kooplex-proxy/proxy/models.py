from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, MetaData
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, TEXT, TIMESTAMP, \
    VARCHAR, INTEGER, REAL, BOOLEAN, DATE, NUMERIC
from database import Base

METADATA = MetaData()


class MViewCountrySamples(Base):
    __tablename__ = "app_country_samples_full"
    country = Column(VARCHAR, primary_key=True)
    n_sample = Column(INTEGER)
    log_n_sample = Column(DOUBLE_PRECISION)
    relative_n_sample = Column(DOUBLE_PRECISION)
    relative_log_n_sample = Column(DOUBLE_PRECISION)


class MViewHumanMetaMv(Base):
    __tablename__ = "app_human_meta_mv"
    country_name = Column(VARCHAR, primary_key=True)
    date = Column(DATE, primary_key=True)
    date_year = Column(DOUBLE_PRECISION)
    date_week = Column(DOUBLE_PRECISION)
    weekly_sample = Column(INTEGER)


class MViewHumanMetaMvJhd(Base):
    __tablename__ = "app_human_meta_mv_jhd"
    country_name = Column(VARCHAR, primary_key=True)
    date = Column(DATE, primary_key=True)
    date_year = Column(DOUBLE_PRECISION)
    date_week = Column(DOUBLE_PRECISION)
    weekly_sample = Column(INTEGER)
    cases = Column(INTEGER)
    pct = Column(NUMERIC)


class LineageDef(Base):
    __tablename__ = "lineage_def"
    variant_id = Column(TEXT, primary_key=True)
    pango = Column(TEXT, primary_key=True)
    type_variant = Column(TEXT)
    amino_acid_change = Column(TEXT)
    protein_codon_position = Column(INTEGER, primary_key=True)
    ref_protein = Column(TEXT)
    alt_protein = Column(TEXT)
    gene = Column(TEXT, primary_key=True)
    effect = Column(TEXT)
    snpeff_original_mut = Column(TEXT, primary_key=True)
    ref_pos_alt = Column(TEXT)
    ref = Column(TEXT)
    alt = Column(TEXT)
    pos = Column(INTEGER, primary_key=True)
    description = Column(TEXT)


class MViewLineage(Base):
    __tablename__ = "app_lineage"
    collection_date = Column(DATE, primary_key=True)
    country = Column(VARCHAR)
    variant_id = Column(TEXT)
    n = Column(INTEGER)
    n_all = Column(INTEGER)
    pct = Column(NUMERIC)


class MViewNewCasesJhd(Base):
    __tablename__ = "app_new_cases_jhd"
    country = Column(VARCHAR, primary_key=True)
    date = Column(DATE, primary_key=True)
    date_year = Column(DOUBLE_PRECISION)
    date_week = Column(DOUBLE_PRECISION)
    weekly_sample = Column(INTEGER)
    cases = Column(INTEGER)


class MViewVariantsWeekly(Base):
    __tablename__ = "app_variants_weekly"
    country = Column(VARCHAR, primary_key=True)
    date_year = Column(DOUBLE_PRECISION, primary_key=True)
    date_week = Column(DOUBLE_PRECISION, primary_key=True)
    variant_id = Column(TEXT)
    weekly_variant_sample = Column(INTEGER)
