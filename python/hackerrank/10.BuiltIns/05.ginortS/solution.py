#!/usr/bin/env python3.9
"""
ginortS Jerod Gawne, 2021.01.2 <https://github.com/jerodg/hackerrank>
"""


def main():
    print(*sorted(input().strip(), key=lambda x: (-x.islower(), x.isdigit() - x.isupper(), x in "02468", x), ), sep="", )


if __name__ == "__main__":
    main()
