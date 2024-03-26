# !/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.07

https://github.com/jerodg/hackerrank
"""
import sys
import traceback


def main() -> None:
    """
    Main/Tests
    """
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))

    print(
        sum(map(lambda x, y: x > y, alice, bob)),
        sum(map(lambda x, y: y > x, alice, bob)),
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
