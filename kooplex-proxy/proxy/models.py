from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, TEXT, TIMESTAMP, \
    VARCHAR, INTEGER, REAL, BOOLEAN, DATE, NUMERIC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import text

from database import ALLOWED_SCHEMAS

Base = declarative_base()


class AbstractBase(Base):

    __abstract__ = True

    def __init__(self):
        self.default_schema = ALLOWED_SCHEMAS['schema_1']

    @property
    def schema(self):
        return self.default_schema

    @classmethod
    def get_schema(cls):
        return cls.__table_args__['schema']

    @classmethod
    def set_schema(cls, schema_name):
        cls.__table_args__['schema'] = schema_name


class MViewCountrySamples(AbstractBase):
    __tablename__ = "app_country_samples_full"
    __table_args__ = {'schema': AbstractBase().schema}
    country = Column(VARCHAR, primary_key=True)
    n_sample = Column(INTEGER)
    log_n_sample = Column(DOUBLE_PRECISION)
    relative_n_sample = Column(DOUBLE_PRECISION)
    relative_log_n_sample = Column(DOUBLE_PRECISION)


class MViewHumanMetaMv(AbstractBase):
    __tablename__ = "app_human_meta_mv"
    __table_args__ = {'schema': AbstractBase().schema}
    country_name = Column(VARCHAR, primary_key=True)
    date = Column(DATE, primary_key=True)
    date_year = Column(DOUBLE_PRECISION)
    date_week = Column(DOUBLE_PRECISION)
    weekly_sample = Column(INTEGER)


class MViewHumanMetaMvJhd(AbstractBase):
    __tablename__ = "app_human_meta_mv_jhd"
    __table_args__ = {'schema': AbstractBase().schema}
    country_name = Column(VARCHAR, primary_key=True)
    date = Column(DATE, primary_key=True)
    date_year = Column(DOUBLE_PRECISION)
    date_week = Column(DOUBLE_PRECISION)
    weekly_sample = Column(INTEGER)
    cases = Column(INTEGER)
    pct = Column(NUMERIC)


class LineageDef(AbstractBase):
    __tablename__ = "lineage_def"
    __table_args__ = {'schema': AbstractBase().schema}
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


class MViewLineage(AbstractBase):
    __tablename__ = "app_lineage"
    __table_args__ = {'schema': AbstractBase().schema}
    collection_date = Column(DATE, primary_key=True)
    country = Column(VARCHAR)
    variant_id = Column(TEXT)
    n = Column(INTEGER)
    n_all = Column(INTEGER)
    pct = Column(NUMERIC)


class MViewNewCasesJhd(AbstractBase):
    __tablename__ = "app_new_cases_jhd"
    __table_args__ = {'schema': AbstractBase().schema}
    country = Column(VARCHAR, primary_key=True)
    date = Column(DATE, primary_key=True)
    date_year = Column(DOUBLE_PRECISION)
    date_week = Column(DOUBLE_PRECISION)
    weekly_sample = Column(INTEGER)
    cases = Column(INTEGER)


class MViewVariantsWeekly(AbstractBase):
    __tablename__ = "app_variants_weekly"
    __table_args__ = {'schema': AbstractBase().schema}
    country = Column(VARCHAR, primary_key=True)
    date_year = Column(DOUBLE_PRECISION, primary_key=True)
    date_week = Column(DOUBLE_PRECISION, primary_key=True)
    variant_id = Column(TEXT)
    weekly_variant_sample = Column(INTEGER)


class MViewUniqueEnaRunSum(AbstractBase):
    __tablename__ = "unique_ena_run_summary"
    __table_args__ = {'schema': AbstractBase().schema}
    table_name = Column(VARCHAR, primary_key=True)
    count = Column(INTEGER)


class SProcFilterCustomBrowserCov(AbstractBase):
    __tablename__ = 'filter_custom_browser_cov'
    __table_args__ = {'schema': AbstractBase().schema}

    country = Column(VARCHAR, primary_key=True)
    count = Column(INTEGER)

    @classmethod
    def call(cls, session):
        session.execute(
            text(f"CALL sandbox_public.filter_custom_browser_cov('p.Asp80Ala,p.Asp215Gly', 'p.Asp77Al,p.Asp102Ala');")
        )
        return


class SProcFilterCustomBrowserCovTime(AbstractBase):
    __tablename__ = 'filter_custom_browser_cov_time'
    __table_args__ = {'schema': AbstractBase().schema}

    collection_date = Column(DATE, primary_key=True)
    country = Column(VARCHAR, primary_key=True)
    other_count = Column(INTEGER)
    variant_count = Column(INTEGER)

    @classmethod
    def call(cls, session):
        session.execute(
            text(f"CALL sandbox_public.filter_custom_browser_cov('p.Asp80Ala,p.Asp215Gly', 'p.Asp77Al,p.Asp102Ala');")
        )
        return
