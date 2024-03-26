#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.22

https://github.com/jerodg/hackerrank
"""
import sys
import traceback


def print_full_name(first, last) -> None:
    """Jerod Gawne, 2018.06.22

    Print Full Name

    Accepts two strings and prints a greeting.

    :param first: str
    :param last: str
    :return: None
    """
    print("Hello {} {}! You just delved into hackerrank.".format(first, last))


if __name__ == "__main__":
    try:
        print_full_name(input(), input())
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
