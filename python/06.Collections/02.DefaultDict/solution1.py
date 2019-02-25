#!/usr/bin/env python3.7
"""Default Dict: Jerod Gawne, 2019.02.25 <https://github.com/jerodg>"""
from collections import defaultdict
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    n, m = map(int, input().split())
    d = defaultdict(list)
    [d[input()].append(i + 1) for i in range(n)]
    for j in [' '.join(map(str, d[input()])) or -1 for i in range(m)]:
        print(j)


if __name__ == '__main__':
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
