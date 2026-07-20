import re

def normalize_year(year):
    """
    Convert different year formats into a 4-digit year.
    Examples:
        FY22 -> 2022
        FY2023 -> 2023
        2024-25 -> 2025
        2022 -> 2022
    """

    if year is None:
        return None

    year = str(year).strip()

    # FY22
    if re.match(r"^FY\d{2}$", year):
        return 2000 + int(year[-2:])

    # FY2023
    if re.match(r"^FY\d{4}$", year):
        return int(year[-4:])

    # 2024-25
    if re.match(r"^\d{4}-\d{2}$", year):
        return 2000 + int(year[-2:])

    # 2022
    if year.isdigit():
        return int(year)

    return None


def normalize_ticker(ticker):
    """
    Normalize stock ticker.
    Examples:
        tcs -> TCS
        TCS.NS -> TCS
        TCS BO -> TCS
    """

    if ticker is None:
        return None

    ticker = str(ticker).upper().strip()

    ticker = ticker.replace(".NS", "")
    ticker = ticker.replace(" BO", "")

    return ticker