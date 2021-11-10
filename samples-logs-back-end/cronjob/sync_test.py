from .sync import set_lineage


def test_set_lineage():
    record = {"accession": "XY123"}
    crossref = {"XY123": "B"}
    expected = record | {"lineage": "B", "has_lineage": True}
    assert set_lineage(record, crossref) == expected


def test_set_lineage_not_found():
    record = {"accession": "XY123"}
    crossref = {}
    expected = record | {"has_lineage": False}
    assert set_lineage(record, crossref) == expected


