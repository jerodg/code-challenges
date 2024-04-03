#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.26

https://github.com/jerodg/hackerrank

This doesn't actually solve the problem but it's cool non the less.
Reference: https://www.hackerrank.com/challenges/text-alignment/forum/comments/317258
"""
import math
import sys
import traceback

if __name__ == "__main__":
    try:
        c = "♥"
        width = 40

        print((c * 2).center(width // 2) * 2)

        for i in range(1, width // 10 + 1):
            print(((c * int(math.sin(math.radians(i * width // 2)) * width // 4)).rjust(width // 4) + (
                    c * int(math.sin(math.radians(i * width // 2)) * width // 4)).ljust(width // 4)) * 2)

        for i in range(width // 4, 0, -1):
            print((c * i * 4).center(width))
        print((c * 2).center(width))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
