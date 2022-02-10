from .process_fasta import extract_id
import pytest

def test_extract_id():
    assert extract_id(">foo|bar|baz\n") == ">bar\n"

