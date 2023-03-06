"""Lists exercise!"""
___author___ = "730477496"

def all(ints, insert: int) -> bool:
    j: int = 0
    while j < len(int):
        if ints[j] == insert:
            return True
        j = j + 1
    return False

def max_number(number: list[int]) -> int:
    if len(number) == 0:
        raise ValueError("max() arg is an empty List")
    return max(number)

def is_equal(ints: list[int], insert: list[int]) -> bool:
    if len(ints) != len(insert):
        return False
    i = 0
    while i < len(ints):
        if ints[i] != insert[i]:
            return False
        i += 1
    return True