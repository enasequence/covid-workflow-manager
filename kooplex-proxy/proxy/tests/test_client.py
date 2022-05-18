from fastapi.testclient import TestClient

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_covid_country_weekly():
    response = client.get("/covid_country_weekly/")
    assert response.status_code == 200


def test_read_vcf_all():
    response = client.get("/vcf_all/")
    assert response.status_code == 200


def test_read_cov():
    response = client.get("/cov/")
    assert response.status_code == 200


def test_read_meta():
    response = client.get("/meta/")
    assert response.status_code == 200


def test_read_lineage_def():
    response = client.get("/lineage_def/")
    assert response.status_code == 200


def test_read_unique_cov():
    response = client.get("/unique_cov/")
    assert response.status_code == 200


def test_read_unique_vcf():
    response = client.get("/unique_vcf/")
    assert response.status_code == 200


def test_read_country_samples():
    response = client.get("/country_samples/")
    assert response.status_code == 200


def test_read_lineage_def_description():
    response = client.get("/lineage_def_description/")
    assert response.status_code == 200


def test_read_lineage():
    response = client.get("/lineage/")
    assert response.status_code == 200


def test_read_new_cases():
    response = client.get("/new_cases/")
    assert response.status_code == 200


def test_read_variants_weekly():
    response = client.get("/variants_weekly/")
    assert response.status_code == 200


def test_read_worldplot_data():
    response = client.get("/worldplot_data/")
    assert response.status_code == 200


test_read_root()
test_read_covid_country_weekly()
test_read_vcf_all()
test_read_cov()
test_read_meta()
test_read_lineage_def()
test_read_unique_cov()
test_read_unique_vcf()
test_read_country_samples()
test_read_lineage_def_description()
test_read_lineage()
test_read_new_cases()
test_read_variants_weekly()
test_read_worldplot_data()
