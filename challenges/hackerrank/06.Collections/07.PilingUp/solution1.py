#!/usr/bin/env python3.8
"""
Piling Up: Jerod Gawne, 2020.02.03 <https://github.com/jerodg/hackerrank>
"""


def main():
    for t in range(int(input())):
        l = int(input())
        lst = list(map(int, input().split()))
        i = 0
        while i < l - 1 and lst[i] >= lst[i + 1]:
            i += 1

        while i < l - 1 and lst[i] <= lst[i + 1]:
            i += 1

        print("Yes" if i == l - 1 else "No")


if __name__ == "__main__":
    main()
