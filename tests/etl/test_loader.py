import os

def test_processed_folder_exists():
    assert os.path.exists("data/processed")

def test_raw_folder_exists():
    assert os.path.exists("data/raw")

def test_output_folder_exists():
    assert os.path.exists("data/output")