#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.07

https://www.hackerrank.com/challenges/simple-array-sum/problem
"""
import sys
import traceback


def main():
    """
    Main/Tests
    """
    _ = input()  # required to pass tests
    print(sum(map(int, input().split())))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
