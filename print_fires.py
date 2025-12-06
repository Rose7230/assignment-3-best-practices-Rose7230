"""
AI Usage Policy:
This file contains portions of code where AI assistance was used.
AI assistance was limited to improving clarity and structure.
All core logic and verification was performed by the student.
"""

import argparse
import csv
import sys
from my_utils import mean, median, std


def parse_args():
    """
    Set up command-line arguments for the script.
    """
    description = (
        "Extract values for a specified country from a CSV file. "
        "Optionally compute mean, median, or std using --op."
    )
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        "--country",
        required=True,
        help="Country name to search for.",
    )
    parser.add_argument(
        "--country_column",
        type=int,
        required=True,
        help="Column index of the country name.",
    )
    parser.add_argument(
        "--fires_column",
        type=int,
        required=True,
        help="Column index of the numeric values.",
    )
    parser.add_argument(
        "--file_name",
        required=True,
        help="CSV file to read.",
    )
    parser.add_argument(
        "--op",
        choices=["mean", "median", "std"],
        help="Statistic to compute on the values.",
    )

    return parser.parse_args()


def main():
    """
    Read the CSV file, filter rows by country, collect numeric values,
    and compute optional statistics.
    """
    args = parse_args()

    country = args.country
    col_country = args.country_column
    col_fires = args.fires_column
    fname = args.file_name
    op = args.op

    values = []

    try:
        with open(fname, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            # Skip header if present
            next(reader, None)

            for row in reader:
                if len(row) <= max(col_country, col_fires):
                    continue

                if row[col_country] == country:
                    try:
                        number = int(row[col_fires])
                        values.append(number)
                    except ValueError:
                        print(
                            f"Skipping invalid number: {row[col_fires]}",
                            file=sys.stderr,
                        )

    except FileNotFoundError:
        print(f"Error: file '{fname}' not found.", file=sys.stderr)
        return 1
    except PermissionError:
        print(f"Error: no permission to read '{fname}'.", file=sys.stderr)
        return 1

    if op is None:
        print(values)
        return 0

    if len(values) == 0:
        print("Error: no data values found for this country.", file=sys.stderr)
        return 1

    ops = {
        "mean": mean,
        "median": median,
        "std": std,
    }

    result = ops[op](values)
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
