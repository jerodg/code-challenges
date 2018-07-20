#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.22

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == '__main__':
    try:
        string = input()
        position, character = input().split()
        print(string[:position] + character + string[position + 1:])
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
