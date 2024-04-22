#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.10.10 <https://github.com/jerodg>
Doesn't use collections and technically doesn't meet the problem criteria."""

import sys
import traceback

if __name__ == '__main__':
    try:
        monies = 0
        num_shoes, avail_sizes, num_cust = input(), input().split(), input()
        for i in range(int(num_cust)):
            size, value = input().split()
            if size in avail_sizes:
                monies += int(value)
                del avail_sizes[avail_sizes.index(size)]

        print(monies)

    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
