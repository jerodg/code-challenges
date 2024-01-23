#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.08

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == "__main__":
    try:
        n = int(input())

        if n in range(1, 101):
            if bool(n & 1):
                print("Weird")
            elif n in range(2, 6):
                print("Not Weird")
            elif n in range(6, 21):
                print("Weird")
            elif n > 20:
                print("Not Weird")
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
