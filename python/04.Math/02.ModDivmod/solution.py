#!/usr/bin/env python3.7
"""Mod Divmod: Jerod Gawne, 2019.02.19 <https://github.com/jerodg>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    a, b = int(input()), int(input())
    print(a // b)
    print(a % b)
    print(divmod(a, b))


if __name__ == '__main__':
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
