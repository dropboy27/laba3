import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    if distinct:
        if hi - lo + 1 < n:
            raise ValueError(
                "Невозможно сгенерировать n уникальных чисел в данном диапазоне")
        return random.sample(range(lo, hi + 1), k=n)
    else:
        return [random.randint(lo, hi) for i in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    arr = [int(x) for x in range(n)]

    for i in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    unique = [int(x) for x in range(k_unique)]

    return [random.choice(unique) for i in range(n)]


def reverse_sorted(n: int) -> list[int]:
    return [int(x) for x in range(n-1, -1, -1)]


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    if seed is not None:
        random.seed(seed)

    return [random.uniform(lo, hi) for i in range(n)]
