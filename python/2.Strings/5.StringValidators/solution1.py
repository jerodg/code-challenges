#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.23

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == '__main__':
    try:
        s = input()
        for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
            print(any(eval("c." + test + "()") for _ in s))
        print('\n')
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
