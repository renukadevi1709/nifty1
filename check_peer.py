import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql_query(
    "SELECT * FROM financial_ratios",
    conn
)

conn.close()

print("=" * 50)
print("Financial Ratios Table")
print("=" * 50)

print("Rows :", len(df))
print("Columns :", len(df.columns))

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())