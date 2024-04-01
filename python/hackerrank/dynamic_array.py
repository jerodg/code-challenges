#!/bin/python3

import os


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    lastAnswer = 0
    seqList = [[] for _ in range(n)]
    result = []
    for query in queries:
        queryType = query[0]
        x = query[1]
        y = query[2]
        index = (x ^ lastAnswer) % n
        if queryType == 1:
            seqList[index].append(y)
        elif queryType == 2:
            size = len(seqList[index])
            lastAnswer = seqList[index][y % size]
            result.append(lastAnswer)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
