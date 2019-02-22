#!/usr/bin/env python3.7
"""Maximize It: Jerod Gawne, 2019.02.22 <https://github.com/jerodg>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn
from itertools import product


def main() -> NoReturn:
    k, m = map(int, input().split())
    n = (list(map(int, input().split()))[1:] for _ in range(k))
    results = (sum(num**2 for num in numbers) % m for numbers in product(*n))
    print(max(results))


if __name__ == '__main__':
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
