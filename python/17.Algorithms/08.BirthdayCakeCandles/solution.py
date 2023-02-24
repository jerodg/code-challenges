#!/usr/bin/env python3.11
"""Birthday Cake Candles
Jerod Gawne, 2023.02.24 <https://github.com/jerodg/hackerrank>
"""


def birthday_cake_candles(ls: list) -> int:
    m = max(ls)
    return ls.count(m)


def main():
    _ = int(input())  # unused

    candles = list(map(int, input().rstrip().split()))

    print(birthday_cake_candles(candles))


if __name__ == '__main__':
    main()
