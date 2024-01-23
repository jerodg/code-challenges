#!/usr/bin/env python3.7
"""Triangle Quest 2: Jerod Gawne, 2019.02.19 <https://github.com/jerodg>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    for i in range(1, int(input()) + 1):
        print(
            [
                1,
                121,
                12321,
                1234321,
                123454321,
                12345654321,
                1234567654321,
                123456787654321,
                12345678987654321,
            ][i - 1]
        )


if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
