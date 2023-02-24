#!/usr/bin/env python3.9
"""
Plus Minus
(c) 2021 Jerod Gawne, 2021.10.05 <https://github.com/jerodg/hackerrank>
"""


def main():
    n = int(input())
    lst = [int(x) for x in input().split()]
    print(f'{len([x for x in lst if x > 0]) / n:.6f}')
    print(f'{len([x for x in lst if x < 0]) / n:.6f}')
    print(f'{len([x for x in lst if x == 0]) / n:.6f}')


if __name__ == '__main__':
    main()
