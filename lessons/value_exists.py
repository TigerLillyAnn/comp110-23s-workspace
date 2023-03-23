"""Practice for Quiz 2"""

def value_exists(dct: dict[str,int]) -> bool:
    for value in dct.values():
        if type(value) != int:
            return True
    return False