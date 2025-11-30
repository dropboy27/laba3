# https://www.hackerrank.com/challenges/countingsort1/problem

#!/bin/python3

import os


def countingSort(arr):
    freq = [0] * 100
    for num in arr:
        freq[num] += 1
    return freq


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
