#!/usr/bin/python3.6
"""Jerod Gawne, 2017-10-02

Swap Case

https://www.hackerrank.com/challenges/swap-case/

Editorial:
 - Use the method string.swapcase(s) to swap lower case letters to upper case letters and vice versa.

import string
print string.swapcase(raw_input())
"""


def swap_case(s):
    """
    Reverse Case

    :param s:
    :return:
    """
    return ''.join([l.upper() if l.islower() else l.lower() for l in s])


def swap_case2(s):
    """
    Reverse Case

    Best Method

    :param s:
    :return:
    """
    return s.swapcase()


def swap_case3(s):
    """
    Reverse Case

    :param s:
    :return:
    """
    return "".join(map(str.swapcase, s))


def main():
    """
    Main/Tests
    """
    s = input()
    print(swap_case(s))
    print(swap_case2(s))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
