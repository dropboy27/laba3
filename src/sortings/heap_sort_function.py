def heapify(arr, n, i, key=None, cmp=None):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    def compare(a, b):
        if cmp:
            return cmp(a, b) > 0
        val_a = key(a) if key else a
        val_b = key(b) if key else b
        return val_a > val_b

    if left < n and compare(arr[left], arr[largest]):
        largest = left
    if right < n and compare(arr[right], arr[largest]):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key, cmp)


def heap_sort(arr, key=None, cmp=None):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key, cmp)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key, cmp)
