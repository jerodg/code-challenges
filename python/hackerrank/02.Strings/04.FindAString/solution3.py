#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.23

https://github.com/jerodg/hackerrank
"""
import sys
import traceback


def count_substring(string, sub_string) -> int:
    """Jerod Gawne, 2017-10-04

    Count Substring

    Counts the number of occurences of sub_string in string

    :param string: str
    :param sub_string: str
    :return: int
    """
    count = 0
    while sub_string in string:
        count += 1
        string = string[string.find(sub_string) + 1:]
    return count


if __name__ == "__main__":
    try:
        string = input().strip()
        sub_string = input().strip()
        print(count_substring(string, sub_string))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
