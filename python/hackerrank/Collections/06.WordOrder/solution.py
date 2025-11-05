#!/usr/bin/env python3.7
"""Word Order: Jerod Gawne, 2019.03.07 <https://github.com/jerodg/hackerrank>"""

import sys
import traceback
from collections import Counter

if __name__ == '__main__':
    try:
        d = Counter(input() for _ in range(int(input())))
        print(len(d))
        print(*d.values())
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
