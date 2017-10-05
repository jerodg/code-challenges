#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""Jerod Gawne, 2017-10-05

Text Wrap

https://www.hackerrank.com/challenges/text-wrap/

Editorial:
 -This can be solved using the function textwrap.fill().

import textwrap
S = raw_input()
w = input()
print textwrap.fill(S,w)

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


def wrap(s, w):
    """Jerod Gawne, 2017-10-05

    Wraps string limiting line length by width

    :param s: str
    :param w: int
    :return: str
    """
    import textwrap

    return textwrap.fill(s, w)


def wrap2(s, w):
    """Jerod Gawne, 2017-10-05

    credit: https://stackoverflow.com/a/13673133/4434405

    :param s: str
    :param w: int
    :return: list
    """
    return [s[i:i + w] for i in range(0, len(s), w)]


def wrap3(s, w):
    """Jerod Gawne, 2017-10-05

    credit: https://stackoverflow.com/a/25250485/4434405

    :param s: str
    :param w: int
    :return: list
    """
    import functools
    import io

    return [l for l in iter(functools.partial(io.StringIO(s).read, w), '')]

    # If you have a file or socket, StringIO wrapper is not needed:
    # [l for l in iter(functools.partial(flo.read, width), '')]


def wrap4(s, w):
    """Jerod Gawne, 2017-10-05

    credit: https://stackoverflow.com/a/44103651/4434405

    :param s: str
    :param w: int
    :return: list
    """
    import re
    sre = re.compile(rf'(.{{{w}}})')
    return [x for x in re.split(sre, s) if x]


def main():
    """
    Main/Tests
    """
    s, width = input(), int(input())

    print(wrap(s, width))
    print('\n')
    print(*wrap2(s, width), sep='\n')
    print('\n')
    print(*wrap3(s, width), sep='\n')
    print('\n')
    print(*wrap4(s, width), sep='\n')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
