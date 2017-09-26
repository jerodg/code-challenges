#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-04-19

HackkerRank

https://www.hackerrank.com/challenges/python-division/
"""


def main():
    """
    Main-Logic
    """
    a = int(input())
    b = int(input())
    if b != 0:
        print(a//b)
        print(a/b)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))