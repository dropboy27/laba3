from copy import deepcopy


def counting_sort(a: list[int], k) -> list[int]:
    min_a = min(a)
    max_a = max(a)
    count = [0] * (max_a-min_a+1)

    for num in a:
        count[num-min_a] += 1

    index = 0
    countn = deepcopy(count)
    for i in range(len(count)):
        while count[i] > 0:
            a[index] = i + min_a
            index += 1
            count[i] -= 1
    index = 0
    sy = []
    for i in range(k):
        sy.append(a[index])
        index += countn[i]
    return sy


nums = [1, 1, 2, 2, 1, 3]
print(counting_sort(nums, 2))
