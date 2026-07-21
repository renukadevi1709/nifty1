from src.cashflow_kpis import capital_allocation_pattern
from src.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion_rate,
)


def test_free_cash_flow():
    assert free_cash_flow(500, -200) == 300


def test_cfo_quality_high():
    assert cfo_quality_score(120, 100) == "High Quality"


def test_cfo_quality_moderate():
    assert cfo_quality_score(70, 100) == "Moderate"


def test_cfo_quality_low():
    assert cfo_quality_score(30, 100) == "Accrual Risk"


def test_capex_intensity():
    assert capex_intensity(-20, 1000) == "Asset Light"


def test_fcf_conversion():
    assert fcf_conversion_rate(300, 600) == 50.0


def test_fcf_zero():
    assert fcf_conversion_rate(100, 0) is None

def test_reinvestor():
    result = capital_allocation_pattern(100, -50, -20)
    assert result["pattern_label"] == "Reinvestor"


def test_shareholder_returns():
    result = capital_allocation_pattern(100, -50, -20, 1.5)
    assert result["pattern_label"] == "Shareholder Returns"


def test_distress():
    result = capital_allocation_pattern(-100, 50, 20)
    assert result["pattern_label"] == "Distress Signal"


def test_cash_accumulator():
    result = capital_allocation_pattern(100, 50, 20)
    assert result["pattern_label"] == "Cash Accumulator"