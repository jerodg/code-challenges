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
        _, s, n = input(), input().split(), int(input())
        t = list(itertools.combinations(s, n))
        f = [i for i in t if "a" in i]
        print("{:.3}".format(len(f) / len(t)))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
