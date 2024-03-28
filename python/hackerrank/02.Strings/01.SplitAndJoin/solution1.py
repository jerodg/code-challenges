#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.21

https://github.com/jerodg/hackerrank
"""
import sys
import traceback


def split_and_join(line) -> str:
    """Jerod Gawne, 2018.06.21

    Split and Join

    Splits a string by space and joins by hyphen '-'

    :param line: str
    :return: str
    """
    return "-".join(line.split(" "))


if __name__ == "__main__":
    try:
        print(split_and_join(input()))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
