import sqlite3
import pandas as pd
import os

print("=" * 60)
print("DAY 20 - PEER COMPARISON REPORT")
print("=" * 60)

# =====================================
# CREATE OUTPUT FOLDER
# =====================================

os.makedirs("output", exist_ok=True)

# =====================================
# CONNECT DATABASE
# =====================================

conn = sqlite3.connect("db/nifty100.db")

print("Database Connected Successfully")

# =====================================
# LOAD TABLE
# =====================================

df = pd.read_sql_query(
    "SELECT * FROM peer_percentiles",
    conn
)

conn.close()

print("\npeer_percentiles Loaded Successfully")

print("Rows :", len(df))

# =====================================
# UNIQUE PEER GROUPS
# =====================================

peer_groups = df["peer_group_name"].dropna().unique()

print("\nPeer Groups Found :", len(peer_groups))

# =====================================
# EXPORT TO EXCEL
# =====================================

excel_path = "output/peer_comparison.xlsx"

with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:

    for group in peer_groups:

        group_df = df[df["peer_group_name"] == group]

        sheet = str(group)[:31]

        group_df.to_excel(
            writer,
            sheet_name=sheet,
            index=False
        )

        print(f"{sheet} exported")

print("\n====================================")
print("peer_comparison.xlsx CREATED")
print("====================================")