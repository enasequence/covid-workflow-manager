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
    print(f"covid_country_weekly:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_read_vcf_all():
    response = client.get("/vcf_all/")
    print(f"vcf_all:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_read_cov():
    response = client.get("/cov/")
    print(f"cov:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_read_meta():
    response = client.get("/meta/")
    print(f"meta:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_read_lineage_def():
    response = client.get("/lineage_def/")
    print(f"lineage_def:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_read_unique_cov():
    response = client.get("/unique_cov/")
    print(f"unique_cov:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_read_unique_vcf():
    response = client.get("/unique_vcf/")
    print(f"unique_vcf:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_read_country_samples():
    response = client.get("/country_samples/")
    print(f"country_samples:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_read_lineage_def_description():
    response = client.get("/lineage_def_description/")
    print(f"lineage_def_description:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_read_lineage():
    response = client.get("/lineage/")
    print(f"lineage:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_read_new_cases():
    response = client.get("/new_cases/")
    print(f"new_cases:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_read_variants_weekly():
    response = client.get("/variants_weekly/")
    print(f"variants_weekly:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_read_worldplot_data():
    response = client.get("/worldplot_data/")
    print(f"worldplot_data:\n{response.json()[:5]}\n")
    assert response.status_code == 200


def test_views():
    response = client.get("/check_views/")
    print(f"check_views:\n{response.json()}/n")
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
test_views()
