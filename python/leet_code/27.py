#!/usr/bin/env python3.12
# coding=utf-8
"""
Module for removing a specific element from a list in-place.

This module provides a solution for removing a specific element from a list in-place.
The solution is implemented in the `Solution` class, which has a method
`removeElement`. This method takes a list of integers and a value to be removed,
and modifies the list in-place to remove all instances of the value. The method
returns the number of elements remaining in the list after removal.

Example:
    >>> s = Solution()
    >>> nums = [3, 2, 2, 3]
    >>> val = 3
    >>> print(s.removeElement(nums, val))
    2
    >>> print(nums[:2])
    [2, 2]

This module requires Python 3.12 or later.

Author:
    Jerod Gawne (https://github.com/jerodg)

Date:
    2024.1
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove a specific element from a list in-place.

        This method takes a list of integers and a value to be removed, and modifies
        the list in-place to remove all instances of the value. The method returns
        the number of elements remaining in the list after removal.

        Args:
            nums (List[int]): The list of integers from which to remove the value.
            val (int): The value to be removed from the list.

        Returns:
            int: The number of elements remaining in the list after removal.

        Raises:
            ValueError: If `nums` is not a list or `val` is not an integer.

        Example:
            >>> s = Solution()
            >>> nums = [3, 2, 2, 3]
            >>> val = 3
            >>> print(s.removeElement(nums, val))
            2
            >>> print(nums[:2])
            [2, 2]

            >>> nums = [0, 1, 2, 2, 3, 0, 4, 2]
            >>> val = 2
            >>> print(s.removeElement(nums, val))
            5
            >>> print(nums[:5])
            [0, 1, 3, 0, 4]
        """
        if not isinstance(nums, list) or not isinstance(val, int):
            raise ValueError('`nums` must be a list and `val` must be an integer.')

        i = 0
        for j in range(len(nums)):
            # If the current element is not the value to be removed
            if nums[j] != val:
                # Place the current element at the position indicated by i
                nums[i] = nums[j]
                # Increment i
                i += 1

        # Return the number of elements remaining in the list after removal
        return i
