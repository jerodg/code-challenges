#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.07

https://www.hackerrank.com/challenges/simple-array-sum/problem
"""
import os
import sys
import traceback


def simple_array_sum(ar):
    pass


def main():
    """
    Main/Tests
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simple_array_sum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
