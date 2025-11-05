#!/usr/bin/env python3.7
"""03.Sets/09.Mutations: Jerod Gawne, 2019.02.08 <https://github.com/jerodg>"""

from sys import exc_info
from traceback import print_exception
from typing import NoReturn


def main() -> NoReturn:
    _, a, n = input(), set(map(int, input().split())), int(input())
    for i in range(n):
        cmd, _ = input().split()
        b = set(map(int, input().split()))

        if cmd == 'intersection_update':
            a.intersection_update(b)
        elif cmd == 'update':
            a.update(b)
        elif cmd == 'symmetric_difference_update':
            a.symmetric_difference_update(b)
        elif cmd == 'difference_update':
            a.difference_update(b)

    print(sum(a))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(print_exception(*exc_info()))
