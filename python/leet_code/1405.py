"""Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
"""

import heapq


class Solution:
    """A class to solve the problem of generating the longest diverse string.

    This class provides a method to generate the longest possible string without three consecutive
    characters being the same, given counts of three different characters.
    """

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """Generate the longest diverse string with no three consecutive characters being the same.

        This function takes the counts of three different characters and constructs the longest
        possible string such that no three consecutive characters are the same.

        Args:
            a (int): The count of character 'a'.
            b (int): The count of character 'b'.
            c (int): The count of character 'c'.

        Returns:
            str: The longest diverse string possible.

        Example:
            >>> Solution().longestDiverseString(1, 1, 7)
            'ccaccbcc'
        """
        maxh = []
        # Push the counts and characters into the heap if they are non-zero
        if a:
            heapq.heappush(maxh, (-a, 'a'))
        if b:
            heapq.heappush(maxh, (-b, 'b'))
        if c:
            heapq.heappush(maxh, (-c, 'c'))

        res = ""
        while maxh:
            f1, c1 = heapq.heappop(maxh)
            f1 *= -1  # Convert back to positive

            # Check if the last two characters in the result are the same as the current character
            if len(res) >= 2 and res[-1] == res[-2] == c1:
                if not maxh:
                    return res  # No other characters to use, return the result
                f2, c2 = heapq.heappop(maxh)
                f2 *= -1  # Convert back to positive
                res += c2
                f2 -= 1
                if f2:
                    heapq.heappush(maxh, (-f2, c2))
                heapq.heappush(maxh, (-f1, c1))
                continue

            res += c1
            f1 -= 1
            if f1:
                heapq.heappush(maxh, (-f1, c1))

        return res
