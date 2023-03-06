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

def max(numbers):
    if len(numbers) == 0:
        raise ValueError("List is empty.")
    return max(numbers)

def is_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True