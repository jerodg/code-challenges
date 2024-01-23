#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.21

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == "__main__":
    try:
        print("".join([i.lower() if i.isupper() else i.upper() for i in input()]))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
