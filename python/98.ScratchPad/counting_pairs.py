#!/usr/bin/env python3.10
"""Counting Pairs
(C) Jerod Gawne, 2021.09.28 <https://github.com/jerodg>"""


def count_pairs(numbers: list, k: int) -> int:
    answer = 0

    s = set(numbers)
    for v in s:
        if v + k in s:
            answer += 1

    return answer


if __name__ == '__main__':
    numbers = [int(input().strip()) for x in range(int(input().strip()))]

    k = int(input().strip())

    print(count_pairs(numbers, k))
