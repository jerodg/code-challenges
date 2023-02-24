#!/bin/python3

def min_max_sum(arr):
    arr.sort()
    print(sum(arr[0:-1]), sum(arr[1:]))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    min_max_sum(arr)
