"""Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

Codewars Kata: Sum of Pairs
"""
def sum_pairs(ints: list[int], s: int) -> list[int] | None:
    """Find the first pair of integers that sum to the target value.

    For multiple valid pairs, returns the pair whose second element has the smallest index.

    Parameters:
        ints (list[int]): List of integers to search through
        s (int): Target sum value

    Returns:
        list[int] | None: A pair [a, b] where a + b = s, or None if no such pair exists

    Example:
        >>> sum_pairs([11, 3, 7, 5], 10)
        [3, 7]
        >>> sum_pairs([4, 3, 2, 3, 4], 6)
        [4, 2]
    """
    seen = set()

    for num in ints:
        # If we've already seen the complement of the current number,
        # we've found a pair with the earliest possible second index
        if (s - num) in seen:
            return [s - num, num]

        # Otherwise, add the current number to our set of seen numbers
        seen.add(num)

    return None