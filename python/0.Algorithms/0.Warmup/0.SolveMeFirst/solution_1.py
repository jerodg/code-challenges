#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.07

https://www.hackerrank.com/challenges/solve-me-first/problem
"""
import sys
import traceback


def solvemefirst(a, b) -> int:
    """Solve Me First

    :param a: int
    :param b: int
    :return: int
    """
    # Hint: Type return a+b below
    return a + b


def main():
    """
    Main/Tests
    """
    num1 = int(input())
    num2 = int(input())

    print(solvemefirst(num1, num2))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
