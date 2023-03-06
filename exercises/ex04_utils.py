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

def max(numbers):
    if len(numbers) == 0:
        raise ValueError("List is empty.")
    return max(numbers)

def is_equal(ints, insert:int) -> bool:
    count: int = 0
    count2: int = 0
    output: bool = False
    if len(ints) != len(insert):
        return False
    while count2 < len(insert):
        if ints[count] == insert[count2]:
            output = True
        else:
            return False 
        count += 1
        count2 += 1
    return output