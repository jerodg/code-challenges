#!/usr/bin/env python3.7
"""Set Discard, Remove Pop: Jerod Gawne, 2019.01.18 <https://github.com/jerodg/hackerrank>"""
from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    """Main"""
    _ = int(input())
    s = set(map(int, input().split()))
    for _ in range(int(input())):
        method, *args = input().split()
        getattr(s, method)(*map(int, args))

    print(sum(s))


if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print(print_exception(*exc_info()))
