#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-09-12

HackkerRank

https://www.hackerrank.com/challenges/ginorts
"""


def main():
    """
    Main-Logic
    """
    print(*sorted(input(), key=lambda x: (x.isdigit() - x.islower(), x in '02468', x)), sep='')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
