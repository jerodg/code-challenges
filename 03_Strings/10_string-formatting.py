#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""Jerod Gawne, 2017-10-

String Formatting

https://www.hackerrank.com/challenges/python-string-formatting/

Editorial:
 -

Sample Input:
17

Sample Output:
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""


def print_formatted(number):
    """

    :param number:
    :return:
    """
    data = []
    for i in range(1, number+1):
        data.append([str(i), str(oct(i))[2:], str(hex(i))[2:], str(bin(i))[2:]])

    width = max(len(word) for row in data for word in row) + 2
    for row in data:
        print(''.join(word.rjust(width) for word in row))


def main():
    """
    Main/Tests
    """
    n = int(input())
    print_formatted(n)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
