from typing import Any, Callable, TypeVar

T = TypeVar('T')


def should_swap(a: T, b: T,
                key: Callable[[T], Any] | None,
                cmp: Callable[[T, T], int] | None) -> bool:
    if cmp is not None:
        return cmp(a, b) > 0

    if key is not None:
        return key(a) > key(b)

    return a > b
