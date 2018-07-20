#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.14

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == '__main__':
    try:
        marks = [[input(), float(input())] for _ in range(int(input()))]
        second_lowest = sorted(list(set([score for name, score in marks])))[1]
        print(*[a for a, b in sorted(marks) if b == second_lowest], sep='\n')
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
