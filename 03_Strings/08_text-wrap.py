#!/usr/bin/python3.6
"""Jerod Gawne, 2017-10-05

Text Wrap

https://www.hackerrank.com/challenges/text-wrap/

Editorial:
 -

Sample Input
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

import textwrap


def wrap(s, width):
    """Jerod Gawne, 2017-10-05

    Wraps string limiting line length by width

    :param s:
    :param width:
    :return:
    """
    return textwrap.fill(s, width)


def wrap2(s, width):
    """Jerod Gawne, 2017-10-05

    credit: https://stackoverflow.com/a/13673133/4434405

    :param s:
    :param width:
    :return:
    """
    return [s[i:i + width] for i in range(0, len(s), width)]


def main():
    """
    Main/Tests
    """
    s, width = input(), int(input())

    print(wrap(s, width))
    print('\n')
    print(wrap2(s, width))
    print(*wrap2(s, width), sep='\n')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
