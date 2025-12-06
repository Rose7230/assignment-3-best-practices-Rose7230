"""
AI Usage Policy:
This file contains portions of code where AI assistance was used.
AI assistance was limited to:
- Improving code style and readability
- Adding documentation (docstrings and comments)
- Ensuring compliance with best practices
All core logic, decisions, and verification were performed by the student.
"""

import csv


def get_column(file_name, column_index):
    """
    Read the given CSV file and return a list of integers from the given column.

    Parameters
    ----------
    file_name : str
        Path to the CSV file.
    column_index : int
        Zero-based index of the column to read.

    Returns
    -------
    list[int]
        List of integer values from the requested column.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    PermissionError
        If the file cannot be read due to permissions.
    """
    values = []

    try:
        with open(file_name, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            _header = next(reader, None)  # Skip header if present

            for row in reader:
                # Skip rows too short to contain the column
                if len(row) <= column_index:
                    continue

                raw_value = row[column_index]

                try:
                    values.append(int(raw_value))
                except ValueError:
                    # Skip values that cannot be converted to int
                    continue

    except FileNotFoundError:
        print(f"Error: file '{file_name}' not found.")
        raise
    except PermissionError:
        print(f"Error: no permission to read '{file_name}'.")
        raise

    return values



