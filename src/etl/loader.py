import os
import pandas as pd

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

excel_files = [
    f for f in os.listdir(RAW_FOLDER)
    if f.endswith(".xlsx") or f.endswith(".xls")
]

print(f"Found {len(excel_files)} Excel files.\n")

for file in excel_files:
    file_path = os.path.join(RAW_FOLDER, file)

    try:
        df = pd.read_excel(file_path)

        # Clean column names
        df.columns = (
            df.columns.astype(str)
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        output_file = os.path.join(
            PROCESSED_FOLDER,
            file.replace(".xlsx", "_clean.csv").replace(".xls", "_clean.csv")
        )

        df.to_csv(output_file, index=False)

        print(f"Loaded: {file}  ->  {output_file}")

    except Exception as e:
        print(f"Error loading {file}: {e}")