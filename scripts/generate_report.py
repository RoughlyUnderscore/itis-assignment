import argparse
from pathlib import Path

import pandas as pd

from perfanalysis.analyzer import analyze_students
from perfanalysis.report import generate_html_report


def main(input_path: str, output_path: str) -> None:
    df = pd.read_csv(input_path)

    analysis = analyze_students(df)
    html = generate_html_report(analysis)

    Path(output_path).write_text(html, encoding="utf-8")

    print(f"Report generated: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate student performance report"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to input CSV file"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path to output HTML report"
    )

    args = parser.parse_args()

    main(args.input, args.output)
