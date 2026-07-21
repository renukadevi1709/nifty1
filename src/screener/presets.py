import pandas as pd


# ------------------------------------
# Quality Compounder
# ------------------------------------
def quality_compounder(df):

    filtered = df.copy()

    filtered = filtered[
        (filtered["return_on_equity_pct"] > 15) &
        (filtered["debt_to_equity"] < 1) &
        (filtered["free_cash_flow_cr"] > 0)
    ]

    return filtered


# ------------------------------------
# Value Pick
# ------------------------------------
def value_pick(df):

    filtered = df.copy()

    return filtered


# ------------------------------------
# Growth Accelerator
# ------------------------------------
def growth_accelerator(df):

    filtered = df.copy()

    return filtered


# ------------------------------------
# Dividend Champion
# ------------------------------------
def dividend_champion(df):

    filtered = df.copy()

    return filtered


# ------------------------------------
# Debt Free Blue Chip
# ------------------------------------
def debt_free_blue_chip(df):

    filtered = df.copy()

    filtered = filtered[
        (filtered["debt_to_equity"] == 0) &
        (filtered["return_on_equity_pct"] > 12)
    ]

    return filtered


# ------------------------------------
# Turnaround Watch
# ------------------------------------
def turnaround_watch(df):

    filtered = df.copy()

    return filtered