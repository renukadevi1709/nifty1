import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

print("=" * 60)
print("DAY 19 - RADAR CHARTS")
print("=" * 60)

# =====================================
# CREATE OUTPUT FOLDER
# =====================================

os.makedirs("reports/radar_charts", exist_ok=True)

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

print("Rows :", len(df))

# =====================================
# REQUIRED METRICS
# =====================================

metrics = [
    "return_on_equity_pct",
    "operating_profit_margin_pct",
    "debt_to_equity",
    "asset_turnover"
]

# =====================================
# GENERATE FIRST COMPANY CHART
# =====================================

company = df.iloc[0]

values = []

for m in metrics:
    values.append(float(company[m]))

values += values[:1]

angles = np.linspace(
    0,
    2*np.pi,
    len(metrics),
    endpoint=False
).tolist()

angles += angles[:1]

plt.figure(figsize=(6,6))

ax = plt.subplot(111, polar=True)

ax.plot(angles, values)

ax.fill(angles, values, alpha=0.25)

ax.set_xticks(angles[:-1])

ax.set_xticklabels(metrics)

plt.title(company["company_id"])

plt.savefig(
    "reports/radar_charts/sample_radar.png"
)

plt.close()

print("sample_radar.png created successfully")

print("\nDAY 19 STEP 1 COMPLETED")