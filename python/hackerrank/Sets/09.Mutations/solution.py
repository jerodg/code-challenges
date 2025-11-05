#!/usr/bin/env python3.7
"""03.Sets/09.Mutations: Jerod Gawne, 2019.02.12 <https://github.com/jerodg>"""

from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    input()
    a = set(input().split())

    for _ in range(int(input())):
        cmd, *args = input().split()
        getattr(a, cmd)(set(input().split()))

    print(sum(map(int, a)))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(print_exception(*exc_info()))
