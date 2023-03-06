"""Lists exercise!"""
___author___ = "730477496"

def all(ints, insert: int) -> bool:
    j: int = 0
    while j < len(ints):
        if ints[j] == insert:
            return True
        j = j + 1
    return False

def max(input_list: list[int]) -> int:
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")
    return max(input_list)

def is_equal(ints: list[int], insert: list[int]) -> bool:
    if len(ints) != len(insert):
        return False
    i = 0
    while i < len(ints):
        if ints[i] != insert[i]:
            return False
        i += 1
    return True