def counting_sort(a: list[int]) -> list[int]:
    min_a = min(a)
    max_a = max(a)
    count = [0] * (max_a-min_a+1)

    for num in a:
        count[num-min_a] += 1

    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            a[index] = i + min_a
            index += 1
            count[i] -= 1

    return a
