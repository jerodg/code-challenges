#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-05-20

HackkerRank

https://www.hackerrank.com/challenges/python-loops/
"""


def main():
    """
    Main-Logic
    """
    n = int(input())
    if 1 <= n <= 20:
        [print(i**2) for i in range(0, n)]


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))