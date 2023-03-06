"""Lists exercise!"""
___author___ = "730477496"


def all(numbers, target):
    if not numbers:
        return False
    return numbers.count(target) == len(numbers)
#using count for smaller list recommended since it goes through the sequence twice.

def max(numbers):
    if len(numbers) == 0:
        raise ValueError("List is empty.")
    return max(numbers)

def is_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        return True