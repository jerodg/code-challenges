#!/usr/bin/python3.6
"""Jerod Gawne, 2017-09-28

Nested List

https://www.hackerrank.com/challenges/nested-list/

Editorial:
 -
"""


def main():
    """
    Main/Tests
    """
    grades = [[input(), float(input())] for _ in range(int(input()))]
    second_lowest = sorted(list(set([grade for name, grade in grades])))[1]
    print(*[a for a, b in sorted(grades) if b == second_lowest], sep='\n')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
