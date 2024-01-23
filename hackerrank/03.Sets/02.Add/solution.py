#!/usr/bin/env python3.7
from sys import exc_info
from traceback import print_exception


def main():
    """Main"""
    print(len(set({input().strip() for _ in range(int(input()))})))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(print_exception(*exc_info()))
