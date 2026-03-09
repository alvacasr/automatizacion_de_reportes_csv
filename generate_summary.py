"""
generate_summary.py

Creates summary statistics from merged dataset.
"""

import pandas as pd
from pathlib import Path

INPUT_FILE = Path("output/merged_data.csv")
OUTPUT_FILE = Path("output/summary_report.csv")


def load_data():

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            "Merged dataset not found. Run process_files.py first."
        )

    print("Loading merged dataset...")
    df = pd.read_csv(INPUT_FILE)

    return df


def generate_summary(df):

    print("Generating summary report...")

    summary = df.groupby("product").agg(
        total_sales=("sales", "sum"),
        avg_sales=("sales", "mean"),
        transactions=("sales", "count")
    )

    summary = summary.sort_values("total_sales", ascending=False)

    return summary


def save_summary(summary):

    summary.to_csv(OUTPUT_FILE)

    print(f"Summary report saved to {OUTPUT_FILE}")


def main():

    df = load_data()

    summary = generate_summary(df)

    save_summary(summary)


if __name__ == "__main__":
    main()