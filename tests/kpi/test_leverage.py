import os
import sys

sys.path.insert(0, os.path.abspath("."))
from src.ratios import (
    debt_to_equity,
    interest_coverage_ratio,
    icr_label,
    high_leverage_flag,
    net_debt,
    asset_turnover,
)

def test_debt_free():
    assert debt_to_equity(0, 100, 200) == 0

def test_interest_zero():
    assert interest_coverage_ratio(100, 20, 0) is None

def test_icr_label():
    assert icr_label(None) == "Debt Free"

def test_high_leverage():
    assert high_leverage_flag(6, "IT") is True

def test_net_debt():
    assert net_debt(500, 100) == 400

def test_asset_turnover():
    assert asset_turnover(1000, 500) == 2.0

def test_asset_turnover_zero():
    assert asset_turnover(1000, 0) is None