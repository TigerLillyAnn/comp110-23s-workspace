"""Quiz 2 Practice: Code writing exercises."""

def odd_and_even(lst: list[int]) -> list[list[int]]:
    odds = []
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return[odds, evens]    

