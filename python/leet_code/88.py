"""
Module for merging two sorted arrays.

This module provides a solution for merging two sorted arrays into one sorted array.
The solution is implemented in the `Solution` class, which has a method `merge`. This method takes two lists of integers
representing the sorted arrays and their respective lengths, and modifies the first array in-place to include the elements of the second array.

Example:
    >>> s = Solution()
    >>> nums1 = [1, 2, 3, 0, 0, 0]
    >>> m = 3
    >>> nums2 = [2, 5, 6]
    >>> n = 3
    >>> s.merge(nums1, m, nums2, n)
    >>> print(nums1)
    [1, 2, 2, 3, 5, 6]

This module requires Python 3.12 or later.

Author:
    Jerod Gawne (https://github.com/jerodg)

Date:
    2024.1
"""

from typing import List


class Solution:
    """
    This class provides a solution to the problem of merging two sorted arrays into one sorted array.
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        This function merges two sorted arrays into one sorted array.

        Args:
            nums1 (List[int]): The first sorted array.
            m (int): The number of elements in the first array.
            nums2 (List[int]): The second sorted array.
            n (int): The number of elements in the second array.

        Returns:
            None: The function modifies the first array in-place to include the elements of the second array.

        Raises:
            ValueError: If `nums1` and `nums2` are not lists or `m` and `n` are not integers.

        Example:
            >>> s = Solution()
            >>> nums1 = [1, 2, 3, 0, 0, 0]
            >>> m = 3
            >>> nums2 = [2, 5, 6]
            >>> n = 3
            >>> s.merge(nums1, m, nums2, n)
            >>> print(nums1)
            [1, 2, 2, 3, 5, 6]

            >>> nums1 = [1]
            >>> m = 1
            >>> nums2 = []
            >>> n = 0
            >>> s.merge(nums1, m, nums2, n)
            >>> print(nums1)
            [1]

            >>> nums1 = [0]
            >>> m = 0
            >>> nums2 = [1]
            >>> n = 1
            >>> s.merge(nums1, m, nums2, n)
            >>> print(nums1)
            [1]
        """
        if (
            not isinstance(nums1, list)
            or not isinstance(nums2, list)
            or not isinstance(m, int)
            or not isinstance(n, int)
        ):
            raise ValueError('`nums1` and `nums2` must be lists and `m` and `n` must be integers.')

        # Replace the elements in nums1 from index m with the elements in nums2
        nums1[m:] = nums2

        # Sort the array in-place
        nums1.sort()
