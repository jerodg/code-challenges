#!/usr/bin/env python3.8
"""
Calendar Jerod Gawne, 2020.02.10 <https://github.com/jerodg/hackerrank>
"""

import datetime as dt
from calendar import day_name


def main():
    print(day_name[dt.datetime.strptime(input(), '%m %d %Y').weekday()].upper())


if __name__ == '__main__':
    main()
