#!/usr/bin/python3.6
"""Jerod Gawne, 2016-09-21

Arithmetic Operators

https://www.hackerrank.com/challenges/python-arithmetic-operators/

Editorial
 - We can solve this problem by using basic arithmetic operators like +, - and *.

a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
"""


def main():
    """
    Main-Logic
    """
    a, b = int(input()), int(input())

    print(f'{a + b} \n{a - b} \n{a * b}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))