"""Dictionary practice with color. Test version."""
__author__ = "730477496"

"""you are to define at least 3x unit test functions.
1. One edge case
2. Two use cases
"""

def test_invert():
    """checks for inverted"""
    first_list_1: list[str] = ["x", "y", "z"]
    assert test_invert(first_list_1) == ["z", "y", "x"]
    first_list_2: list[str] = ["apple", "cat"]
    assert test_invert(first_list_2) == ["cat", "apple"]
    first_list_3: list[str] = []
    assert test_invert(first_list_3) == []
