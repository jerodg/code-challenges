#!/usr/bin/env python3.7
"""Symmetric Difference: Jerod Gawne, 2019.01.17 <https://github.com/jerodg/hackerrank>"""

from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    """Main"""
    _, a, _, b = (
        input(),
        set(map(int, input().split())),
        input(),
        set(map(int, input().split())),
    )
    print(*sorted(a.symmetric_difference(b)), sep='\n')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(print_exception(*exc_info()))
