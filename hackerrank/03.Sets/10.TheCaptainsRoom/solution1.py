#!/usr/bin/env python3.7
"""The Captains Rooms: Jerod Gawne, 2019.02.13 <https://github.com/jerodg>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    _, s = int(input()), input().split()
    d = {}
    for item in s:
        try:
            d[item] += 1
        except KeyError:
            d[item] = 1

    for k, v in d.items():
        if v == 1:
            print(k)
            break


if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
