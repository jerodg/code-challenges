#!/usr/bin/python3.6
"""Jerod Gawne, 2017-10-04

What's Your Name?

https://www.hackerrank.com/challenges/whats-your-name/

Editorial:
 -Use + for string concatenation.

a = input()
b = input()
print("Hello %s %s! You just delved into python." % (a,b))
"""


def main():
    """
    Main/Tests
    """
    print(f'Hello {input()} {input()}! You just delved into python.')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
