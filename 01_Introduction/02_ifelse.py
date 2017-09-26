#!/usr/bin/python3.6
"""
Jerod Gawne, 2016-09-20

HackkerRank

https://www.hackerrank.com/challenges/py-if-else/
"""


def main():
    """
    Main-Logic
    """
    n = int(input().strip())

    if n in range(1, 101):
        if bool(n & 1):
            print('Weird')
        elif n in range(2, 6):
            print('Not Weird')
        elif n in range(6, 21):
            print('Weird')
        elif n > 20:
            print('Not Weird')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
