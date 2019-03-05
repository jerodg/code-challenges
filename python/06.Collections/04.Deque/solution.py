#!/usr/bin/env python3.7
"""Jerod Gawne, 2019.03.05 <https://github.com/jerodg>"""
import sys
import traceback
from collections import deque

if __name__ == '__main__':
    try:
        d = deque()
        for _ in range(int(input())):
            cmd, *args = input().split()
            getattr(d, cmd)(*args)
        print(*d)

    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
