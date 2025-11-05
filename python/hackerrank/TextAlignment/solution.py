#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.26

https://github.com/jerodg/hackerrank
"""

import sys
import traceback

if __name__ == '__main__':
    try:
        thickness = int(input())  # This must be an odd number
        c = 'H'

        # Top Cone
        for i in range(thickness):
            print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

        # Top Pillars
        for i in range(thickness + 1):
            print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

        # Middle Belt
        for i in range((thickness + 1) // 2):
            print((c * thickness * 5).center(thickness * 6))

        # Bottom Pillars
        for i in range(thickness + 1):
            print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

        # Bottom Cone
        for i in range(thickness):
            print(
                ((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
                    thickness * 6
                )
            )
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
