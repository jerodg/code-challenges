#!/usr/bin/env python3.6
"""Jerod Gawne, 2017-10-13

Alphabet Rangoli

https://www.hackerrank.com/challenges/alphabet-rangoli

Editorial:
 -

Sample Input:
5

Sample Output:
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""


def print_rangoli(size):
    """

    :param size: int
    :return: None
    """
    import string
    alpha = string.ascii_lowercase

    ls = []
    for i in range(size):
        s = '-'.join(alpha[i:size])
        ls.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))

    print(*(ls[:0:-1] + ls), sep='\n')


def main():
    """
    Main/Tests
    """
    n = int(input())
    print_rangoli(n)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
