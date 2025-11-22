from src.exceptions import EmptyListError


def bubble_sort(a: list[int]) -> list[int]:
    if not a:
        raise EmptyListError
    else:
        len_arr = len(a)
        for i in range(len_arr):
            for j in range(len_arr-i-1):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
        return a
