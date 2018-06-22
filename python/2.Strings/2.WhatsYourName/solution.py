#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.22

https://github.com/jerodg/hackerrank
"""
import sys
import traceback


if __name__ == '__main__':
    try:
        print(f'Hello {input()} {input()}! You just delved into python.')
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
