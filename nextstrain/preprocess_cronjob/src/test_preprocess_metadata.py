import pytest
from .preprocess_metadata import format_date, country_to_region


def test_format_date():
    assert format_date("20001010") == "2000-10-10"


def test_format_date_ambiguous():
    assert format_date("20001000") == "2000-10-XX"
    assert format_date("20000000") == "2000-XX-XX"


def test_format_date_none():
    assert format_date(None) == None

def test_format_date_wrong_length():
    assert format_date("2000") == None
    assert format_date("200010101111") == None


def test_country_to_region():
    assert country_to_region("United Kingdom") == "Europe"
    assert country_to_region("USA") == "North America"
    assert country_to_region("Brazil") == "South America"
    assert country_to_region("Australia") == "Oceania"
    assert country_to_region("China") == "Asia"


def test_country_to_region_invalid():
    assert country_to_region("Antarctica") == "?"
    assert country_to_region("Not a Country") == "?"
    assert country_to_region(None) == "?"


def test_netherlands():
    assert country_to_region("Netherlands") == "Europe"

