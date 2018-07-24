#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.07.24

https://github.com/jerodg/hackerrank
"""
import itertools
import sys
import traceback

if __name__ == '__main__':
    try:
        ls_len = int(input())
        ls = input().split()
        indices = int(input())

        combinations = list(itertools.combinations(ls, indices))
        fltr = filter(lambda c: 'a' in c, combinations)
        print("{0:.3}".format(len(list(fltr)) / len(combinations)))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
