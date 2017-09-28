#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-05-20

Loops

https://www.hackerrank.com/challenges/python-loops/

Editorial
 - Use loops to iterate over the range.

for i in range(int(raw_input())):
    print i**2
"""


def main():
    """
    Main
    """
    [print(i ** 2) for i in range(int(input()))]


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))