#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.26

https://github.com/jerodg/hackerrank
"""
import re
import sys
import traceback


def wrap(s, w) -> list:
    """Jerod Gawne, 2017.10.05

    Wrap

    Wraps string limiting line length by width

    :param s: str
    :param w: int
    :return: list
    """
    return [x for x in re.split(f'(.{{{w}}})', s) if x]


if __name__ == '__main__':
    try:
        string, max_width = input(), int(input())
        result = wrap(string, max_width)
        print(*wrap(string, max_width), sep='\n')
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
