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
        cmd = input().split()

        if cmd[0] == 'pop':
            s.pop()
        elif cmd[0] == 'remove':
            s.remove(int(cmd[1]))
        elif cmd[0] == 'discard':
            s.discard(int(cmd[1]))

    print(sum(s))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(print_exception(*exc_info()))
