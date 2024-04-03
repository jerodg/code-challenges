#!/usr/bin/env python3.7
"""Jerod Gawne, 2019.03.06 <https://github.com/jerodg>"""
import sys
import traceback
from collections import Counter, OrderedDict

if __name__ == "__main__":
    try:

        class OrderedCounter(Counter, OrderedDict):
            @classmethod
            def fromkeys(cls, iterable, v=None):
                pass


        [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
