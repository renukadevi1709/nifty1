import os
import pandas as pd

# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

os.makedirs("output", exist_ok=True)

# ==========================================
# CSV FILES
# ==========================================

files = {
    "Quality Compounder": "output/quality_compounder.csv",
    "Value Pick": "output/value_pick.csv",
    "Growth Accelerator": "output/growth_accelerator.csv",
    "Dividend Champion": "output/dividend_champion.csv",
    "Debt Free Blue Chip": "output/debt_free_blue_chip.csv",
    "Turnaround Watch": "output/turnaround_watch.csv"
}

# ==========================================
# CREATE EXCEL
# ==========================================

excel_path = "output/screener_output.xlsx"

with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:

    for sheet_name, file_path in files.items():

        if os.path.exists(file_path):

            df = pd.read_csv(file_path)

            df.to_excel(
                writer,
                sheet_name=sheet_name,
                index=False
            )

            print(f"{sheet_name} exported.")

        else:

            print(f"{file_path} NOT FOUND")

print("\n===================================")
print("screener_output.xlsx CREATED")
print("===================================")