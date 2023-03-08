___author___ = "730477496"

from exercises.ex05.utils import only_evens, concat, sub

def test_only_evens(i: list[int]):
    test_list: list[int] = [2, 3, 4, 5]
    assert only_evens(test_list) == [2, 4]

def test_only_evens(i: list[int]):
    test_list: list[int] = [50, 60, 70, 80, 90, 100]
    assert only_evens(test_list) == [60, 80, 100]

def test_only_evens(i: list[int]):
    test_list: list[int] = [5, 7, 9]
    assert only_evens(test_list) == []

def test_concat(first: list[int], second: list[int]):
    test_first_list: list[int] = [1, 2, 3]
    test_second_list: list[int] = [1, 2, 3]
    assert concat(test_first_list + test_second_list) == [1, 2, 3, 1, 2, 3]

def test_concat(first: list[int], second: list[int]):
    test_first_list: list[int] = [100, 100, 100]
    test_second_list: list[int] = [200, 200, 200]
    assert concat(test_first_list + test_second_list) == [100, 100, 100, 200, 200, 200]

def test_concat(first: list[int], second: list[int]):
    test_first_list: list[int] = [0, 0, -1]
    test_second_list: list[int] = [-1, 0, 0]
    assert concat(test_first_list + test_second_list) == [0, 0, -1, -1, 0, 0]

def test_sub(first: list[int], start_index: list[int], end_index: list[int]):
    test_first: list[int] = [10, 20, 30, 40]
    assert sub(first[start_index: end_index]) == [20, 30]

def test_sub(first: list[int], start_index: list[int], end_index: list[int]):
    test_first: list[int] = [1, 2, 3, 4]
    assert sub(first[start_index: end_index]) == [3, 4]

def test_sub(first: list[int], start_index: list[int], end_index: list[int]):
    test_first: list[int] = [0, -1, 2, 3]
    assert sub(first[start_index: end_index]) == [-1, 2]
