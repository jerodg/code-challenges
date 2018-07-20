#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.28

https://github.com/jerodg/hackerrank
"""
import string
import sys
import traceback


def print_rangoli(size):
    """Jerod Gawne, 2017.10.13

    Print Rangoli

    If n is the number of unique letters we will be printing,
    then we end up printing twice this many in any given row.
    We are also printing a '-' for each letter, so now we're
    at 4n characters total. BUT we do no re-print the "middle"
    character, so it and its character are substracted from the
    total. So 4n-2. Now, we also don't want to print the trailing
    '-' so subtract 1 more. Thus, 4n-3 is the width.

    :param size: int
    :return: None
    """
    alpha = string.ascii_lowercase

    ls = []
    for i in range(size):
        s = '-'.join(alpha[i:size])
        ls.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))

    print(*(ls[:0:-1] + ls), sep='\n')


if __name__ == '__main__':
    try:
        print_rangoli(int(input()))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
