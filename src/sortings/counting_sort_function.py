from copy import deepcopy
from additional_utils.should_swap_function import should_swap
from typing import Any, Callable, TypeVar

T = TypeVar('T')


def counting_sort(a: list[T], key: Callable[[T], Any] | None = None,
                  cmp: Callable[[T, T], int] | None = None) -> list[T]:
    result = a.copy()
    min_a = min(a)
    max_a = max(a)
    count = [0] * (max_a-min_a+1)

    for num in a:
        count[num-min_a] += 1

    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            result[index] = i + min_a
            index += 1
            count[i] -= 1

    return result
