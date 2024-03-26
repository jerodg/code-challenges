#!/usr/bin/env python3.7
"""Triangle Quest: Jerod Gawne, 2019.02.19 <https://github.com/jerodg>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    for i in range(1, int(input())):
        print(i * 10**i / 9)


if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
