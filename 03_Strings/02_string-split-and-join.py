#!/usr/bin/python3.6
"""Jerod Gawne, 2017-10-02

String Split and Join

https://www.hackerrank.com/challenges/python-string-split-and-join/

Editorial:
 -Using the split and join methods, we can solve this challenge.

print "-".join(raw_input().split())
"""


def main():
    """
    Main/Tests
    """
    print(*input().split(), sep='-')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
