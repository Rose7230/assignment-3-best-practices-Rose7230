"""
AI Usage Policy:
AI assistance was used to help structure these tests and improve clarity.
All test ideas, expected behaviors, and final verification were performed
by the student.
"""

import math

from my_utils import mean, median, std


def test_mean_basic():
    values = [1, 2, 3, 4]
    assert mean(values) == 2.5


def test_mean_with_negative_numbers():
    values = [-2, -1, 0, 1, 2]
    assert mean(values) == 0.0


def test_mean_single_value():
    values = [10]
    assert mean(values) == 10


def test_mean_empty_raises():
    try:
        mean([])
        assert False, "Expected ValueError for empty list"
    except ValueError:
        assert True


def test_median_odd_length():
    values = [3, 1, 2]
    # Sorted: [1, 2, 3], median is 2
    assert median(values) == 2


def test_median_even_length():
    values = [1, 2, 3, 4]
    # Median is (2 + 3) / 2 = 2.5
    assert median(values) == 2.5


def test_median_with_duplicates():
    values = [5, 1, 5, 2, 5]
    # Sorted: [1, 2, 5, 5, 5], median is 5
    assert median(values) == 5


def test_median_empty_raises():
    try:
        median([])
        assert False, "Expected ValueError for empty list"
    except ValueError:
        assert True


def test_std_all_same_values():
    values = [2, 2, 2, 2]
    # All the same => std = 0
    assert std(values) == 0.0


def test_std_basic():
    values = [10, 20, 30]
    # Population std: sqrt(((10-20)^2 + (20-20)^2 + (30-20)^2) / 3)
    expected = math.sqrt(((10 - 20) ** 2 + (20 - 20) ** 2 + (30 - 20) ** 2) / 3)
    assert std(values) == expected


def test_std_empty_raises():
    try:
        std([])
        assert False, "Expected ValueError for empty list"
    except ValueError:
        assert True

