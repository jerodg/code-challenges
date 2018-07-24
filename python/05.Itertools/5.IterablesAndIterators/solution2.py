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
        N = int(input())
        S = input().split()
        K = int(input())

        num = 0
        den = 0

        for c in itertools.combinations(S, K):
            den += 1
            num += 'a' in c

        print(float(num) / den)
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
