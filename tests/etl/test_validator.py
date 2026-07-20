import os
import pandas as pd

def test_validation_file_exists():
    assert os.path.exists("data/output/validation_failures.csv")

def test_validation_csv():
    df = pd.read_csv("data/output/validation_failures.csv")
    assert isinstance(df, pd.DataFrame)