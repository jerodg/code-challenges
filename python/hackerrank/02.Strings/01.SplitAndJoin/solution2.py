#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.21

https://github.com/jerodg/hackerrank

Doesn't really flow well with the online interpreter
as the main code is locked and is expecting the function to return.
"""
import sys
import traceback

if __name__ == "__main__":
    try:
        print("-".join(input().split(" ")))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
