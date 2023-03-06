"""Example function for unit tests"""

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    if len(xs) == 1:
        return xs[0]
    
    sum_total: float = 0.0
    for num in range(0,len(xs)):
        sum_total += xs[num]

    return sum_total