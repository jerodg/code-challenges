#!/usr/bin/env python3.7
"""03.Sets/06.Intersection: Jerod Gawne, 2019.02.07 <https://github.com/jerodg>"""

from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    _, s = int(input()), set(input().split())
    _, s2 = int(input()), set(input().split())
    print(len(s.intersection(s2)))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(print_exception(*exc_info()))
