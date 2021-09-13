#!/usr/bin/env python3.9
"""Diagonal Difference

Copyright ©2021 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""


def diagonal_difference(arr: list) -> int:
    n = len(arr)
    ltrd = sum(arr[i][n - i - 1] for i in range(n))
    rtld = sum(arr[n - i - 1][n - i - 1] for i in range(n))

    return abs(rtld - ltrd)


def main():
    n = int(input().strip())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(diagonal_difference(arr))


if __name__ == '__main__':
    main()
