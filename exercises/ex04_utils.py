"""Lists exercise!"""
___author___ = "730477496"


def all(ints, insert: int) -> bool:
    n: int = len(ints)
    j: int = 0
    while j < n:
        if ints[j] == insert:
            j = j + 1
        else:
            j = j + 1
            return False
    return True

print(all([1, 2, 3], 2)) #prints False
print(all([2, 2, 2], 2)) #prints True

def max(ints, insert: int) -> bool:
    n: int = len(ints)
    j: int = 0
    while j < n:
        if ints[j] == insert:
            j = j + 1
        else:
            j = j + 1
            return False
    return True

def is_equal(ints, insert:int) -> bool:
    count: int = len(ints)
    count2 = 0
    output: bool = False
    if len(input) == 0:
        return False
    while count < len(input):
        if input(count) == insert(count2):
            output = True
        else: return False 
        count += 1
        count2 += 1
    return(output)
