#!/usr/bin/env python3.8
"""
Athlete Sort Jerod Gawne, 2021.01.22 <https://github.com/jerodg/hackerrank>
"""


def main():
    n, m = map(int, input().split())
    rows = [input() for _ in range(n)]
    k = int(input())

    for r in sorted(rows, key=lambda row: int(row.split()[k])):
        print(r)


if __name__ == "__main__":
    main()
