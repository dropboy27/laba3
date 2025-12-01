# https://www.hackerrank.com/challenges/countingsort2/problem

#!/bin/python3

import os


def countingSort(arr):
    freq = [0] * 100
    for num in arr:
        freq[num] += 1

    result = []
    for i in range(100):
        result.extend([i] * freq[i])

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
