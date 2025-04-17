"""LeetCode 2176 Count Equal and Divisible Pairs in an Array.

This module implements a solution to LeetCode problem 2176, which requires counting
pairs of indices in an array where the values are equal and the product of
indices is divisible by a given number.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""
from collections import defaultdict


class Solution:
    """Solution class for LeetCode problem 2176.

    Uses a mapping-based approach to efficiently find pairs of indices with equal values
    and divisible index products, avoiding the O(n²) complexity of a brute force solution.
    """

    def countPairs(self, nums: list[int], k: int) -> int:
        """Count pairs of indices (i,j) where nums[i] == nums[j] and (i*j) is divisible by k.

        Maintains a mapping of values to their indices, allowing for efficient checking of
        previously encountered values that match the current value. This approach processes
        the array in a single pass.

        Parameters:
            nums (list[int]): The input array of integers
            k (int): The divisibility factor

        Returns:
            int: Count of valid pairs that satisfy both conditions

        Example:
            >>> Solution().countPairs([3,1,2,2,2,1,3], 2)
            4
            >>> Solution().countPairs([1,2,3,4], 1)
            0
        """
        index_map = defaultdict(list)   # Maps each value to a list of its indices
        result = 0

        for i in range(len(nums)):
            # Check current value against all previous occurrences of the same value
            for j in index_map[nums[i]]:
                # If product of indices is divisible by k, increment result
                if (i * j) % k == 0:
                    result += 1

            # Record the current index for this value
            index_map[nums[i]].append(i)

        return result
