import pytest
from src.sortings.bubble_sort_function import bubble_sort
from src.sortings.quick_sort_function import quick_sort
from src.sortings.bucket_sort_function import bucket_sort
from src.sortings.counting_sort_function import counting_sort
from src.sortings.radix_sort_function import radix_sort
from src.sortings.heap_sort_function import heap_sort

RETURNING_SORTS = [
    bubble_sort,
    quick_sort,
    bucket_sort,
    counting_sort,
    radix_sort
]


@pytest.mark.parametrize("sort_func", RETURNING_SORTS)
def test_standard_sort(sort_func):
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    assert sort_func(arr) == sorted(arr)


@pytest.mark.parametrize("sort_func", RETURNING_SORTS)
def test_empty_or_single_element(sort_func):
    assert sort_func([]) == []
    assert sort_func([10]) == [10]


@pytest.mark.parametrize("sort_func", RETURNING_SORTS)
def test_already_sorted_or_reverse(sort_func):
    assert sort_func([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert sort_func([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_heap_sort():
    arr = [3, 1, 4, 1, 5]
    heap_sort(arr)
    assert arr == [1, 1, 3, 4, 5]

    arr_empty = []
    heap_sort(arr_empty)
    assert arr_empty == []


def test_sort_with_key():
    arr = ["dota", "cat", "a"]
    assert quick_sort(arr, key=len) == ["a", "cat", "dota"]
    assert bubble_sort(arr, key=len) == ["a", "cat", "dota"]


def test_sort_with_cmp():
    def reverse_cmp(a, b):
        return -1 if a > b else (1 if a < b else 0)

    arr = [3, 1, 4, 1, 5]
    assert quick_sort(arr, cmp=reverse_cmp) == [5, 4, 3, 1, 1]


def test_bucket_sort_edge_cases():
    assert bucket_sort([0.5, 0.2, 0.8]) == [0.2, 0.5, 0.8]
    data = [("a", 3), ("b", 1), ("c", 2)]
    result = bucket_sort(data, key=lambda x: x[1])
    assert result == [("b", 1), ("c", 2), ("a", 3)]


def test_counting_sort_with_key():
    words = ["cat", "a", "dog", "hi"]
    result = counting_sort(words, key=len)
    assert result == ["a", "hi", "cat", "dog"]


def test_heap_sort_edge():
    arr = [1, 3, 2]
    heap_sort(arr)
    assert arr == [1, 2, 3]
