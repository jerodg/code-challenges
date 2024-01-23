#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.07.20

https://github.com/jerodg/hackerrank
"""
import itertools
import sys
import traceback

if __name__ == "__main__":
    try:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(*itertools.product(a, b))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
