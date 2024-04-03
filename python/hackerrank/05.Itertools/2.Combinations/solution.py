#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.07.24

https://github.com/jerodg/hackerrank
"""
import itertools
import sys
import traceback

if __name__ == "__main__":
    try:
        s, plen = input().split()
        s = sorted(s)  # Sort before so the string is not sorted with each iteration of geneartor below
        print(*("".join(j) for i in range(1, int(plen) + 1) for j in itertools.combinations(s, i)), sep="\n", )
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
