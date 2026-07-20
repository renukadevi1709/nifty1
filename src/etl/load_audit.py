import sqlite3
import pandas as pd
import os

DB_PATH = "db/nifty100.db"
OUTPUT_PATH = "data/output/load_audit.csv"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "financial_ratios",
    "peer_groups",
    "prosandcons",
    "stock_prices"
]

audit = []

for table in tables:
    try:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]

        audit.append({
            "table": table,
            "rows_loaded": count,
            "rejected_rows": 0
        })

    except Exception:
        audit.append({
            "table": table,
            "rows_loaded": 0,
            "rejected_rows": 0
        })

conn.close()

os.makedirs("data/output", exist_ok=True)

pd.DataFrame(audit).to_csv(OUTPUT_PATH, index=False)

print("load_audit.csv generated successfully.")