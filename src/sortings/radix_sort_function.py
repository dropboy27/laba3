from additional_utils.should_swap_function import should_swap
from typing import Any, Callable, TypeVar

T = TypeVar('T')


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    max_len = max(len(str(x)) for x in a)
    len_a = len(a)
    a = [int(x) for x in a]
    print(a)
    based_mas = [[] for i in range(base)]
    for i in range(0, max_len):
        for j in a:
            digit = (j // base ** i) % 10
            based_mas[digit].append(j)
        a = [x for item in based_mas for x in item]
        based_mas = [[] for i in range(base)]
    return a
