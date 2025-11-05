#!/usr/bin/env python3.8
"""
Time Delta Jerod Gawne, 2020.02.14 <https://github.com/jerodg/hackerrank>
"""

from datetime import datetime


def main():
    tme_fmt = '%a %d %b %Y %H:%M:%S %z'

    for _ in range(0, int(input())):
        t1 = datetime.strptime(input(), tme_fmt)
        t2 = datetime.strptime(input(), tme_fmt)

        print(int(abs((t1 - t2)).total_seconds()))


if __name__ == '__main__':
    main()
