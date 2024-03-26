#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.

https://github.com/jerodg/hackerrank
"""
import sys
import traceback
import math
import os
import random
import re


def fizzBuzz(n):
    for i in range(1, n + 1):
        if i != 0:
            if i % 3 == 0 and i % 5 == 0:
                print('FizzBuzz')
            elif i % 3 == 0 and i % 5 != 0:
                print('Fizz')
            elif i % 5 == 0 and i % 3 != 0:
                print('Buzz')
            else:
                print(i)


if __name__ == '__main__':
    try:
        fizzBuzz(int(input()))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
