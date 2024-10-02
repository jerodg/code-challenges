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
    """Provides a method to transform an array into its rank array.

    The rank array is an array where each element is replaced by its rank in the sorted array.
    """

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """Transforms the input array into its rank array.

        The rank of an element is its position in the sorted unique array, starting from 1.

        Args:
            arr: A list of integers to be transformed.

        Returns:
            A list of integers where each element is replaced by its rank.

        Example:
            >>> Solution().arrayRankTransform([40, 10, 20, 30])
            [4, 1, 2, 3]
        """
        # Remove duplicates and sort the array to determine the rank of each element.
        b = sorted(set(arr))

        # Create a dictionary to map each element to its rank.
        c = {ele: rank + 1 for rank, ele in enumerate(b)}

        # Replace each element in the original array with its rank.
        ranked_arr = [c[ele] for ele in arr]

        return ranked_arr
