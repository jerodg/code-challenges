"""Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>.

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see SSPL.
"""


class Solution:
    """A class to solve the problem of adding spaces at specified positions in a string."""

    def addSpaces(self, s: str, spaces: list[int]) -> str:
        """
        Inserts spaces into the string `s` at the positions specified in the list `spaces`.

        Args:
            s (str): The input string where spaces need to be added.
            spaces (List[int]): A list of indices where spaces should be inserted.

        Returns:
            str: The modified string with spaces inserted at the specified positions.
        """
        index, result = 0, []

        for space in spaces:
            # Append the substring from the current index to the space index
            result.append(s[index: space])
            # Update the index to the current space position
            index = space

        # Append the remaining part of the string after the last space
        result.append(s[index:])

        # Join all parts with a space and return the final string
        return ' '.join(result)