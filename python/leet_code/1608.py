"""
Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>

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

"""
Package leet_code

This module contains the Solution class which provides a method to solve the problem of finding a special array.

A special array is an array where there exists a value x such that there are x numbers in the array that are greater than or equal to x.
"""


class Solution:
    """
    The Solution class provides a method to solve the problem of finding a special array.

    A special array is an array where there exists a value x such that there are x numbers in the array that are greater than or equal to x.
    """

    def specialArray(self, nums: list[int]) -> int:
        """
        This method finds and returns the special value in the given list of integers.

        It sorts the list in ascending order and then iterates over the list, counting the number of elements that are greater than or equal to each possible value of x (from 1 to the length of the list). If it finds a value of x where the count is equal to x, it returns that value. If no such value is found, it returns -1.

        Parameters:
        nums (list[int]): The list of integers to search for the special value.

        Returns:
        int: The special value if found, otherwise -1.

        """

        # Sort the list in ascending order
        nums.sort()

        # Get the length of the list
        n = len(nums)

        # Iterate over the possible values of x
        for x in range(1, n + 1):

            # Initialize the count of elements greater than or equal to x
            count = 0

            # Iterate over the elements in the list
            for num in nums:

                # If the current element is greater than or equal to x, increment the count
                if num >= x:
                    count += 1

            # If the count is equal to x, return x as the special value
            if count == x:
                return x

        # If no special value is found, return -1
        return -1
