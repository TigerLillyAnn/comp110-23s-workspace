"""Dictionary exercise with color."""
__author__ = "730477496"

import pytest

def invert(d: dict[str, str]) -> dict[str, str]:
    """ Invert the keys and values of a dictionary."""
    inverted_d = {}
    for key in d:
        value = d[key]
        inverted_d[value] = key
    return inverted_d

def favorite_color(names_colors: dict[str, str]) -> str:
    """Returns the most frequent color from a dictionary of names and favorite colors."""
    color_counts = {}
    for color in names_colors.values():
        color_counts[color] = color_counts.get(color, 0) + 1
    most_frequent_color = None
    most_frequent_count = 0
    first_color = None
    for key in names_colors:
        if first_color is None:
            first_color = names_colors[key]
        count = color_counts[names_colors[key]]
        if count > most_frequent_count or (count == most_frequent_count and names_colors[key] == first_color):
            most_frequent_color = names_colors[key]
            most_frequent_count = count
    return most_frequent_color

def count(values: list[str]) -> dict[str, int]:
    "counts the frequences of each item in a list and returns a dictionary of said counts"
    counts = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts