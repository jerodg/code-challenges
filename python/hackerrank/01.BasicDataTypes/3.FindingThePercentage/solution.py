#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.18

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == "__main__":
    try:
        marks = {}
        for _ in range(int(input())):
            line = input().split()
            marks[line[0]] = list(map(float, line[1:]))
        print(
            f"{sum(marks[input()]) / 3:.2f}"
        )  # Doesn't work with the online interperter but is a valid answer
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
