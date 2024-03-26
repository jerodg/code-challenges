#!/usr/bin/env python3.7
"""Check Subsets: Jerod Gawne, 2019.02.15 <https://github.com/jerodg>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    for _ in range(int(input())):
        _, a = input(), set(input().split())
        _, b = input(), set(input().split())
        print(a <= b)


if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
