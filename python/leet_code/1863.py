"""
Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>

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

"""
Package leet_code

This module contains the Solution class which is used to solve the problem of finding the sum of all possible XOR of subsets of a given list of numbers.

The Solution class has a constructor and a method named subsetXORSum. The subsetXORSum method takes a list of integers as input and returns an integer which is the sum of all possible XOR of subsets of the input list.
"""


class Solution:
    """
    The Solution class is used to solve the problem of finding the sum of all possible XOR of subsets of a given list of numbers.

    This class has a method named subsetXORSum.
    """

    def subsetXORSum(self, nums: list[int]) -> int:
        """
        The subsetXORSum method takes a list of integers as input and returns an integer which is the sum of all possible XOR of subsets of the input list.

        Parameters:
            nums (list[int]): the input list of integers.

        Returns:
            int: the sum of all possible XOR of subsets of the input list.

        This method uses a bitwise OR operation to find the XOR of all numbers in the list. It then shifts the result to the left by (n - 1) places, where n is the length of the list. This is equivalent to multiplying the result by 2^(n - 1), which gives the sum of all possible XOR of subsets of the list.
        """

        # Length of the input list
        n = len(nums)

        # Initialize the result to 0
        ans = 0

        # Use a bitwise OR operation to find the XOR of all numbers in the list
        for num in nums:
            ans |= num

        # Shift the result to the left by (n - 1) places, which is equivalent to multiplying the result by 2^(n - 1)
        return ans << (n - 1)
