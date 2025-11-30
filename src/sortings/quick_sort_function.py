from src.additional_utils.should_swap_function import should_swap
from typing import Any, Callable, TypeVar

T = TypeVar('T')


def quick_sort(a: list[T], key: Callable[[T], Any] | None = None,
               cmp: Callable[[T, T], int] | None = None) -> list[T]:

    if not a:
        return []
    if len(a) == 1:
        return a
    pivot = a[0]

    left = []
    middle = []
    right = []

    for x in a:
        if should_swap(pivot, x, key, cmp):
            left.append(x)
        elif should_swap(x, pivot, key, cmp):
            right.append(x)
        else:
            middle.append(x)

    return quick_sort(left, key=key, cmp=cmp) + middle + quick_sort(right, key=key, cmp=cmp)
