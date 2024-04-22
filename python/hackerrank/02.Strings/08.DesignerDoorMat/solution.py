#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.28

https://github.com/jerodg/hackerrank
"""

import sys
import traceback

if __name__ == '__main__':
    try:
        n, m = map(int, input().split())
        pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
        print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
