#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-09-10

Print

https://www.hackerrank.com/challenges/python-print/

Editorial:
 - Using the map() and the print _function, we can solve this in one line.

print(*range(1, int(input()) + 1), sep="")
"""


def main():
    """
    Main
    """
    print(*range(1, int(input()) + 1), sep='')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))