#!/usr/bin/env python3.7
"""Word Order: Jerod Gawne, 2019.03.07 <https://github.com/jerodg/hackerrank>"""

import sys
import traceback

if __name__ == '__main__':
    try:
        d = {}
        for i in range(int(input())):
            # If input not in the dictionary, then add it; else increment the counter
            key = input()
            if key not in d.keys():
                d.update({key: 1})
                continue
            d[key] += 1

        print(len(d.keys()))
        print(*d.values())
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
