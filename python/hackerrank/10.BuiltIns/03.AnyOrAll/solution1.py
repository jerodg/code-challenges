#!/usr/bin/env python3.8
"""
Any or All Jerod Gawne, 2020.08.12 <https://github.com/jerodg/hackerrank>
"""


def main():
    n, arr = int(input()), input().split()
    print(all(int(i) >= 0 for i in arr) and any(i == i[::-1] for i in arr))


if __name__ == '__main__':
    main()
