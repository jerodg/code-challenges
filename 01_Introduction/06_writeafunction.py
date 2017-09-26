#!/usr/bin/python3.6
"""
Jerod Gawne, 2016-09-19

HackkerRank

https://www.hackerrank.com/challenges/write-a-function/
"""


def is_leap(year):
    leap = False
    if 1900 <= year <= 10 ** 5:
        if not year % 4:
            leap = True
            if not year % 100:
                leap = False
                if not year % 400:
                    leap = True

    return leap


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