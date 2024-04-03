#!/bin/python3

import os


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max_sum = float('-inf')
    for i in range(1, 5):
        for j in range(1, 5):
            top = sum(arr[i - 1][j - 1:j + 2])
            mid = arr[i][j]
            bottom = sum(arr[i + 1][j - 1:j + 2])
            hourglass_sum = top + mid + bottom
            max_sum = max(max_sum, hourglass_sum)
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
