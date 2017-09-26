#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-06-23

HackkerRank

https://www.hackerrank.com/challenges/solve-me-first/
"""


def solvemefirst(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a + b


def main():
    """
    Main-Logic
    """
    num1 = int(input())
    num2 = int(input())
    print(solvemefirst(num1, num2))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
