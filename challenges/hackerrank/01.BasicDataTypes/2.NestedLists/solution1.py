#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.14

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == "__main__":
    try:
        marks = []
        for _ in range(0, int(input())):
            marks.append([input(), float(input())])

        second_lowest = sorted(list(set([score for name, score in marks])))[1]
        print("\n".join([a for a, b in sorted(marks) if b == second_lowest]))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
