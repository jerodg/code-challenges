#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.

"""
import sys
import traceback

import re
import itertools

def count(s):
    # subs = [''.join(g) for n, g in itertools.groupby(s)]
    # return subs
    longest = None
    prev = s[0]
    cnt = 0

    for c in range(len(s) + 1):
        if s[c]



if __name__ == '__main__':
    try:
        v = 'aabbbtcaa'
        print(count(v))

    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
