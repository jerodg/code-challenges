#!/usr/bin/env python3.7
"""Symmetric Difference: Jerod Gawne, 2019.01.17 <https://github.com/jerodg/hackerrank>"""
from sys import argv, exc_info, exit
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    """Main"""
    a, b = [set(input().split()) for _ in range(4)][1::2]
    print(*sorted(a ^ b, key=int), sep='\n')


if __name__ == '__main__':
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
