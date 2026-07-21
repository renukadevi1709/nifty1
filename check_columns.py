import pandas as pd

df = pd.read_csv("output/quality_compounder.csv")

print("Columns:")
print(df.columns.tolist())

print("\nTotal Columns:", len(df.columns))