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
    """A class to solve the problem of finding the minimum length of a string after removing specific pairs.

    The pairs to be removed are:
    - 'AB'
    - 'CD'
    """

    def minLength(self, s: str) -> int:
        """Calculates the minimum length of the string after removing specific pairs.

        Args:
            s: The input string consisting of characters.

        Returns:
            The length of the string after removing all possible 'AB' and 'CD' pairs.

        The function uses a stack to keep track of characters. When a character forms a pair with the
        top of the stack, the pair is removed. Otherwise, the character is added to the stack.
        """
        s1 = []  # Stack to keep track of characters
        for p in s:
            # Check if the current character forms a pair with the top of the stack
            if s1 and ((s1[-1] == 'A' and p == 'B') or (s1[-1] == 'C' and p == 'D')):
                s1.pop()  # Remove the top of the stack if a pair is formed
            else:
                s1.append(p)  # Add the current character to the stack if no pair is formed

        return len(s1)  # The length of the stack is the minimum length of the string
