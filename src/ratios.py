def net_profit_margin(net_profit, sales):
    if sales == 0:
        return None
    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    if sales == 0:
        return None
    return (operating_profit / sales) * 100


def return_on_equity(net_profit, equity, reserves):
    total_equity = equity + reserves
    if total_equity <= 0:
        return None
    return (net_profit / total_equity) * 100


def return_on_capital_employed(ebit, equity, reserves, total_debt):
    """
    ROCE = EBIT / Capital Employed * 100
    Capital Employed = equity + reserves + total_debt
    """
    capital_employed = equity + reserves + total_debt
    if capital_employed <= 0:
        return None
    return (ebit / capital_employed) * 100


def return_on_assets(net_profit, total_assets):
    if total_assets == 0:
        return None
    return (net_profit / total_assets) * 100


def debt_to_equity(total_debt, equity, reserves):
    total_equity = equity + reserves
    if total_equity <= 0:
        return None
    return total_debt / total_equity


def interest_coverage_ratio(ebit, depreciation, interest):
    if interest == 0:
        return None
    return (ebit + depreciation) / interest


def icr_label(icr):
    if icr is None:
        return "Debt Free"
    if icr >= 3:
        return "Safe"
    if icr >= 1:
        return "Moderate"
    return "Risky"


def high_leverage_flag(debt_to_eq, sector):
    threshold = 1.0 if sector in ("IT", "FMCG", "Pharma") else 2.0
    return debt_to_eq > threshold


def net_debt(total_debt, cash):
    return total_debt - cash


def asset_turnover(sales, total_assets):
    if total_assets == 0:
        return None
    return sales / total_assets