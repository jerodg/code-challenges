#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-09-12

HackkerRank

https://www.hackerrank.com/challenges/py-collections-deque/
"""

from collections import deque


def main():
    """
    Main-Logic
    """
    dq, it = deque(), [input().split() for _ in range(int(input()))]
    [getattr(dq, c)(*args) for c, *args in it]
    print(*dq, sep=' ')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
