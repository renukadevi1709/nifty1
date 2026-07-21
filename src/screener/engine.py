import sqlite3
import pandas as pd
import os

from src.screener.presets import (
    quality_compounder,
    value_pick,
    growth_accelerator,
    dividend_champion,
    debt_free_blue_chip,
    turnaround_watch
)

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql_query(
    "SELECT * FROM financial_ratios",
    conn
)

conn.close()

presets = {

    "quality_compounder": quality_compounder(df),

    "value_pick": value_pick(df),

    "growth_accelerator": growth_accelerator(df),

    "dividend_champion": dividend_champion(df),

    "debt_free_blue_chip": debt_free_blue_chip(df),

    "turnaround_watch": turnaround_watch(df)

}

os.makedirs("output", exist_ok=True)

for name, result in presets.items():

    print("="*50)
    print(name)
    print("Companies:", len(result))
    print(result.head())

    result.to_csv(
        f"output/{name}.csv",
        index=False
    )

print("\nDAY 16 COMPLETED")