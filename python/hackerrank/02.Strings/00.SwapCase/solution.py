#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.21

https://github.com/jerodg/hackerrank
"""

import sys
import traceback


def swap_case(s) -> str:
    """Jerod Gawne, 2018.06.21

    Swap Case

    Returns a string with the 'case' swapped

    :param s: str
    :return: str
    """
    return s.swapcase()


if __name__ == '__main__':
    try:
        print(swap_case(input()))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
