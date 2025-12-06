"""
AI Usage Policy:
This file contains portions of code where AI assistance was used.
AI assistance was limited to:
- Improving code style and readability
- Ensuring compliance with best practices
All core logic, decisions, and verification were performed by the student.
"""

import csv


def get_column(file_name, column_index):
    """
    Read the given CSV file and return a list of integers from one column.

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
            # Skip header row if present
            next(reader, None)

            for row in reader:
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


def mean(values):
    """
    Return the arithmetic mean of a list of numbers.
    """
    if len(values) == 0:
        raise ValueError("mean() requires at least one value.")
    return sum(values) / len(values)


def median(values):
    """
    Return the median of a list of numbers.
    """
    if len(values) == 0:
        raise ValueError("median() requires at least one value.")

    sorted_vals = sorted(values)
    n_vals = len(sorted_vals)
    mid = n_vals // 2

    if n_vals % 2 == 1:
        return sorted_vals[mid]

    return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2


def std(values):
    """
    Return the population standard deviation of a list of numbers.
    """
    if len(values) == 0:
        raise ValueError("std() requires at least one value.")

    m_val = mean(values)
    squared_diffs = [(x - m_val) ** 2 for x in values]
    variance = sum(squared_diffs) / len(squared_diffs)
    return variance ** 0.5
