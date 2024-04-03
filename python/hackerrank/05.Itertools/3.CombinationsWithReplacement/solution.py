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
        print(*("".join(_) for _ in itertools.combinations_with_replacement(s, int(plen))), sep="\n", )
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
