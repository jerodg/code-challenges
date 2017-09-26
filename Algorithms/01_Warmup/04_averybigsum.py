#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-06-27

HackkerRank

https://www.hackerrank.com/challenges/a-very-big-sum
"""


def averybigsum(n, ar):
    ans = 0
    for i in ar:
        ans += i
    return ans


def main():
    """
    Main-Logic
    """
    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    result = averybigsum(n, ar)
    print(result)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))