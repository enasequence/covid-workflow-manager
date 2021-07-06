from .sync import deduplicate_dicts, reorder_top_records, set_lineage


def test_deduplicate_dicts():
    entry = {"name": "foo"}
    entry2 = {"name": "bar"}
    assert deduplicate_dicts([entry, entry]) == [entry]
    assert deduplicate_dicts([entry, entry, entry2]) == [entry, entry2]


def test_reorder_top_records():
    pinned_entry = [{"name": "top foo"}]
    entries = [
        {"name": "bar"},
        {"name": "top foo"},
        {"name": "baz"},
    ]
    expected = [
        {"name": "top foo"},
        {"name": "bar"},
        {"name": "baz"},
    ]
    assert reorder_top_records(entries, pinned_entry) == expected


def test_set_lineage():
    record = {"acc": "XY123"}
    crossref = {"XY123": "B"}
    expected = {**record, "lineage": "B", "has_lineage": True}
    assert set_lineage(record, crossref) == expected


def test_set_lineage_not_found():
    record = {"acc": "XY123"}
    expected = {**record, "has_lineage": False}
    assert set_lineage(record, {}) == expected
