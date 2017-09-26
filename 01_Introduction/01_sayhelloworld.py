#!/usr/bin/python3.6
"""
Jerod Gawne, 2016-09-19

HackkerRank
Say "Hello, World!" With Python
https://www.hackerrank.com/challenges/py-hello-world/
"""


def main():
    """
    Main-Logic
    """
    print('Hello World!')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))