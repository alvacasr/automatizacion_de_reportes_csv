"""
process_files.py

Loads multiple CSV files from a directory and merges them into one dataset.
"""

import pandas as pd
from pathlib import Path

INPUT_DIR = Path("input_data")
OUTPUT_FILE = Path("output/merged_data.csv")


def load_csv_files():
    """Load all CSV files from the input directory."""
    
    if not INPUT_DIR.exists():
        raise FileNotFoundError(f"Input directory not found: {INPUT_DIR}")

    csv_files = list(INPUT_DIR.glob("*.csv"))

    if not csv_files:
        raise ValueError("No CSV files found in input directory.")

    print(f"Found {len(csv_files)} CSV files.")

    dataframes = []

    for file in csv_files:
        print(f"Loading {file.name}")
        df = pd.read_csv(file)
        df["source_file"] = file.name
        dataframes.append(df)

    return dataframes


def merge_data(dataframes):
    """Merge all DataFrames."""
    
    merged = pd.concat(dataframes, ignore_index=True)

    return merged


def save_merged_data(df):
    """Save merged dataset."""

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Merged dataset saved to {OUTPUT_FILE}")


def main():

    dfs = load_csv_files()

    merged = merge_data(dfs)

    save_merged_data(merged)


if __name__ == "__main__":
    main()