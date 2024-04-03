#!/usr/bin/env python3.11
"""
Copyright ©2022 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""


def spiral_order(matrix):
    """

    :param matrix:
    :return:
    """
    ln = max(map(len, matrix))
    ans = []

    if len(matrix) == 0:
        return ans

    m = len(matrix)
    n = len(matrix[0])
    seen = [[0 for i in range(n)] for j in range(m)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x = 0
    y = 0
    di = 0

    # Iterate from 0 to R * C - 1
    for i in range(m * n):
        ans.append(matrix[x][y])
        seen[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]

        if 0 <= cr < m and 0 <= cc < n and not (seen[cr][cc]):
            x = cr
            y = cc
        else:
            di = (di + 1) % (ln if ln % 2 == 0 else ln - 1)
            x += dr[di]
            y += dc[di]
    return ans


if __name__ == "__main__":
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print(*spiral_order(a))
