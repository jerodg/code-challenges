#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.18

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == '__main__':
    try:
        n = int(input())  # only required for automated tests (online interpreter)
        print(hash(tuple(map(int, input().split()))))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
