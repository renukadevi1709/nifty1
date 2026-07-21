def free_cash_flow(operating_activity, investing_activity):
    return operating_activity + investing_activity


def cfo_quality_score(cfo, pat):
    if pat == 0:
        return None

    ratio = cfo / pat

    if ratio > 1:
        return "High Quality"
    elif ratio >= 0.5:
        return "Moderate"
    else:
        return "Accrual Risk"


def capex_intensity(investing_activity, sales):
    if sales == 0:
        return None

    intensity = abs(investing_activity) / sales * 100

    if intensity < 3:
        return "Asset Light"
    elif intensity <= 8:
        return "Moderate"
    else:
        return "Capital Intensive"


def fcf_conversion_rate(fcf, operating_profit):
    if operating_profit == 0:
        return None

    return (fcf / operating_profit) * 100

def capital_allocation_pattern(cfo, cfi, cff, cfo_pat_ratio=None):
    cfo_sign = "+" if cfo >= 0 else "-"
    cfi_sign = "+" if cfi >= 0 else "-"
    cff_sign = "+" if cff >= 0 else "-"

    if (cfo_sign, cfi_sign, cff_sign) == ("+", "-", "-"):
        if cfo_pat_ratio is not None and cfo_pat_ratio > 1:
            label = "Shareholder Returns"
        else:
            label = "Reinvestor"

    elif (cfo_sign, cfi_sign, cff_sign) == ("+", "+", "-"):
        label = "Liquidating Assets"

    elif (cfo_sign, cfi_sign, cff_sign) == ("-", "+", "+"):
        label = "Distress Signal"

    elif (cfo_sign, cfi_sign, cff_sign) == ("-", "-", "+"):
        label = "Growth Funded by Debt"

    elif (cfo_sign, cfi_sign, cff_sign) == ("+", "+", "+"):
        label = "Cash Accumulator"

    elif (cfo_sign, cfi_sign, cff_sign) == ("-", "-", "-"):
        label = "Pre-Revenue"

    elif (cfo_sign, cfi_sign, cff_sign) == ("+", "-", "+"):
        label = "Mixed"

    else:
        label = "Unknown"

    return {
        "cfo_sign": cfo_sign,
        "cfi_sign": cfi_sign,
        "cff_sign": cff_sign,
        "pattern_label": label
    }