# !/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.07

https://github.com/jerodg/hackerrank
"""

import sys
import traceback


def score(alice, bob) -> tuple:
    """Score

    Accepts two lists and awards one point for the higher score

    :param alice: list
    :param bob: list
    :return: tuple
    """
    a = b = 0

    for i, j in zip(alice, bob):
        if i > j:
            a += 1
        elif i < j:
            b += 1

    return a, b


def main():
    """
    Main/Tests
    """
    alice = map(int, input().split())
    bob = map(int, input().split())

    print(' '.join(map(str, score(alice, bob))))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
