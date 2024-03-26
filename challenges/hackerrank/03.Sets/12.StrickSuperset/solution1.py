#!/usr/bin/env python3.7
"""Strict Supersets: Jerod Gawne, 2019.02.18 <https://github.com/jerodg>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    a = set(input().split())
    for _ in range(int(input())):
        if not set(input().split()).issuperset(a):
            print("False")
            break
        print("True")


if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
