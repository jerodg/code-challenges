#!/usr/bin/env python3.7
# coding=utf-8

"""Jerod Gawne, 2018.07.18
"""

import operator
import re

if __name__ == '__main__':
    string = re.sub(r'[^A-Za-z]', '', input()).lower()
    total, x, d = 0, 26, {}
    d.update({_: string.count(_) for _ in string})
    data = sorted(d.items(), key=operator.itemgetter(1))[::-1]

    for i in data:
        total += i[1] * x
        x -= 1
    print(total)
