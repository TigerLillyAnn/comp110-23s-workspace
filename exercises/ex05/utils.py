__author__ = "730477496"

def only_evens(i: list[int]):
    #returns only even numbers
    even = []
    for num in i:
        if num % 2 == 0:
            even.append(num)
    return even

def concat(first: list[int], second: list[int]):
    #combines first and second list together
    return first + second 

def sub(first: list[int], start_index: list[int], end_index: list[int]):
    return first[start_index: end_index]
