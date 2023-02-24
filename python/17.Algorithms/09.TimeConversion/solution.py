#!/usr/bin/env python3.10
"""Time Conversion
Jerod Gawne, 2023.02.24 <https://github.com/jerodg/hackerrank>
"""
from datetime import *


def time_conversion(s: str) -> str:
    return str(datetime.strptime(s, '%I:%M:%S%p').time())


def main():
    print(time_conversion(input()))


if __name__ == '__main__':
    main()
