def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    len_a = len(a)
    if len_a <= 1:
        return a
    min_a = min(a)
    max_a = max(a)
    range_a = max_a-min_a
    if buckets == None:
        buckets = len_a

    bucket_list = [[] for i in range(buckets)]
    for num in a:
        if num == max_a:
            index = -1
        else:
            index = int((num - min_a) / (range_a) * buckets)
        bucket_list[index].append(num)
    soerted_list = []
    for bucket in bucket_list:
        sorted_bucket = bucket_sort(bucket)
        soerted_list.extend(sorted_bucket)
    return soerted_list


print(bucket_sort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]))
