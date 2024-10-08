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


class Solution:
    """
    A class used to solve the problem of finding the minimum number of swaps to balance a string of brackets.
    """

    def minSwaps(self, s: str) -> int:
        """
        Calculate the minimum number of swaps to balance a string of brackets.

        This function counts the number of unmatched opening brackets '[' and determines the minimum number of swaps
        needed to balance the string. A swap can balance two unmatched brackets.

        Args:
            s (str): The input string containing only '[' and ']' characters.

        Returns:
            int: The minimum number of swaps required to balance the string.
        """
        unmatched = 0  # Tracks the number of unmatched opening brackets

        for c in s:
            if c == '[':
                unmatched += 1  # Increment for an opening bracket
            elif unmatched > 0:
                unmatched -= 1  # Decrement for a closing bracket if there's an unmatched opening bracket

        # Each swap can fix two unmatched brackets, so we divide by 2 and round up
        return (unmatched + 1) // 2
