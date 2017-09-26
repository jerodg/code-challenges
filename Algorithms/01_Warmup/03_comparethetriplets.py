#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-06-25

HackkerRank

https://www.hackerrank.com/challenges/compare-the-triplets
"""


def solve(a0, a1, a2, b0, b1, b2):
    ehs = [a0, a1, a2]
    bees = [b0, b1, b2]
    a = 0
    b = 0
    for i, j in zip(ehs, bees):
        if i > j:
            a += 1
        elif i < j:
            b += 1
    return a, b


def main():
    """
    Main-Logic
    """
    a0, a1, a2 = input().strip().split(' ')
    a0, a1, a2 = [int(a0), int(a1), int(a2)]
    b0, b1, b2 = input().strip().split(' ')
    b0, b1, b2 = [int(b0), int(b1), int(b2)]
    result = solve(a0, a1, a2, b0, b1, b2)
    print(" ".join(map(str, result)))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
