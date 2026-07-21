import sqlite3

# Connect Database
conn = sqlite3.connect("db/nifty100.db")
cur = conn.cursor()

print("Connected Successfully\n")

# ----------------------------
# Financial Ratios Row Count
# ----------------------------
cur.execute("SELECT COUNT(*) FROM financial_ratios")
rows = cur.fetchone()[0]

print(f"Financial Ratios Rows : {rows}")

# ----------------------------
# ROE Check
# ----------------------------
print("\nChecking ROE values...")

cur.execute("""
SELECT company_id,
       year,
       return_on_equity_pct
FROM financial_ratios
LIMIT 10
""")

roe_data = cur.fetchall()

for row in roe_data:
    print(row)

# ----------------------------
# Debt to Equity Check
# ----------------------------
print("\nChecking Debt to Equity...")

cur.execute("""
SELECT company_id,
       year,
       debt_to_equity
FROM financial_ratios
LIMIT 10
""")

de_data = cur.fetchall()

for row in de_data:
    print(row)

# ----------------------------
# Interest Coverage Check
# ----------------------------
print("\nChecking Interest Coverage...")

cur.execute("""
SELECT company_id,
       year,
       interest_coverage
FROM financial_ratios
LIMIT 10
""")

interest_data = cur.fetchall()

for row in interest_data:
    print(row)

conn.close()

print("\nValidation Completed Successfully.")