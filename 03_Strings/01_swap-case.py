#!/usr/bin/python3.6
"""Jerod Gawne, 2017-10-02

Swap Case

https://www.hackerrank.com/challenges/swap-case/

Editorial:
 -
"""


def swap_case(s):
    """
    Reverse Case

    :param s:
    :return:
    """
    return ''.join([l.upper() if l.islower() else l.lower() for l in s])


def main():
    """
    Main/Tests
    """
    print(swap_case(input()))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
