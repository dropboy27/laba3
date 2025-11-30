from copy import deepcopy
from src.additional_utils.should_swap_function import should_swap
from typing import Any, Callable, TypeVar

T = TypeVar('T')


def counting_sort(a: list[T], key: Callable[[T], Any] | None = None,
                  cmp: Callable[[T, T], int] | None = None) -> list[T]:
    if not a:
        return []

    if key is not None:
        keyed_items = [(key(x), x) for x in a]
        min_key = min(k for k, _ in keyed_items)
        max_key = max(k for k, _ in keyed_items)

        range_keys = max_key - min_key + 1
        buckets = [[] for _ in range(range_keys)]

        for k, item in keyed_items:
            buckets[k - min_key].append(item)

        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result
    else:
        min_a = min(a)
        max_a = max(a)
        count = [0] * (max_a - min_a + 1)

        for num in a:
            count[num - min_a] += 1

        result = []
        for i in range(len(count)):
            result.extend([i + min_a] * count[i])

        return result
