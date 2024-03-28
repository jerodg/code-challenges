#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.10.10 <https://github.com/jerodg>"""
import collections
import sys
import traceback

if __name__ == "__main__":
    try:
        _, inventory = input(), collections.Counter(list(map(int, input().split())))
        balance = 0
        for size, cost in [map(int, input().split()) for _ in range(int(input()))]:
            if inventory[size] > 0:
                inventory[size] -= 1
                balance += cost
        print(balance)

    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
