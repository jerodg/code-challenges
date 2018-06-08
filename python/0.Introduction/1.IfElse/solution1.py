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
        check = {True: "Not Weird", False: "Weird"}

        print(check[n % 2 == 0 and (n in range(2, 6) or n > 20)])
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
