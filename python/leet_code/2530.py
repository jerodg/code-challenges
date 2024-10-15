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
from math import floor
import heapq


class Solution:
    """A class to solve the problem of maximizing the sum of elements after performing a series of operations.

    This class provides a method to maximize the sum of elements in a list by repeatedly replacing the largest
    element with one-third of its value, rounded down, for a specified number of operations.
    """

    def maxKelements(self, nums: List[int], k: int) -> int:
        """Maximize the sum of elements after performing k operations.

        This function takes a list of integers and a number of operations. In each operation, it replaces the
        largest element in the list with one-third of its value, rounded down. The goal is to maximize the sum
        of the elements after performing all operations.

        Args:
            nums (List[int]): A list of integers to be processed.
            k (int): The number of operations to perform.

        Returns:
            int: The maximum sum of the elements after performing k operations.

        Example:
            >>> Solution().maxKelements([10, 20, 7], 2)
            27
        """
        # Convert all elements to negative to use the min-heap as a max-heap
        nums = [-num for num in nums]
        heapq.heapify(nums)  # Transform the list into a heap

        ans = 0  # Initialize the answer to 0

        for i in range(k):
            # Pop the largest element, divide it by 3, floor it, and push it back
            ans -= heapq.heappushpop(nums, floor(nums[0] / 3))

        return ans
