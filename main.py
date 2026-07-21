import yaml
import sqlite3
import pandas as pd
import os
from src.screener.presets import quality_compounder

# =====================================
# LOAD CONFIG
# =====================================

with open("config/screener_config.yaml", "r") as file:
    config = yaml.safe_load(file)

print("=" * 60)
print("SCREENER CONFIG LOADED")
print("=" * 60)
print(config)

# =====================================
# CONNECT DATABASE
# =====================================

conn = sqlite3.connect("db/nifty100.db")
print("\nDatabase Connected Successfully.")

# =====================================
# LOAD financial_ratios TABLE
# =====================================

df = pd.read_sql_query("SELECT * FROM financial_ratios", conn)
conn.close()
print("\nfinancial_ratios loaded.")

# =====================================
# BASIC INFO
# =====================================

print("\nRows :", len(df))
print("Columns :", len(df.columns))
print("\nColumns")
print(df.columns.tolist())
print("\nFirst 5 Rows")
print(df.head())

# =====================================
# MISSING VALUES
# =====================================

print("\nMissing Values")
print(df.isnull().sum())

# =====================================
# DATA TYPES
# =====================================

print("\nData Types")
print(df.dtypes)

# =====================================
# QUALITY COMPOUNDER FILTER
# =====================================

filtered_df = df.copy()

filtered_df = filtered_df[
    filtered_df["return_on_equity_pct"] >= config["quality_compounder"]["roe_min"]
]

filtered_df = filtered_df[
    filtered_df["debt_to_equity"] <= config["quality_compounder"]["debt_equity_max"]
]

filtered_df = filtered_df[
    filtered_df["free_cash_flow_cr"] > config["quality_compounder"]["fcf_min"]
]

print("\nAfter Filter")
print(filtered_df.head())
print("Companies :", len(filtered_df))

# =====================================
# COMPOSITE SCORE
# =====================================

filtered_df["composite_quality_score"] = (
    filtered_df["return_on_equity_pct"].fillna(0) * 0.50 +
    filtered_df["operating_profit_margin_pct"].fillna(0) * 0.30 +
    filtered_df["asset_turnover"].fillna(0) * 20
)

print("\nComposite Score Added")
print(filtered_df[["company_id", "year", "return_on_equity_pct", "composite_quality_score"]].head())

# =====================================
# SORT
# =====================================

filtered_df = filtered_df.sort_values(by="composite_quality_score", ascending=False)

print("\nTop Companies")
print(filtered_df[["company_id", "year", "composite_quality_score"]].head(10))

# =====================================
# EXPORT
# =====================================

os.makedirs("output", exist_ok=True)
filtered_df.to_csv("output/quality_compounder.csv", index=False)
print("\nquality_compounder.csv Generated Successfully")
print("\nDAY 15 COMPLETED SUCCESSFULLY")

# =====================================
# QUALITY COMPOUNDER PRESET
# =====================================

print("\nApplying Quality Compounder Preset...")
result = quality_compounder(df)
print("Companies Found :", len(result))
print(result.head())

result.to_csv("output/quality_compounder.csv", index=False)
print("\nquality_compounder.csv created successfully.")
