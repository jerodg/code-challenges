"""
leet_code/3075.py

Copyright ©2012-2024 JerodG <https://github.com/jerodg/>

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
    """
    This class provides a solution for the problem. It has a method called maximumHappinessSum.
    """

    @staticmethod
    def maximumHappinessSum(happiness: list[int], k: int) -> int:
        """
        This method calculates the maximum happiness sum.

        It first sorts the happiness list in descending order. Then it checks if the kth child's
        happiness is greater than or equal to k-1.
        If it is, it returns the sum of the happiness of the first k children minus the sum of the
        first k-1 natural  numbers.
        If it's not, it calculates the sum of the happiness of each child minus their index
        (0-indexed) until the result is non-positive.

        Parameters:
        happiness (list[int]): A list of integers representing the happiness of each child.
        k (int): The number of children to consider.

        Returns:
        int: The maximum happiness sum.
        """

        # Sort the happiness list in descending order
        children = sorted(happiness, reverse=True)

        # Check if the kth child's happiness is greater than or equal to k-1
        if children[k - 1] >= k - 1:
            # Return the sum of the happiness of the first k children minus the sum of the first
            # k-1 natural numbers
            return sum(children[:k]) - ((0 + k - 1) * k // 2)

        res = 0
        # Calculate the sum of the happiness of each child minus their index (0-indexed) until the
        # result is non-positive
        for i, h in enumerate(children[:k]):
            if h - i <= 0:
                break
            res += h - i

        # Return the maximum happiness sum
        return res
