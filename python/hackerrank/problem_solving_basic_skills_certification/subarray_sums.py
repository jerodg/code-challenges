#!/bin/python3

import os


#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries) -> list[int]:
    n = len(numbers)
    arr = [0] * (n + 1)
    zero_count = [0] * (n + 1)
    for i in range(n):
        arr[i + 1] = arr[i] + numbers[i]
        zero_count[i + 1] = zero_count[i] + (1 if numbers[i] == 0 else 0)

    result = []
    for l, r, x in queries:
        s = arr[r] - arr[l - 1]
        count = zero_count[r] - zero_count[l - 1]
        result.append(s + count * x)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = findSum(numbers, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
