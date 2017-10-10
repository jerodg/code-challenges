#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""Jerod Gawne, 2017-10-

String Formatting

https://www.hackerrank.com/challenges/python-string-formatting/

Editorial:
We can solve this challenge using the .format tool.
"{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width)
0 is the index indicating which format argument should be placed in that spot.
width indicates the padding space between two rows.
d, o, X and b converts the string into decimal, octal, hexadecimal, and binary format, respectively.

Note: Capital X is used to print the hexadecimal characters in uppercase.

Another Approach
We can solve this using the rjust function to align the rows.
The oct, hex and bin can be used to convert the integer into octal, hexadecimal and binary format, respectively.4

def fun(N):
    width = len(bin(N)) - 2
    for i in range(1,N+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width)

n = input()
fun(n)

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


def print_formatted(n):
    """

    :param n:
    :return:
    """
    width = len("{0:b}".format(n))
    for i in range(1, n + 1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=width))


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
