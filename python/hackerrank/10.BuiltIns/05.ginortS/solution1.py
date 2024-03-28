#!/usr/bin/env python3.9
"""
ginortS Jerod Gawne, 2021.01.2 <https://github.com/jerodg/hackerrank>
"""


def main():
    print(
        *sorted(
            input(),
            key=lambda x: (
                x.isdigit() and int(x) % 2 == 0,
                x.isdigit(),
                x.isupper(),
                x.islower(),
                x,
            ),
        ),
        sep="",
    )


if __name__ == "__main__":
    main()
