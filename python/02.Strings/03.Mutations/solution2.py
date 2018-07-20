#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.22

https://github.com/jerodg/hackerrank
"""
import sys
import traceback


def mutate_string(string, position, character) -> str:
    """Jerod Gawne, 2018.06.22

    Mutate String

    Changes string character at position to character.

    :param string: str
    :param position: str|int
    :param character: str
    :return: str
    """
    return ''.join([character if i == position else string[i] for i in range(len(string))])


if __name__ == '__main__':
    try:
        s = input()
        i, c = input().split()
        print(mutate_string(s, int(i), c))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
