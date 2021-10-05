#!/usr/bin/env python3.9
"""
Plus Minus
(c) 2021 Jerod Gawne, 2021.10.05 <https://github.com/jerodg/hackerrank>
"""


def plus_minus(arr):
    pos = 0
    neg = 0
    zer = 0
    lng = len(arr)

    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        elif x == 0:
            zer += 1

    pos /= lng
    neg /= lng
    zer /= lng

    return pos, neg, zer


def main():
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    res = plus_minus(arr)

    for x in res:
        print(f'{x:.6f}')


if __name__ == '__main__':
    main()
