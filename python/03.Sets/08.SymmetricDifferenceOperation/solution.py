#!/usr/bin/env python3.7
"""Symmetric Difference Operation: Jerod Gawne, 2019.02.11 <https://github.com/jerodg>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    _, s = int(input()), set(input().split())
    _, s2 = int(input()), set(input().split())
    print(len(s.symmetric_difference(s2)))


if __name__ == '__main__':
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
