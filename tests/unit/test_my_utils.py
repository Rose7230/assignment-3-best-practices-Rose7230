"""
AI Usage Policy:
AI assistance was used to improve clarity and organization.
All test behaviors and verification were performed by the student.
"""

import math
from my_utils import mean, median, std


def test_mean_basic():
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_negative():
    assert mean([-2, -1, 0, 1, 2]) == 0.0


def test_mean_single():
    assert mean([10]) == 10


def test_mean_empty():
    try:
        mean([])
        assert False
    except ValueError:
        assert True


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_median_duplicates():
    assert median([5, 1, 5, 2, 5]) == 5


def test_median_empty():
    try:
        median([])
        assert False
    except ValueError:
        assert True


def test_std_same():
    assert std([2, 2, 2, 2]) == 0.0


def test_std_basic():
    vals = [10, 20, 30]
    expected = math.sqrt(
        ((10 - 20) ** 2 + (20 - 20) ** 2 + (30 - 20) ** 2) / 3
    )
    assert std(vals) == expected


def test_std_empty():
    try:
        std([])
        assert False
    except ValueError:
        assert True
