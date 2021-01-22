#!/usr/bin/env python3.7
"""Symmetric Difference: Jerod Gawne, 2019.01.17 <https://github.com/jerodg/hackerrank>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    """Main"""
    input()
    l1 = set(map(int, input().split()))
    input()
    l2 = set(map(int, input().split()))

    out = []
    out.extend(l1.difference(l2))
    out.extend(l2.difference(l1))
    out = sorted(out)
    print(*out, sep='\n')


if __name__ == '__main__':
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
