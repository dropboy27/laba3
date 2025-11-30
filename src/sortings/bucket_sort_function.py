from typing import Any, Callable, TypeVar
from src.sortings.quick_sort_function import quick_sort
T = TypeVar('T')


def bucket_sort(a: list[T], buckets: int | None = None, key: Callable[[T], Any] | None = None,
                cmp: Callable[[T, T], int] | None = None) -> list[T]:
    len_a = len(a)
    if len_a <= 1:
        return a.copy()

    if buckets == None:
        buckets = len_a

    if key is not None:
        values = [key(x) for x in a]
        min_a = min(values)
        max_a = max(values)
    else:
        min_a = min(a)
        max_a = max(a)
    range_a = max_a-min_a
    bucket_list = [[] for i in range(buckets)]
    for num in a:
        if key is not None:
            val = key(num)
        else:
            val = num
        if val == max_a:
            index = -1
        else:
            index = int((val - min_a) / range_a * buckets)
        bucket_list[index].append(num)

    soerted_list = []

    for bucket in bucket_list:
        sorted_bucket = quick_sort(bucket, key=key, cmp=cmp)
        soerted_list.extend(sorted_bucket)
    return soerted_list
