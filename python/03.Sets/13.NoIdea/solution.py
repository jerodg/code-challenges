#!/usr/bin/env python3.7
"""No Idea: Jerod Gawne, 2019.02.18 <https://github.com/jerodg>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    _ = input()
    n = input().split()
    a, b = set(input().split()), set(input().split())

    print(sum([1 for x in n if x in a]) - sum([1 for x in n if x in b]))


if __name__ == '__main__':
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
