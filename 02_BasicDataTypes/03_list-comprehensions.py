#!/usr/bin/python3.6
"""Jerod Gawne, 2017-09-28

List Comprehensions

https://www.hackerrank.com/challenges/list-comprehensions

Editorial:
 -List comprehensions are an elegant way where lists can be built without having
  to use different for loops to append values one by one.
"""


def main():
    """
    Main/Tests
    """
    x, y, z, n = (int(input()) for _ in range(4))
    print([[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n])


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
