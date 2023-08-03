from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, TEXT, TIMESTAMP, \
    VARCHAR, INTEGER, REAL, BOOLEAN, DATE, NUMERIC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import text

from database import SQLALCHEMY_DATABASE_URL, ALLOWED_SCHEMAS, POSTGRES_SCHEMA_KEY

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi import HTTPException

Base = declarative_base()


class DbConnect:

    def __init__(self):
        self.connect_instance = None
        self.schema = ALLOWED_SCHEMAS[POSTGRES_SCHEMA_KEY]
        self.engine = None

    def connect(self, schema_name):

        if schema_name is None:
            raise HTTPException(status_code=500, details="Schema name can't be empty")

        if self.connect_instance is not None and self.schema == schema_name:
            return self.connect_instance

        self.schema = schema_name

        engine = create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={'options': '-csearch_path={}'.format(
                self.schema
            )}
        )
        self.engine = engine

        Base.metadata.create_all(bind=engine)
        self.connect_instance = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return self.connect_instance

    def get_schema(self):
        return self.schema

    def get_engine(self):
        return self.engine


db_connect = DbConnect()


class AbstractBase(Base):

    __abstract__ = True

    def __init__(self):
        self.default_schema = ALLOWED_SCHEMAS[POSTGRES_SCHEMA_KEY]

    @property
    def schema(self):
        return self.default_schema

    @classmethod
    def get_schema(cls):
        return cls.__table__.schema

    @classmethod
    def set_schema(cls, schema_name):
        cls.__table__.schema = schema_name


class MViewCountrySamples(AbstractBase):
    __tablename__ = "api_country_samples_full"
    pkey = Column(INTEGER, primary_key=True)
    country = Column(VARCHAR)
    n_sample = Column(INTEGER)
    log_n_sample = Column(DOUBLE_PRECISION)
    relative_n_sample = Column(DOUBLE_PRECISION)
    relative_log_n_sample = Column(DOUBLE_PRECISION)


class MViewHumanMetaMv(AbstractBase):
    __tablename__ = "api_human_meta_mv"
    pkey = Column(INTEGER, primary_key=True)
    country_name = Column(VARCHAR)
    date = Column(DATE)
    date_year = Column(DOUBLE_PRECISION)
    date_week = Column(DOUBLE_PRECISION)
    weekly_sample = Column(INTEGER)


class MViewHumanMetaMvJhd(AbstractBase):
    __tablename__ = "api_human_meta_mv_jhd"
    pkey = Column(INTEGER, primary_key=True)
    country_name = Column(VARCHAR)
    date = Column(DATE)
    date_year = Column(DOUBLE_PRECISION)
    date_week = Column(DOUBLE_PRECISION)
    weekly_sample = Column(INTEGER)
    cases = Column(INTEGER)
    pct = Column(NUMERIC)


class LineageDef(AbstractBase):
    __tablename__ = "api_lineage_def"
    pkey = Column(INTEGER, primary_key=True)
    variant_id = Column(TEXT)
    pango = Column(TEXT)
    type_variant = Column(TEXT)
    amino_acid_change = Column(TEXT)
    protein_codon_position = Column(INTEGER)
    ref_protein = Column(TEXT)
    alt_protein = Column(TEXT)
    gene = Column(TEXT)
    effect = Column(TEXT)
    snpeff_original_mut = Column(TEXT)
    ref_pos_alt = Column(TEXT)
    ref = Column(TEXT)
    alt = Column(TEXT)
    pos = Column(INTEGER)
    description = Column(TEXT)


class MViewLineage(AbstractBase):
    __tablename__ = "api_lineage"
    pkey = Column(INTEGER, primary_key=True)
    collection_date = Column(DATE)
    country = Column(VARCHAR)
    variant_id = Column(TEXT)
    n = Column(INTEGER)
    n_all = Column(INTEGER)
    pct = Column(NUMERIC)


class MViewNewCasesJhd(AbstractBase):
    __tablename__ = "api_new_cases_jhd"
    pkey = Column(INTEGER, primary_key=True)
    country = Column(VARCHAR)
    date = Column(DATE)
    date_year = Column(DOUBLE_PRECISION)
    date_week = Column(DOUBLE_PRECISION)
    weekly_sample = Column(INTEGER)
    cases = Column(INTEGER)


class MViewVariantsWeekly(AbstractBase):
    __tablename__ = "api_variants_weekly"
    pkey = Column(INTEGER, primary_key=True)
    country = Column(VARCHAR)
    date_year = Column(DOUBLE_PRECISION)
    date_week = Column(DOUBLE_PRECISION)
    variant_id = Column(TEXT)
    weekly_variant_sample = Column(INTEGER)


class MViewUniqueEnaRunSum(AbstractBase):
    __tablename__ = "api_unique_ena_run_summary"
    pkey = Column(INTEGER, primary_key=True)
    table_name = Column(VARCHAR)
    count = Column(INTEGER)


class SProcFilterCustomBrowserCov(AbstractBase):
    __tablename__ = 'filter_custom_browser_cov'

    country = Column(VARCHAR, primary_key=True)
    collection_date = Column(DATE, primary_key=True)

    @classmethod
    def call(cls, schema, included, excluded):
        global db_connect
        engine = db_connect.get_engine()

        connection = engine.raw_connection()

        cursor = connection.cursor()
        cursor.execute(
            f"CALL {schema}.filter_custom_browser_cov('{included}', '{excluded}');"
        )
        cursor.close()

        return connection


class SProcFilterCustomBrowser(AbstractBase):
    __tablename__ = 'filter_custom_browser'

    country = Column(VARCHAR, primary_key=True)
    collection_date = Column(DATE, primary_key=True)

    @classmethod
    def call(cls, schema, included, excluded):
        global db_connect
        engine = db_connect.get_engine()

        connection = engine.raw_connection()

        cursor = connection.cursor()
        cursor.execute(
            f"CALL {schema}.filter_custom_browser('{included}', '{excluded}');"
        )
        cursor.close()

        return connection
