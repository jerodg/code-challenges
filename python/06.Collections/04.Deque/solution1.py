#!/usr/bin/env python3.7
"""Jerod Gawne, 2019.03.05 <https://github.com/jerodg>"""
import sys
import traceback
from collections import deque

if __name__ == '__main__':
    try:
        d = deque()
        for _ in range(int(input())):
            inp = input().split()
            getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
        print(*d)

    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
