#!/usr/bin/env python3.7
"""Find Angle MBC: Jerod Gawne, 2019.02.19 <https://github.com/jerodg>"""
from math import atan2, degrees
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    ab, bc = int(input()), int(input())
    print(str(int(round(degrees(atan2(ab, bc))))) + "°")


if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
