#!/usr/bin/env python3.7
"""Jerod Gawne, 2019.02.26 <https://github.com/jerodg>"""

import sys
import traceback

if __name__ == '__main__':
    try:
        student, marks = int(input()), input().split().index('MARKS')
        print(sum([int(input().split()[marks]) for _ in range(student)]) / student)
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
