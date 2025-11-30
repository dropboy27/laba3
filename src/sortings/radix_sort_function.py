def radix_sort(a: list[int], base: int = 10) -> list[int]:
    if not a:
        return []
    max_len = max(len(str(x)) for x in a)
    a = [int(x) for x in a]
    based_mas = [[] for i in range(base)]
    for i in range(0, max_len):
        for j in a:
            digit = (j // base ** i) % 10
            based_mas[digit].append(j)
        a = [x for item in based_mas for x in item]
        based_mas = [[] for i in range(base)]
    return a
