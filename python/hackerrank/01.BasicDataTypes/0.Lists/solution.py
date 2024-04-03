#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.18

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == "__main__":
    try:
        ls = []
        [getattr(ls, s[0])(*map(int, s[1:])) if hasattr(ls, s[0]) else print(ls) for s in
                [input().split() for _ in range(int(input()))]]
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
