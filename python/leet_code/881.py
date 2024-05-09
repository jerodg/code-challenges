"""
Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""

from json import loads
from sys import stdin


def numRescueBoats(p: list[int], limit: int) -> int:
    """
    Calculates the minimum number of rescue boats needed.

    The function sorts the list of people's weights, then uses a two-pointer approach to find the minimum number of boats.
    It starts with the lightest and heaviest person, and if they can fit in one boat, it moves both pointers. If not, it only moves the pointer for the heaviest person.

    Parameters
    ----------
    p : list[int]
        List of people's weights.
    limit : int
        Maximum weight a boat can carry.

    Returns
    -------
    int
        Minimum number of boats needed.
    """
    p.sort()
    x = 0
    l, r = 0, len(p) - 1
    while l <= r:
        x += 1
        if p[l] + p[r] <= limit:
            l += 1
        r -= 1
    return x


def main():
    """
    Main function to execute the program.

    It reads the input from stdin, calls the numRescueBoats function and writes the output to a file.
    """
    f = open('user.out', 'w')
    for i1, i2 in zip(stdin, stdin):
        f.write(f'{numRescueBoats(loads(i1), loads(i2))}\n')
    f.flush()
    exit(0)


if __name__ == '__main__':
    main()
