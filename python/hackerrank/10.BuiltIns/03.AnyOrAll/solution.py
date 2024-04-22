#!/usr/bin/env python3.8
"""
Any or All Jerod Gawne, 2020.08.12 <https://github.com/jerodg/hackerrank>
"""


def main():
    n, ls = input(), list(map(int, input().split()))
    print(all(i > 0 for i in ls) and any(((str(x))[::-1] == str(x) for x in ls)))


if __name__ == '__main__':
    main()
