"""Copyright ©2010-2025 JerodG <https://github.com/jerodg/>

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
    """Provides solutions for the maximum happiness sum problem.

    Implements algorithmic solutions for calculating the maximum
    happiness achievable when giving gifts to children with various constraints.
    """

    @staticmethod
    def maximumHappinessSum(happiness: list[int], k: int) -> int:
        """Calculates the maximum possible sum of happiness after giving gifts to children.

        The happiness of each child is reduced by their position in the gift-giving order
        (0-indexed). A gift is only given if the resulting happiness is positive.

        Args:
            happiness: A list of integers representing each child's happiness value.
            k: The maximum number of children to give gifts to.

        Returns:
            The maximum possible sum of happiness after giving gifts to at most k children.

        Examples:
            >>> Solution().maximumHappinessSum([1, 2, 3], 2)
            4
            >>> Solution().maximumHappinessSum([10, 5, 8], 3)
            20
        """
        # Sort children by happiness in descending order to prioritize the happiest children
        children = sorted(happiness, reverse=True)

        # Optimization: If the k-th happiest child still has positive happiness
        # after decrementing (k-1) times, we can use a formula to calculate the total
        if children[k - 1] >= k - 1:
            # Sum of first k children minus the sum of decrements (arithmetic sequence)
            return sum(children[:k]) - ((0 + k - 1) * k // 2)

        res = 0

        # Process each child in order of decreasing happiness
        for i, h in enumerate(children[:k]):
            # Skip children who would have zero or negative happiness after decrement
            if h - i <= 0:
                break
            # Add adjusted happiness value to the result
            res += h - i

        return res
