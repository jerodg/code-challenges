#!/usr/bin/env python3.8
"""
Athlete Sort Jerod Gawne, 2021.01.22 <https://github.com/jerodg/hackerrank>
"""

from operator import itemgetter


def main():
    lines, fields = input().split(' ')

    entries = []
    for x in range(int(lines)):
        entries.append(list(map(int, input().rstrip().split())))

    index = int(input())

    entries.sort(key=itemgetter(index))

    [print(*e) for e in entries]


if __name__ == '__main__':
    main()
