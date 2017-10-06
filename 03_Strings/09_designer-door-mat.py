#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""Jerod Gawne, 2017-10-06

Designer Door Mat

https://www.hackerrank.com/challenges/designer-door-mat/

Editorial:
Python String center() Method

Syntax
str.center(width[, fillchar])
width: Total width of the string.
fillchar: Filler character.

N,M = map(int,raw_input().split())
for i in xrange(1, N, 2):
    print ( str('.|.')*i ).center(M, '-')
print str('WELCOME').center(M, '-')
for i in xrange(N-2, -1, -2):
    print ( str('.|.')*i ).center(M, '-')

Sample Input:
9 27

Sample Output:
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""


def main():
    """
    Main/Tests

    line 1: srtaightforward.
    There are a couple things to notice.
    The first is that each line has a set number of repetitions of '.|.',
    which are centered, and the rest is filled by '-'.
    The second is that the flag is symmetrical, so if you have the top,
    you have the bottom by reversing it. You only need to work on n // 2
    (n is odd and you need the integer div because the remaining line is the "WELCOME" line).
    line 2: I generate 2\*i + 1 '.|.', center it, and fill the rest with '-'.
    That's basically the top part of the output.
    line 3: put things together. '\n'.join() should be straightforward. Then,
    the sequence of strings to join is the pattern described above, the middle
    'WELCOME' line, and the pattern reversed.
    """
    n, m = map(int,input().split())
    pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
    print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
