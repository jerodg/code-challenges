#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.28

https://github.com/jerodg/hackerrank
"""
import sys
import traceback


def print_formatted(n) -> None:
    """ Jerod Gawne 2017.10.13

    Print Formatted

    :param n: int
    :return: None
    """
    width = len("{0:b}".format(n))
    for i in range(1, n + 1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=width))


if __name__ == '__main__':
    try:
        print_formatted(int(input()))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
