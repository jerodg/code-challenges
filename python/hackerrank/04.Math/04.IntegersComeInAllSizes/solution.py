#!/usr/bin/env python3.7
"""Integers Come In All Sizes: Jerod Gawne, 2019.02.19 <https://github.com/jerodg>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    a, b, c, d = (int(input()) for _ in range(4))
    print(a ** b + c ** d)


if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
