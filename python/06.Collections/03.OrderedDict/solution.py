#!/usr/bin/env python3.7
"""Jerod Gawne, 2019.03.04 <https://github.com/jerodg>"""
import sys
import traceback
from collections import OrderedDict

if __name__ == '__main__':
    try:
        d = OrderedDict()
        for _ in range(int(input())):
            item, space, quantity = input().rpartition(' ')
            d[item] = d.get(item, 0) + int(quantity)

        [print(item, quantity) for item, quantity in d.items()]
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
