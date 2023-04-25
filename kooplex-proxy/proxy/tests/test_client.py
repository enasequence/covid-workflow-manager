import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import models
from main import app
from fastapi.testclient import TestClient
from database import ALLOWED_SCHEMAS


client = TestClient(app)


def test_current_schema_of_the_model(model, expected_schema):
    current_schema = model.get_schema()
    print(f"current schema is '{current_schema}' for object {model.__table__.name}\n")
    assert current_schema == expected_schema


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_country_samples(endp_schema_key='schema_1'):
    response = client.get(f"/country_samples/?schema_key={endp_schema_key}")
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


def test_lineage():
    response = client.get("/lineage/")
    print(f"lineage:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_new_cases_jhd():
    response = client.get("/new_cases_jhd/")
    print(f"new_cases_jhd:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_variants_weekly():
    response = client.get("/variants_weekly/")
    print(f"variants_weekly:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_unique_ena_run_sum():
    response = client.get("/unique_ena_run_sum/")
    print(f"unique_ena_run_sum:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_filter_custom_browser_cov():
    response = client.get("/filter_custom_browser_cov/")
    print(f"filter_custom_browser_cov:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_filter_custom_browser_cov_time():
    response = client.get("/filter_custom_browser_cov_time/")
    print(f"filter_custom_browser_cov_time:\nlen: {len(response.json())}\n{response.json()[:5]}\n")
    assert response.status_code == 200


test_root()

test_country_samples()
test_current_schema_of_the_model(models.MViewCountrySamples, expected_schema=ALLOWED_SCHEMAS['schema_1'])

test_country_samples(endp_schema_key='schema_2')
test_current_schema_of_the_model(models.MViewCountrySamples, expected_schema=ALLOWED_SCHEMAS['schema_2'])

test_country_samples(endp_schema_key='schema_1')
test_current_schema_of_the_model(models.MViewCountrySamples, expected_schema=ALLOWED_SCHEMAS['schema_1'])

test_country_samples(endp_schema_key='schema_test')

test_human_meta_mv()
test_human_meta_mv_jhd()
test_lineage_def()
test_lineage()
test_new_cases_jhd()
test_variants_weekly()
test_unique_ena_run_sum()

test_filter_custom_browser_cov()
test_filter_custom_browser_cov_time()
