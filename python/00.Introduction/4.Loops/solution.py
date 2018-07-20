#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.11

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == '__main__':
    try:
        print(*[num ** 2 for num in range(n)], sep='\n')
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
