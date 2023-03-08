"""Exercise 5: Utility functions list"""
__author__ = "730477496"

"""Checks list for even numbers, output is only even numbers"""
def only_evens(i: list[int]):
    even = []
    for num in i:
        if num % 2 == 0:
            even.append(num)
    return even

"""prints a combination of first list + second list"""
def concat(first: list[int], second: list[int]):
    return first + second 

"""takes the start, end index of the list"""
def sub(first: list[int], start_index: list[int], end_index: list[int]):
    return first[start_index: end_index]
