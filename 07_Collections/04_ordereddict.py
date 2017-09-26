#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-09-12

HackkerRank

https://www.hackerrank.com/challenges/py-collections-ordereddict/
"""

from collections import OrderedDict


def main():
    """
    Main-Logic
    """
    od = OrderedDict()
    for _ in range(int(input())):
        item, space, price = input().rpartition(' ')
        od[item] = od.get(item, 0) + int(price)
    print(*[' '.join([item, str(price)]) for item, price in od.items()], sep='\n')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
