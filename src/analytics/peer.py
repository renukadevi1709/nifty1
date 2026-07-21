import sqlite3
import pandas as pd

print("=" * 60)
print("DAY 18 - PEER ANALYSIS")
print("=" * 60)

# =====================================
# CONNECT DATABASE
# =====================================

conn = sqlite3.connect("db/nifty100.db")

print("Database Connected Successfully")

# =====================================
# LOAD TABLE
# =====================================

df = pd.read_sql_query(
    "SELECT * FROM financial_ratios",
    conn
)

conn.close()

print("\nfinancial_ratios Loaded Successfully")

print("\nRows :", len(df))
print("Columns :", len(df.columns))

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())


print("\nChecking Required Columns...\n")

required_columns = [
    "company_id",
    "year",
    "return_on_equity_pct",
    "debt_to_equity"
]

for col in required_columns:

    if col in df.columns:
        print(f"{col} --> OK")

    else:
        print(f"{col} --> MISSING")

        print("\nAll Columns:\n")

for col in df.columns:
    print(col)



    # =====================================
# LOAD PEER GROUPS
# =====================================

peer_df = pd.read_excel("data/raw/peer_groups.xlsx")

print("\nPeer Groups Loaded Successfully")

print("Rows :", len(peer_df))
print("Columns :", len(peer_df.columns))

print("\nPeer Group Columns:")
print(peer_df.columns.tolist())

print("\nFirst 5 Rows:")
print(peer_df.head())

# =====================================
# MERGE FINANCIAL RATIOS + PEER GROUPS
# =====================================

merged_df = pd.merge(
    df,
    peer_df,
    on="company_id",
    how="left"
)

print("\nMerged Successfully")

print("Rows :", len(merged_df))
print("Columns :", len(merged_df.columns))

print("\nMerged Columns:")
print(merged_df.columns.tolist())

print("\nFirst 5 Rows:")
print(merged_df.head())


# =====================================
# PEER GROUP COUNT
# =====================================

print("\nPeer Groups Summary")
print("=" * 50)

print(
    merged_df["peer_group_name"].value_counts()
)


# =====================================
# ROE PERCENTILE RANK
# =====================================

merged_df["roe_percentile"] = (
    merged_df
    .groupby("peer_group_name")["return_on_equity_pct"]
    .rank(pct=True) * 100
)

print("\nROE Percentile Calculated Successfully")

print(
    merged_df[
        [
            "company_id",
            "peer_group_name",
            "return_on_equity_pct",
            "roe_percentile"
        ]
    ].head(10)
)



# =====================================
# SAVE TO SQLITE
# =====================================

conn = sqlite3.connect("db/nifty100.db")

merged_df.to_sql(
    "peer_percentiles",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\npeer_percentiles table created successfully.")