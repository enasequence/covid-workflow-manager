import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from models import db_connect
from main import app
from fastapi.testclient import TestClient
from database import ALLOWED_SCHEMAS, POSTGRES_SCHEMA_KEY


client = TestClient(app)


def test_current_schema(expected_schema):
    global db_connect
    current_schema = db_connect.get_schema()
    print(f"current schema is '{current_schema}'\n")
    assert current_schema == expected_schema


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_country_samples(endp_schema_key=POSTGRES_SCHEMA_KEY):
    response = client.get(f"/country_samples/?limit=1000000&schema_key={endp_schema_key}")
    print(f"country_samples:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_human_meta_mv():
    response = client.get("/human_meta_mv/")
    print(f"human_meta_mv:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_human_meta_mv_jhd():
    response = client.get("/human_meta_mv_jhd/")
    print(f"human_meta_mv_jhd:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_lineage_def():
    response = client.get("/lineage_def/")
    print(f"lineage_def:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_lineage(endp_schema_key=POSTGRES_SCHEMA_KEY):
    response = client.get(f"/lineage/?limit=1000000&schema_key={endp_schema_key}")
    print(f"lineage:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_lineage_exception(endp_schema_key=POSTGRES_SCHEMA_KEY):
    response = client.get(f"/lineage/?limit=1000000&schema_key={endp_schema_key}")
    print(f"response.status_code: {response.status_code}\n")
    assert response.status_code == 500


def test_new_cases_jhd():
    response = client.get("/new_cases_jhd/")
    print(f"new_cases_jhd:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_variants_weekly():
    response = client.get("/variants_weekly/?limit=1000000")
    print(f"variants_weekly:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_unique_ena_run_sum():
    response = client.get("/unique_ena_run_summary/")
    print(f"unique_ena_run_summary:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_filter_custom_browser_cov(
        included='p.Asp80Ala,p.Asp215Gly',
        excluded='p.Asp77Al,p.Asp102Ala',
        endp_schema_key=POSTGRES_SCHEMA_KEY
    ):

    response = client.get(
        f"/filter_custom_browser_cov/?included={included}&excluded={excluded}&"
        f"schema_key={endp_schema_key}"
    )
    print(f"filter_custom_browser_cov:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_filter_custom_browser_cov_time(
        included='p.Asp80Ala,p.Asp215Gly',
        excluded='p.Asp77Al,p.Asp102Ala',
        endp_schema_key=POSTGRES_SCHEMA_KEY
    ):
    response = client.get(
        f"/filter_custom_browser_cov_time/?included={included}&excluded={excluded}&"
        f"schema_key={endp_schema_key}"
    )
    print(f"filter_custom_browser_cov_time:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_table_count(table_name: str):
    response = client.get(f"/table_count/?table_name={table_name}")
    print(f"table_count for {table_name}:\n{response.json()}\n")
    assert response.status_code == 200


test_root()

test_lineage()
test_current_schema(expected_schema=ALLOWED_SCHEMAS[POSTGRES_SCHEMA_KEY])

test_lineage(endp_schema_key='schema_1')
test_current_schema(expected_schema=ALLOWED_SCHEMAS['schema_1'])

test_lineage(endp_schema_key='schema_2')
test_current_schema(expected_schema=ALLOWED_SCHEMAS['schema_2'])

test_lineage(endp_schema_key=POSTGRES_SCHEMA_KEY)
test_current_schema(expected_schema=ALLOWED_SCHEMAS[POSTGRES_SCHEMA_KEY])

test_lineage_exception(endp_schema_key='schema_test')

test_country_samples(endp_schema_key='schema_1')
test_current_schema(expected_schema=ALLOWED_SCHEMAS['schema_1'])

test_country_samples(endp_schema_key='schema_2')
test_current_schema(expected_schema=ALLOWED_SCHEMAS['schema_2'])

test_country_samples()
test_current_schema(expected_schema=ALLOWED_SCHEMAS[POSTGRES_SCHEMA_KEY])

test_human_meta_mv()
test_human_meta_mv_jhd()
test_lineage_def()
test_new_cases_jhd()
test_variants_weekly()
test_unique_ena_run_sum()

test_table_count(table_name='api_lineage')
test_table_count(table_name='api_variants_weekly')

test_filter_custom_browser_cov()
test_filter_custom_browser_cov_time()
test_filter_custom_browser_cov(endp_schema_key='schema_1')
test_filter_custom_browser_cov_time(endp_schema_key='schema_1')
test_filter_custom_browser_cov(endp_schema_key='schema_2')
test_filter_custom_browser_cov_time(endp_schema_key='schema_2')
