#!/usr/bin/env python3.7
"""Jerod Gawne, 2019.03.06 <https://github.com/jerodg>"""
import sys
import traceback

if __name__ == "__main__":
    try:
        s = list(input())
        s2 = set(s)
        d = {k: 0 for k in s2}
        for x in s2:
            d[x] = s.count(x)

        out = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
        print(*out[:3], sep="\n")
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
