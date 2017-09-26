#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-09-26

HackkerRank

https://www.hackerrank.com/challenges/python-tuples/
"""


def main():
    """
    Main/Tests
    """
    n = int(input())
    ints = tuple(map(int, input().split()))
    print(hash(ints))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
