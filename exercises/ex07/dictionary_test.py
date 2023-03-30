"""Dictionary practice with color. Test version."""
__author__ = "730477496"
from dictionary import invert
from dictionary import favorite_color
from dictionary import count
"""you are to define at least 3x unit test functions.
1. One edge case
2. Two use cases
"""


def test_invert():
    """Checks for inverted."""
    first_list_1: list[str] = ["x", "y", "z"]
    assert invert(first_list_1) == ["z", "y", "x"]
    first_list_2: list[str] = ["apple", "cat"]
    assert invert(first_list_2) == ["cat", "apple"]
    first_list_3: list[str] = []
    assert invert(first_list_3) == []


def test_favorite_color():
    """Checks for empty."""
    assert favorite_color([]) == ""
    """Tests for only one entry"""
    assert favorite_color({"Alice": "red"}) == "red"
    """Test a dictionary with multiple answers"""
    assert favorite_color({"Emma": "red", "Shane": "green", "Thomas": "blue", "Eve": "green", "Davis": "blue", "Jacob": "red"}) == "green"


def test_count():
    """Checks for empty list."""
    assert count([]) == ""
    """Checks for 1:1."""
    value_list1 = ["red", "green", "blue"]
    return_list1 = {"red": 1, "green": 1, "blue": 1}
    assert count(value_list1) == return_list1
    """Checks for many different inputs of the color."""
    value_list2 = ["red", "green", "blue"]
    return_list2 = {"red": 3, "green": 6, "blue": 2}
    assert count(value_list2) == return_list2
