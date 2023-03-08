"""Asserting list and utility functions"""
___author___ = "730477496"

from exercises.ex05.utils import only_evens, concat, sub

def test_only_evens():
    test_list_1: list[int] = [2, 3, 4, 5]
    assert only_evens(test_list_1) == [2, 4]
    test_list_2: list[int] = [50, 60, 70, 80, 90, 100]
    assert only_evens(test_list_2) == [60, 80, 100]
    test_list_3: list[int] = [5, 7, 9]
    assert only_evens(test_list_3) == []


def test_concat():
    test_first_list_1: list[int] = [1, 2, 3]
    test_second_list_1: list[int] = [1, 2, 3]
    assert concat(test_first_list_1 + test_second_list_1) == [1, 2, 3, 1, 2, 3]
    test_first_list_2: list[int] = [100, 100, 100]
    test_second_list_2: list[int] = [200, 200, 200]
    assert concat(test_first_list_2 + test_second_list_2) == [100, 100, 100, 200, 200, 200]
    test_first_list_3: list[int] = [0, 0, -1]
    test_second_list_3: list[int] = [-1, 0, 0]
    assert concat(test_first_list_3 + test_second_list_3) == [0, 0, -1, -1, 0, 0]


def test_sub():
    test_first_1: list[int] = [10, 20, 30, 40]
    start_index_1: list[int] = [20]
    end_index_1: list[int] = [30]
    assert sub(test_first_1[start_index_1: end_index_1]) == [20, 30]
    test_first_2: list[int] = [1, 2, 3, 4]
    start_index_2: list[int] = [3]
    end_index_2: list[int] = [4]
    assert sub(test_first_2[start_index_2: end_index_2]) == [3, 4]
    test_first_3: list[int] = [0, -1, 2, 3]
    start_index_3: list[int] = [-1]
    end_index_3: list[int] = [2]
    assert sub(test_first_3[start_index_3: end_index_3]) == [-1, 2]
