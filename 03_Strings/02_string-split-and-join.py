#!/usr/bin/python3.6
"""Jerod Gawne, 2017-10-02

String Split and Join

https://www.hackerrank.com/challenges/python-string-split-and-join/

Editorial:
 -
"""


def split_and_join(line):
    """
    Splits line on space and joins with hyphen

    :param line:
    :return:
    """
    return '-'.join(line.split())


def main():
    """
    Main/Tests
    """
    print(split_and_join('this is a string'))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
