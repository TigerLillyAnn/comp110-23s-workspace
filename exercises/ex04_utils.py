"""Lists exercise!"""
___author___ = "730477496"

def all(ints, insert: int) -> bool:
    n: int = len(ints)
    j: int = 0
    while j < n:
        if ints[j] == insert:
            return True
        j = j + 1
    return False

def find_max(number: list[int]) -> int:
    if len(number) == 0:
        raise ValueError("List is empty.")
    return max(number)

def is_equal(ints: list[int], insert: list[int]) -> bool:
    i = 0
    assert is_equal([1, 2, 2], [1, 2, 2]) == True
    assert is_equal([2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2]) == True
    if len(ints) != len(insert):
        return False
    while i < len(ints):
        if ints[i] != insert[i]:
            return False
        i += 1
    return True