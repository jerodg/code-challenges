#!/usr/bin/env python3.7
"""No Idea: Jerod Gawne, 2019.02.18 <https://github.com/jerodg>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    _ = input()
    n = input().split()
    a, b = set(input().split()), set(input().split())
    h = 0

    for i in a:
        if i in n:
            h += 1

    for i in b:
        if i in n:
            h -= 1

    print(h)


if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
