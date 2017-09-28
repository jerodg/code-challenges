#!/usr/bin/python3.6
"""
Jerod Gawne, 2016-09-19

Write a Function

https://www.hackerrank.com/challenges/write-a-function/

Editorial:

def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

print(is_leap(int(input())))
"""


def is_leap(year):
    """Jerod Gawne, 2016-09-19

    Checks if a year is a leap-year

    :param year: int
    :return: bool
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def main():
    """
    Main-Logic
    """
    print(is_leap(int(input())))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))