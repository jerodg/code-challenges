#!/usr/bin/env python3.7
"""The Captains Rooms: Jerod Gawne, 2019.02.13 <https://github.com/jerodg>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    k, arr = int(input()), list(map(int, input().split()))
    print(((sum(set(arr)) * k) - (sum(arr))) // (k - 1))


if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
