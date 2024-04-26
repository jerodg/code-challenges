#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.12

https://github.com/jerodg/hackerrank
"""

import sys
import traceback

if __name__ == '__main__':
    try:
        input()  # Only needed to pass tests
        print(sorted(set(map(int, input().split())))[-2])
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
