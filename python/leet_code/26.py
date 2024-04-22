#!/usr/bin/env python3.12
# coding=utf-8
"""
Module for removing duplicates from a list in-place.

This module provides a solution for removing duplicates from a list in-place.
The solution is implemented in the `Solution` class, which has a static method
`removeDuplicates`. This method takes a list of integers and modifies it in-place
to remove any duplicate values. The method returns the number of unique elements
in the list.

Example:
    >>> s = Solution()
    >>> nums = [1, 1, 2]
    >>> print(s.removeDuplicates(nums))
    2
    >>> print(nums)
    [1, 2]

This module requires Python 3.12 or later.

Author:
    Jerod Gawne (https://github.com/jerodg)

Date:
    2024.1
"""

from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        """
        Remove duplicates from a list in-place.

        This method takes a list of integers and modifies it in-place to remove
        any duplicate values. The method returns the number of unique elements
        in the list.

        Args:
            nums (List[int]): The list of integers from which to remove duplicates.

        Returns:
            int: The number of unique elements in the list.

        Raises:
            ValueError: If `nums` is not a list.

        Example:
            >>> s = Solution()
            >>> nums = [1, 1, 2]
            >>> print(s.removeDuplicates(nums))
            2
            >>> print(nums)
            [1, 2]

            >>> nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
            >>> print(s.removeDuplicates(nums))
            5
            >>> print(nums[:5])
            [0, 1, 2, 3, 4]
        """
        if not isinstance(nums, list):
            raise ValueError('`nums` must be a list.')

        if not nums:
            return 0

        # Initialize two pointers: i and j
        i = 0

        # Iterate over the array with j
        for j in range(1, len(nums)):
            # If a new unique element is found
            if nums[j] != nums[i]:
                # Increment i
                i += 1
                # Place the unique element at the position indicated by i
                nums[i] = nums[j]

        # Return the number of unique elements
        return i + 1
