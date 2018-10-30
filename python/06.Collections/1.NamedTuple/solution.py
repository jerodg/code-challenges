#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.10.12 <https://github.com/jerodg>"""
import collections
import sys
import traceback

if __name__ == '__main__':
    try:
        students = input()
        columns = input().split()
        # marks = columns.index('MARKS')
        marks = collections.namedtuple('record', columns)
        score = 0
        for _ in range(students):


    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
