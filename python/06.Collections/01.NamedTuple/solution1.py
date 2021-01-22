#!/usr/bin/env python3.7
"""Jerod Gawne, 2019.02.26 <https://github.com/jerodg>"""
import collections
import statistics
import sys
import traceback

if __name__ == '__main__':
    try:
        print('%.2f' % statistics.mean(next(
                (int(student(*row).MARKS) for row in (input().split() for i in range(size))) for size, student in
                [[int(input()), collections.namedtuple('Student', input())]])))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
