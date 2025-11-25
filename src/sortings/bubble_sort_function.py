from copy import deepcopy
from typing import Any, Callable, TypeVar
from src.exceptions import EmptyListError
from additional_utils.should_swap_function import should_swap

T = TypeVar('T')


def bubble_sort(a: list[int], key: Callable[[T], Any] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
    result = a.copy()
    if not a:
        raise EmptyListError
    else:
        len_arr = len(result)
        for i in range(len_arr):
            for j in range(len_arr-i-1):
                if should_swap(result[j], result[j+1], key, cmp):
                    result[j], result[j+1] = result[j+1], result[j]
        return result
