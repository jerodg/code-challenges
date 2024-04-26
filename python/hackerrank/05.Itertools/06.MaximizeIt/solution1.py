#!/usr/bin/env python3.7
"""Maximize It: Jerod Gawne, 2019.02.22 <https://github.com/jerodg>"""

from itertools import product
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    k, m = map(int, input().split())
    n = (list(map(int, input().split()))[1:] for _ in range(k))
    results = map(lambda x: sum(i**2 for i in x) % m, product(*n))
    print(max(results))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(print_exception(*exc_info()))
