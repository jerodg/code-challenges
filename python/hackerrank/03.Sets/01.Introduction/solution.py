#!/usr/bin/env python3.7
"""Jerod Gawne, 2018.10.02 <https://github.com/jerodg>"""
import sys
import traceback
from typing import NoReturn


def average(array) -> NoReturn:
    """
    :param array: list
    :return: NoReturn"""
    s = set(array)
    return sum(s) / len(s)


if __name__ == "__main__":
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        result = average(arr)
        print(result)
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
