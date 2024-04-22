#!/usr/bin/env python3.7
"""Jerod Gawne, 2019.03.04 <https://github.com/jerodg>"""

import sys
import traceback
from collections import OrderedDict

if __name__ == '__main__':
    try:
        n = int(input())
        d = OrderedDict()
        for i in range(n):
            k, v = input().rsplit(None, 1)
            v = int(v)
            try:
                d[k] += v
            except KeyError:
                d[k] = v
        [print(k, v) for k, v in d.items()]
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
