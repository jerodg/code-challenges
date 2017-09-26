#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-06-27

HackkerRank

https://www.hackerrank.com/challenges/simple-array-sum
"""


def main():
    """
    Main-Logic
    """
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    ans = 0
    for i in arr:
        ans += i

    print(ans)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))