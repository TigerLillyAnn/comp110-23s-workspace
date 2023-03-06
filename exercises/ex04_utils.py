"""Lists exercise!"""
___author___ = "730477496"


def all(numbers, target):
    i: int = 0
    numbers: list[int] = [1, 2, 3]
    if not numbers:
        return False
    else:
        return True

def max(numbers):
    if len(numbers) == 0:
        raise ValueError("List is empty.")
    return max(numbers)

def is_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        return True