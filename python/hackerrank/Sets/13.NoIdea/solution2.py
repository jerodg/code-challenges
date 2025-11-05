#!/usr/bin/env python3.7
"""No Idea: Jerod Gawne, 2019.02.18 <https://github.com/jerodg>"""

from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    _ = input()
    n = input().split()
    a = set(input().split())
    b = set(input().split())

    print(sum([(i in a) - (i in b) for i in n]))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(print_exception(*exc_info()))
