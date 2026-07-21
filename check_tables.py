import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM companies")
print(cur.fetchone())

conn.close()