#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.28

https://github.com/jerodg/hackerrank
"""
import sys
import traceback


def print_rangoli(n) -> None:
    """Jerod Gawne, 2017.06.28

    Print Rangoli

    :param n: int
    :return: None
    """
    for i in range(n):
        s = "-".join(chr(ord('a') + n - j - 1) for j in range(i + 1))
        print((s + s[::-1][1:]).center(n * 4 - 3, '-'))

    for i in range(n - 1):
        s = "-".join(chr(ord('a') + n - j - 1) for j in range(n - i - 1))
        print((s + s[::-1][1:]).center(n * 4 - 3, '-'))


if __name__ == '__main__':
    try:
        print_rangoli(int(input()))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
