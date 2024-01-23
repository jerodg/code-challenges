#!/usr/bin/env python3.8
"""
Exceptions Jerod Gawne, 2020.02.16 <https://github.com/jerodg/hackerrank>
"""


def main():
    for _ in range(0, int(input())):
        try:
            k, m = map(int, input().split())
            print(k // m)
        # except Exception as excp:
        except BaseException as bexcp:
            print(f"Error Code: {excp}")


if __name__ == "__main__":
    main()
