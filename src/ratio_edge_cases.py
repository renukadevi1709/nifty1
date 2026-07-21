import sqlite3
import os

print("Program Started...")

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# Connect to database
conn = sqlite3.connect("db/nifty100.db")
cur = conn.cursor()

print("Connected Successfully")

# Create/Open log file
with open("output/ratio_edge_cases.log", "w") as log:

    log.write("=====================================\n")
    log.write("      RATIO EDGE CASES REPORT\n")
    log.write("=====================================\n\n")

    # -------------------------------
    # Total Rows
    # -------------------------------
    cur.execute("SELECT COUNT(*) FROM financial_ratios")
    total_rows = cur.fetchone()[0]

    log.write(f"Total Rows in financial_ratios : {total_rows}\n\n")

    # -------------------------------
    # Negative ROE
    # -------------------------------
    log.write("1. Negative ROE\n")

    cur.execute("""
        SELECT company_id, year, return_on_equity_pct
        FROM financial_ratios
        WHERE return_on_equity_pct < 0
    """)

    rows = cur.fetchall()

    if rows:
        for row in rows:
            log.write(f"{row}\n")
    else:
        log.write("No Negative ROE Found.\n")

    log.write("\n")

    # -------------------------------
    # High Debt-to-Equity
    # -------------------------------
    log.write("2. High Debt-to-Equity (>5)\n")

    cur.execute("""
        SELECT company_id, year, debt_to_equity
        FROM financial_ratios
        WHERE debt_to_equity > 5
    """)

    rows = cur.fetchall()

    if rows:
        for row in rows:
            log.write(f"{row}\n")
    else:
        log.write("No High Debt Companies Found.\n")

    log.write("\n")

    # -------------------------------
    # Low Interest Coverage
    # -------------------------------
    log.write("3. Interest Coverage < 1.5\n")

    cur.execute("""
        SELECT company_id, year, interest_coverage
        FROM financial_ratios
        WHERE interest_coverage < 1.5
        AND interest_coverage IS NOT NULL
    """)

    rows = cur.fetchall()

    if rows:
        for row in rows:
            log.write(f"{row}\n")
    else:
        log.write("No Low Interest Coverage Found.\n")

    log.write("\n")

    # -------------------------------
    # End
    # -------------------------------
    log.write("=====================================\n")
    log.write("Validation Completed Successfully.\n")
    log.write("=====================================\n")

conn.close()

print("Database Closed")
print("ratio_edge_cases.log created successfully.")
print("Program Finished")