"""
AI Usage Policy:
This file contains portions of code where AI assistance was used.
AI assistance was limited to:
- Improving clarity and structure
- Ensuring correct use of argparse, main(), and error handling
All core logic and verification were performed by the student.
"""

import argparse
import csv
import sys

from my_utils import mean, median, std


def parse_args():
    """
    Set up command-line arguments for the script.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Extract numeric values for a specified country from a CSV file, "
            "and optionally compute a statistic (mean, median, std)."
        )
    )

    parser.add_argument("--country", required=True,
                        help="Country name to search for.")
    parser.add_argument("--country_column", type=int, required=True,
                        help="Column index where country names appear.")
    parser.add_argument("--fires_column", type=int, required=True,
                        help="Column index of the numeric values to extract.")
    parser.add_argument("--file_name", required=True,
                        help="CSV file to read from.")
    parser.add_argument(
        "--op",
        choices=["mean", "median", "std"],
        help="If given, compute this operation on the values instead of printing the list.",
    )

    return parser.parse_args()


def main():
    """
    Reads the CSV file, filters rows by the given country,
    collects numbers from the specified column, and either
    prints the list or a statistic chosen with --op.
    """
    args = parse_args()

    country_wanted = args.country
    country_col = args.country_column
    fires_col = args.fires_column
    file_name = args.file_name
    operation = args.op

    values = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            # Skip header row if present
            _header = next(reader, None)

            for row in reader:
                # Skip rows that are too short
                if len(row) <= max(country_col, fires_col):
                    continue

                # Check if row matches the target country
                if row[country_col] == country_wanted:
                    raw_value = row[fires_col]

                    # Convert the value to an integer
                    try:
                        number = int(raw_value)
                        values.append(number)
                    except ValueError:
                        # Skip values that cannot be converted
                        print(f"Skipping invalid number: {raw_value}", file=sys.stderr)
                        continue

    except FileNotFoundError:
        print(f"Error: file '{file_name}' not found.", file=sys.stderr)
        return 1
    except PermissionError:
        print(f"Error: no permission to read '{file_name}'.", file=sys.stderr)
        return 1

    # If no operation is requested, keep the old behavior
    if operation is None:
        print(values)
        return 0

    # If an operation is requested but there is no data, treat that as an error
    if len(values) == 0:
        print("Error: no data values found for the given country.", file=sys.stderr)
        return 1

    # Compute the requested statistic
    try:
        if operation == "mean":
            result = mean(values)
        elif operation == "median":
            result = median(values)
        elif operation == "std":
            result = std(values)
        else:
            print(f"Unknown operation: {operation}", file=sys.stderr)
            return 1
    except ValueError as exc:
        print(f"Error while computing {operation}: {exc}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
