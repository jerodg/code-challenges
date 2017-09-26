#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-09-12

HackkerRank

https://www.hackerrank.com/challenges/word-order/
"""

from collections import OrderedDict


def main():
    """
    Main-Logic
    """
    od = OrderedDict()
    for _ in range(int(input())):
        item = input()
        od[item] = od.get(item, 0) + 1

    print(len(od))
    print(*od.values(), sep=' ')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
