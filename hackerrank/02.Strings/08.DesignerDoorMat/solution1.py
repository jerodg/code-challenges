#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.28

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == "__main__":
    try:
        n, m = map(int, input().split())
        for i in range(1, n, 2):
            print(str(".|.") * i).center(m, "-")
        print(str("WELCOME").center(m, "-"))
        for i in range(n - 2, -1, -2):
            print(str(".|.") * i).center(m, "-")
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
