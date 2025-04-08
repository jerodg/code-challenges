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
"""


class Solution:
    """Solution for LeetCode problem 3396: Minimum Number of Operations to Make Elements in Array Distinct.

    This class implements an algorithm to find the minimum number of operations needed to make
    all elements in an array distinct, where each operation removes 3 elements from the beginning.

    Attributes:
        None
    """

    def minimumOperations(self, nums: list[int]) -> int:
        """Determine the minimum operations needed to make array elements distinct.

        The function processes the array from right to left, keeping track of seen elements.
        When a duplicate is found, it calculates how many operations are needed to remove
        that element and all elements to its left.

        Parameters:
            nums (list[int]): The input array of integers.

        Returns:
            int: The minimum number of operations required. Returns 0 if elements are already distinct.

        Example:
            >>> Solution().minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7])
            2
            >>> Solution().minimumOperations([4, 5, 6, 4, 4])
            2
            >>> Solution().minimumOperations([6, 7, 8, 9])
            0
        """
        seen = set()
        # Process the array from right to left to maintain elements that should be kept
        for i in range(len(nums) - 1, -1, -1):
            # If a duplicate is found, calculate operations needed to remove it and all previous elements
            if nums[i] in seen:
                # Integer division by 3 gives the number of full operations required
                # Adding 1 handles any remaining elements (1 or 2) that need removal
                return i // 3 + 1

            seen.add(nums[i])

        # Return 0 if all elements are already distinct
        return 0
