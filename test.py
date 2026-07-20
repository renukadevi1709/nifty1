from src.etl.normaliser import normalize_year, normalize_ticker

print(normalize_year("FY22"))
print(normalize_year("FY2023"))
print(normalize_year("2024-25"))

print(normalize_ticker("tcs"))
print(normalize_ticker("TCS.NS"))
print(normalize_ticker("TCS BO"))