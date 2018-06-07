#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.07

https://www.hackerrank.com/challenges/solve-me-first/problem
"""
import sys
import traceback


def main():
    """
    Main/Tests
    """
    print(sum((int(input()), int(input()))))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
