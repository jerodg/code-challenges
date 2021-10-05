#!/usr/bin/env python3.9
"""
Staircase Jerod Gawne, 2021.10.05 <https://github.com/jerodg/hackerrank>
"""


def main():
    n = int(input().strip())

    for i in range(1, n + 1):
        print(str('#'*i).rjust(n))


if __name__ == '__main__':
    main()
