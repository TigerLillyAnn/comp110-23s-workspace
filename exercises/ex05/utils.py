"""Exercise 5: Utility functions list!"""
__author__ = "730477496"


def only_evens(i: list[int]):
    """Checks list for even numbers, output is only even numbers."""
    even = []
    for num in i:
        if num % 2 == 0:
            even.append(num)
    return even


def concat(first: list[int], second: list[int]):
    """Prints a combination of first list + second list."""
    return first + second 


def sub(first: list[int], start_index: list[int], end_index: list[int]):
    """Takes the start, end index of the list."""
    return first[start_index: end_index]
