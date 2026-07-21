from src.cagr import calculate_cagr


def test_normal():
    value, flag = calculate_cagr(100, 200, 5)
    assert flag == "NORMAL"


def test_zero_base():
    value, flag = calculate_cagr(0, 200, 5)
    assert flag == "ZERO_BASE"


def test_turnaround():
    value, flag = calculate_cagr(-100, 200, 5)
    assert flag == "TURNAROUND"


def test_decline():
    value, flag = calculate_cagr(100, -50, 5)
    assert flag == "DECLINE_TO_LOSS"


def test_both_negative():
    value, flag = calculate_cagr(-100, -50, 5)
    assert flag == "BOTH_NEGATIVE"