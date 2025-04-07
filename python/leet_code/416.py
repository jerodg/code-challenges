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
    """Provides solutions for leetcode problems related to array partitioning."""

    def canPartition(self, nums: list[int]) -> bool:
        """Determine if an array can be partitioned into two equal-sum subsets.

        Uses a bit manipulation approach to solve the subset sum problem. The solution
        represents all possible sums as bits in an integer, where each bit position
        corresponds to a specific sum value.

        Parameters:
            nums: A list of positive integers to be partitioned.

        Returns:
            True if the array can be divided into two subsets with equal sums,
            False otherwise.

        Example:
            >>> Solution().canPartition([1, 5, 11, 5])
            True
            >>> Solution().canPartition([1, 2, 3, 5])
            False
        """
        # If the total sum is odd, equal partition is impossible
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        # Initialize a bit mask with only the 0 sum possibility (2^0 = 1)
        dp = 1 << 0

        # For each number, update the bit mask to include all new possible sums
        # by shifting the current mask left by the number's value and OR-ing with
        # the existing mask
        for num in nums:
            dp |= dp << num

        # Check if the target sum is achievable by testing the corresponding bit
        return (dp & (1 << target)) != 0
