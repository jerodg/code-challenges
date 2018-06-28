#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.28

https://github.com/jerodg/hackerrank
"""
import sys
import traceback


def capitalize(string) -> str:
    """Jerod Gawne, 2017.10.13

    print(input().title()) will not work because the question is
    asking to capitalise firse letter of each word keeping in mind
    that "if it is a letter". Title and Capitalise are different in function as:
    'abcd'.title() results in 'Abcd' but
    '12abcd'.title() results in '12Abcd'. This is not what we want.

    We just want to capitalise first letter of each word, not the first occuring letter of a word.

    :param string: str
    :return: str
    """
    return ' '.join((word.capitalize() for word in string.split(' ')))


if __name__ == '__main__':
    try:
        capitalize(input())
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
