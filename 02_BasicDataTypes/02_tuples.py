#!/usr/bin/python3.6
"""Jerod Gawne, 2017-09-26

HackkerRank Challenge Tuples

https://www.hackerrank.com/challenges/python-tuples/

Editorial:
 - hash() is one of the functions in __builtins__ module, so we just need to
   create a tuple of the 'n' elements and then pass it to the hash() function.

n = raw_input()
print hash(tuple([int(i) for i in raw_input().split()]))
"""


def main():
    """
    Main/Tests
    """
    # The tests output this as the quantity of numbers provided next It has no use in Python
    n = int(input())

    print(tuple(map(int, input().split())))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
