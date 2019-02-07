#!/usr/bin/env python3.7
from sys import exc_info
from traceback import print_exception


def main():
    """Main"""
    ln = int(input())
    s = set()
    for i in range(ln):
        s.add(input().strip())

    print(len(s))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(print_exception(*exc_info()))
