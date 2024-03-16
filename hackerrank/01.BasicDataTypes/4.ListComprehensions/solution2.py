#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.11

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == "__main__":
    try:
        x, y, z, n = (int(input()), int(input()), int(input()), int(input()))

        # Not a list comprehension but rather a basic breakdown of the one used in solution.sql
        for a in range(x + 1):
            for b in range(y + 1):
                for c in range(z + 1):
                    if a + b + c != n:
                        print(a, b, c)
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
