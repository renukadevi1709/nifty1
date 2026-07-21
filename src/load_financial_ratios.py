import sqlite3

# Connect to database
conn = sqlite3.connect("db/nifty100.db")
cur = conn.cursor()

print("Connected Successfully\n")

# Show table structure
cur.execute("PRAGMA table_info(financial_ratios)")
columns = cur.fetchall()

print("Financial Ratios Table Columns:")
for col in columns:
    print(col)

print("\n---------------------------")

# Count rows in financial_ratios table
cur.execute("SELECT COUNT(*) FROM financial_ratios")
row_count = cur.fetchone()[0]

print("Rows in financial_ratios table:", row_count)

# Close connection
conn.close()