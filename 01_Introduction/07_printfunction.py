#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-09-10

HackkerRank

https://www.hackerrank.com/challenges/python-print/
"""


def main():
    """
    Main-Logic
    """
    n = int(input())
    s = ''
    for i in range(1, n+1):
        s += str(i)
    print(s)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))