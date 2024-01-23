#!/usr/bin/env python3.8
"""
Piling Up: Jerod Gawne, 2020.02.03 <https://github.com/jerodg/hackerrank>
"""
from collections import deque


def main():
    for _ in range(int(input())):
        input()  # Discard length of list
        side_lengths = deque(map(int, input().strip().split()))
        if max(side_lengths) not in (side_lengths[0], side_lengths[-1]):
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
