#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.11

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == "__main__":
    try:
        x, y, z, n = (int(input()) for _ in range(4))
        print([
            [a, b, c]
            for a in range(0, x + 1)
            for b in range(0, y + 1)
            for c in range(0, z + 1)
            if a + b + c != n
        ])
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
