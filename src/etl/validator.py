import os
import pandas as pd

PROCESSED_FOLDER = "data/processed"
OUTPUT_FOLDER = "data/output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

failures = []

csv_files = [
    f for f in os.listdir(PROCESSED_FOLDER)
    if f.endswith(".csv")
]

for file in csv_files:
    path = os.path.join(PROCESSED_FOLDER, file)

    df = pd.read_csv(path)

    # DQ-14: Null values in columns
    null_cols = df.columns[df.isnull().any()]

    for col in null_cols:
        failures.append({
            "file": file,
            "rule": "DQ-14",
            "column": col,
            "severity": "WARNING"
        })

validation = pd.DataFrame(failures)

output_file = os.path.join(
    OUTPUT_FOLDER,
    "validation_failures.csv"
)

validation.to_csv(output_file, index=False)

print("Validation completed.")
print(f"Failures found: {len(validation)}")