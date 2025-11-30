# https://www.hackerrank.com/challenges/countingsort3/problem


import os


def countingSort(arr):
    freq = [0] * 100
    for item in arr:
        num = int(item.split()[0])
        freq[num] += 1

    cumulative = [0] * 100
    cumulative[0] = freq[0]
    for i in range(1, 100):
        cumulative[i] = cumulative[i-1] + freq[i]

    return cumulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input())

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
