#!/usr/bin/env python3.7
"""Triangle Quest: Jerod Gawne, 2019.02.19 <https://github.com/jerodg>"""

from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    for i in range(1, int(input())):
        print(sum(map(lambda x: i * 10**x, range(i))))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(print_exception(*exc_info()))
