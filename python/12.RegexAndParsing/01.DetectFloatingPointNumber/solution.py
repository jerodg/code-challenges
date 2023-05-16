#!/usr/bin/env python3.11
"""
Detect Floating Point Number Jerod Gawne, 2023.05.16 <https://github.com/jerodg/hackerrank>
"""
import re

float_re = re.compile(r'[+-]?\d*\.\d+')


def main():
    for _ in range(int(input())):
        print(bool(re.fullmatch(float_re, input())))


if __name__ == '__main__':
    main()
