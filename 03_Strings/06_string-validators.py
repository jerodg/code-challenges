#!/usr/bin/python3.6
"""Jerod Gawne, 2017-10-05

String Validators

https://www.hackerrank.com/challenges/string-validators/

Editorial:
 -

Sample Input:
qA2

Sample Output:
True
True
True
True
True
"""


def main():
    """
    Main/Tests


    """
    s = input()
    s = list(s)
    print(any([c.isalnum() for c in s]))
    print(any([c.isalpha() for c in s]))
    print(any([c.isdigit() for c in s]))
    print(any([c.islower() for c in s]))
    print(any([c.isupper() for c in s]))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
