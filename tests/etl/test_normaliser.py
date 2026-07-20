import sys
import os

sys.path.insert(0, os.path.abspath("."))

from src.etl.normaliser import normalize_year, normalize_ticker

def test_normalize_year():
    assert normalize_year("FY22") == 2022
    assert normalize_year("FY2023") == 2023
    assert normalize_year("2024-25") == 2025

def test_normalize_ticker():
    assert normalize_ticker("tcs") == "TCS"
    assert normalize_ticker("TCS.NS") == "TCS"
    assert normalize_ticker("TCS BO") == "TCS"