#!/usr/bin/env python3.7
# coding=utf-8

"""Jerod Gawne, 2018.07.18
"""
from itertools import combinations

if __name__ == '__main__':
    max_weight, num_items = map(int, input().split())

    items = []

    for _ in range(num_items):
        price, weight = map(int, input().split())
        items.append((price, weight))

    highest = 0
    for i in combinations(items, 2):
        psum = i[0][0] + i[1][0]
        if i[0][1] + i[1][1] <= max_weight and psum > highest:
            highest = psum

    print(highest)
