#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.07.20

https://github.com/jerodg/hackerrank
"""
import itertools
import sys
import traceback

if __name__ == '__main__':
    try:
        s, plen = input().split()
        print(*[''.join(_) for _ in itertools.permutations(sorted(s), int(plen))], sep='\n')
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
