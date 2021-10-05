#!/usr/bin/env python3.9
"""
Staircase Jerod Gawne, 2021.10.05 <https://github.com/jerodg/hackerrank>
"""


def main():
    n = int(input().strip())
    cnt = n
    for x in range(n):
        out = ' ' * (cnt - 1)
        cnt -= 1
        out += '#' * (n - cnt)
        print(f'{out}')


if __name__ == '__main__':
    main()
