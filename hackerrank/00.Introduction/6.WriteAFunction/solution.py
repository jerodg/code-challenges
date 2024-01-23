#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.11

https://github.com/jerodg/hackerrank
"""
import sys
import traceback


def is_leap(year) -> int:
    """Jerod Gawne, 2016.09.19

    Checks if a year is a leap-year

    :param year: int
    :return: bool
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


if __name__ == "__main__":
    try:
        print(is_leap(int(input())))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
