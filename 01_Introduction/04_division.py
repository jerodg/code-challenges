#!/usr/bin/python3.6
"""Jerod Gawne, 2017-04-19

Division

https://www.hackerrank.com/challenges/python-division/

Editorial

a = int(input())
b = int(input())

print(a // b)
print(a / b)
"""


def main():
    """
    Main-Logic
    """
    a, b = int(input()), int(input())

    print((a // b), (a / b), sep='\n')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))