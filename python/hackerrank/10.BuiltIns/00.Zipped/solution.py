#!/usr/bin/env python3.8
"""
Zipped Jerod Gawne, 2020.08.06 <https://github.com/jerodg/hackerrank>
"""


def main():
    n, x = map(int, input().split())

    sheet = [map(float, input().split()) for _ in range(x)]

    [print(sum(i) / len(i)) for i in zip(*sheet)]


if __name__ == '__main__':
    main()
