import os
import sqlite3
import pandas as pd

DB_PATH = "db/nifty100.db"
SCHEMA_PATH = "db/schema.sql"
PROCESSED_FOLDER = "data/processed"

# Create database connection
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Execute schema.sql
with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    cursor.executescript(f.read())

print("Database and tables created successfully.")

# Load all processed CSV files
for file in os.listdir(PROCESSED_FOLDER):
    if file.endswith(".csv"):

        table_name = file.replace("_clean.csv", "")

        df = pd.read_csv(os.path.join(PROCESSED_FOLDER, file))

        try:
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"Loaded: {table_name}")
        except Exception as e:
            print(f"Error loading {table_name}: {e}")

conn.commit()
conn.close()

print("All tables loaded successfully.")