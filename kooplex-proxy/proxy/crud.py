from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import text
import asyncio
import time

import models


def get_country_samples(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewCountrySamples
    return db.query(model).offset(skip).limit(limit).all()


def get_human_meta_mv(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewHumanMetaMv
    return db.query(model).offset(skip).limit(limit).all()


def get_human_meta_mv_jhd(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewHumanMetaMvJhd
    return db.query(model).offset(skip).limit(limit).all()


def get_lineage_def(db: Session, skip: int = 0, limit: int = 100):
    model = models.LineageDef
    return db.query(model).offset(skip).limit(limit).all()


def get_lineage(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewLineage
    return db.query(model).offset(skip).limit(limit).all()


def get_new_cases_jhd(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewNewCasesJhd
    return db.query(model).offset(skip).limit(limit).all()


def get_variants_weekly(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewVariantsWeekly
    return db.query(model).offset(skip).limit(limit).all()


def get_unique_ena_run_summary(db: Session, skip: int = 0, limit: int = 100):
    model = models.MViewUniqueEnaRunSum
    return db.query(model).offset(skip).limit(limit).all()


def filter_custom_browser_cov(schema: str, included: str, excluded: str, skip: int = 0,
                              limit: int = 100):
    model = models.SProcFilterCustomBrowserCov

    async def model_call():
        connection = model.call(schema=schema, included=included, excluded=excluded)
        return connection

    async def main_call():
        connection = await model_call()

        try:
            cursor = connection.cursor()
            cursor.callproc(f"{schema}.filter_country_count")

            for _ in range(skip):
                cursor.fetchone()

            outp = []
            for _ in range(limit):
                row = cursor.fetchone()
                if row is None:
                    break
                outp.append(row)

        finally:
            cursor.close()
            connection.close()

        return outp

    outp = asyncio.run(main_call())

    return outp


def filter_custom_browser_cov_time(schema: str, included: str, excluded: str, skip: int = 0,
                                   limit: int = 100):
    model = models.SProcFilterCustomBrowserCov

    async def model_call():
        connection = model.call(schema=schema, included=included, excluded=excluded)
        return connection

    async def main_call():
        connection = await model_call()

        try:
            cursor = connection.cursor()
            cursor.callproc(f"{schema}.filter_country_count_time")

            for _ in range(skip):
                cursor.fetchone()

            outp = []
            for _ in range(limit):
                row = cursor.fetchone()
                if row is None:
                    break
                outp.append(row)

        finally:
            cursor.close()
            connection.close()

        return outp

    outp = asyncio.run(main_call())

    return outp


def filter_custom_browser(schema: str, included: str, excluded: str, skip: int = 0,
                              limit: int = 100):
    model = models.SProcFilterCustomBrowser

    async def model_call():
        connection = model.call(schema=schema, included=included, excluded=excluded)
        return connection

    async def main_call():
        connection = await model_call()

        try:
            cursor = connection.cursor()
            cursor.callproc(f"{schema}.filter_country_count")

            for _ in range(skip):
                cursor.fetchone()

            outp = []
            for _ in range(limit):
                row = cursor.fetchone()
                if row is None:
                    break
                outp.append(row)

        finally:
            cursor.close()
            connection.close()

        return outp

    outp = asyncio.run(main_call())

    return outp


def filter_custom_browser_time(schema: str, included: str, excluded: str, skip: int = 0,
                                   limit: int = 100):
    model = models.SProcFilterCustomBrowser

    async def model_call():
        connection = model.call(schema=schema, included=included, excluded=excluded)
        return connection

    async def main_call():
        connection = await model_call()

        try:
            cursor = connection.cursor()
            cursor.callproc(f"{schema}.filter_country_count_time")

            for _ in range(skip):
                cursor.fetchone()

            outp = []
            for _ in range(limit):
                row = cursor.fetchone()
                if row is None:
                    break
                outp.append(row)

        finally:
            cursor.close()
            connection.close()

        return outp

    outp = asyncio.run(main_call())

    return outp
