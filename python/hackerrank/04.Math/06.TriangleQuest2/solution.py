#!/usr/bin/env python3.7
"""Triangle Quest 2: Jerod Gawne, 2019.02.19 <https://github.com/jerodg>"""

from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    for i in range(1, int(input()) + 1):
        print(((10**i - 1) // 9) * ((10**i - 1) // 9))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(print_exception(*exc_info()))
