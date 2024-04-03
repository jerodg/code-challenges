#!/usr/bin/env python3.8
"""
Zipped Jerod Gawne, 2020.08.06 <https://github.com/jerodg/hackerrank>
"""


def main():
    [print(sum(i) / len(i)) for i in zip(*[map(float, input().split()) for _ in range(int(input().split()[1]))])]


if __name__ == "__main__":
    main()
