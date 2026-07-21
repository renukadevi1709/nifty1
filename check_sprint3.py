import sqlite3
import pandas as pd

print("=" * 60)
print("SPRINT 3 FINAL VERIFICATION")
print("=" * 60)

conn = sqlite3.connect("db/nifty100.db")

# financial_ratios
financial = pd.read_sql_query(
    "SELECT COUNT(*) AS rows FROM financial_ratios",
    conn
)

print("\nfinancial_ratios Rows :", financial["rows"][0])

# peer_percentiles
peer = pd.read_sql_query(
    "SELECT COUNT(*) AS rows FROM peer_percentiles",
    conn
)

print("peer_percentiles Rows :", peer["rows"][0])

conn.close()

print("\nChecking Output Files...")

import os

files = [
    "output/screener_output.xlsx",
    "output/peer_comparison.xlsx",
    "reports/radar_charts/sample_radar.png"
]

for file in files:
    if os.path.exists(file):
        print("✔", file)
    else:
        print("✘", file)

print("\nSPRINT 3 VERIFICATION COMPLETED")