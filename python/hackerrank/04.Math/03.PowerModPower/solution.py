#!/usr/bin/env python3.7
"""Power ModPower: Jerod Gawne, 2019.02.19 <https://github.com/jerodg>"""

from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    a, b, m = int(input()), int(input()), int(input())
    print(pow(a, b), pow(a, b, m), sep='\n')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(print_exception(*exc_info()))
