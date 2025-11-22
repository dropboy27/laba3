
def quick_sort(a: list[int]) -> list[int]:
    if not a:
        return []
    if len(a) == 1:
        return a
    pivot = a[0]

    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
