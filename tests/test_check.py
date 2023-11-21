import os
import pytest
from CheckOnVirustotal import check

def test_correct_hash():
    assert check.create_file_hash("tests/file with spaces.txt") == "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855"

def test_wrong_hash():
    assert check.create_file_hash("tests/file with spaces.txt") != "AAAAAAAD74E"