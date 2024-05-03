"""leet_code/2441.py

This module contains a solution for finding the maximum value of 'k' in a given list of integers.
The value of 'k' is defined as the maximum positive integer in the list that also has its negative counterpart in the list.

Classes:
    Solution: This class contains a method to find the maximum value of 'k' in a list.
"""

from typing import List


class Solution:
    """A class used to find the maximum value of 'k' in a list.

    Methods:
        findMaxK: Finds the maximum value of 'k' in a list.
    """

    def findMaxK(self, nums: List[int]) -> int:
        """Finds the maximum value of 'k' in a list.

        Args:
            nums (List[int]): The list of integers in which to find the maximum value of 'k'.

        Returns:
            int: The maximum value of 'k' in the list. If no such value exists, returns -1.

        This function does not handle errors explicitly. If the input is not a list of integers, Python's built-in error handling will raise an exception.
        """
        # Initialize 'k' to -1
        k = -1

        # Convert the list to a set for faster lookup
        nums_set = set(nums)

        # Iterate over the list
        for n in nums:
            # If 'n' is positive and greater than 'k', and its negative counterpart is in the list, update 'k'
            if n > 0:
                if n > k and -n in nums_set:
                    k = n

        # Return the maximum value of 'k'
        return k
