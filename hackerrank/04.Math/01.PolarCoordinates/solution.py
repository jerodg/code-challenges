#!/usr/bin/env python3.7
"""Polar Coordinates: Jerod Gawne, 2019.02.19 <https://github.com/jerodg>"""
from cmath import polar
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    print(*polar(complex(input())), sep="\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
