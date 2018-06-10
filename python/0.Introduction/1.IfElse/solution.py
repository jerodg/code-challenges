#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.08

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == '__main__':
    try:
        n = int(input())
        print('Weird' if n % 2 == 1 or 6 <= n <= 20 else 'Not Weird')
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
