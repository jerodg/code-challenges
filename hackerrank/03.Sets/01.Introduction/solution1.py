#!/usr/bin/env python3.7
"""Jerod Gawne, 2018.10.02 <https://github.com/jerodg>"""
import sys
import traceback

if __name__ == "__main__":
    try:
        input()  # capture unnecessary input
        s = set(map(int, input().split()))
        print(sum(s) / len(s))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
