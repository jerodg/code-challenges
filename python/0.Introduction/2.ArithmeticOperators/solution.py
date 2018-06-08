#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.08

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == '__main__':
    try:
        a, b = int(input()), int(input())
        print((a + b), (a - b), (a * b), sep='\n')
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
