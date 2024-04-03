#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.07.10

https://github.com/jerodg/hackerrank
"""
import sys
import traceback


def merge_the_tools(string, k) -> None:
    """Jerod Gawne, 2018.07.10

    Merge The Tools

    :param string: str
    :param k: int
    :return: None
    """
    chunks = [string[x: x + k] for x in range(0, len(string), k)]

    # This only works in Python 3.6+ due to ordered dicts by default
    # It doesn't work with the online interpreter because it doesn't support this
    [print("".join(dict.fromkeys(c).keys())) for c in chunks]


if __name__ == "__main__":
    try:
        merge_the_tools(input(), int(input()))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
