#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.07

https://www.hackerrank.com/challenges/
"""
import sys
import traceback


def solvemefirst(a, b):
    # Hint: Type return a+b below
    pass


def main():
    """
    Main/Tests
    """
    num1 = int(input())
    num2 = int(input())
    res = solvemefirst(num1, num2)
    print(res)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
