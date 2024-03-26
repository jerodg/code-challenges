#!/usr/bin/env python3.8
"""
Incorrect Regex Jerod Gawne, 2020.02.16 <https://github.com/jerodg/hackerrank>
"""
import re


def main():
    for _ in range(0, int(input())):
        try:
            re.compile(input())
            print(True)
        except re.error:
            print(False)


if __name__ == "__main__":
    main()
