#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.07.10

https://github.com/jerodg/hackerrank
"""
import collections
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
    [print("".join(collections.OrderedDict.fromkeys(c).keys())) for c in chunks]


if __name__ == "__main__":
    try:
        merge_the_tools(input(), int(input()))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
