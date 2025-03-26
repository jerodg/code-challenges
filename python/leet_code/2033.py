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

Minimum Operations to Make a Uni-Value Grid
"""
from cmath import inf
from collections import Counter


class Solution:
    """Solution for making a 2D grid uni-value using minimum operations.

    This class implements an algorithm to determine the minimum number of operations
    required to transform a grid into a uni-value grid by adding or subtracting a value x.
    """

    def minOperations(self, grid: list[list[int]], x: int) -> int:
        """Calculate minimum operations to make all grid elements equal.

        The function determines if it's possible to make all elements equal by adding
        or subtracting x, and if so, calculates the minimum number of operations required.

        Parameters:
            grid (List[List[int]]): A 2D integer grid to be transformed.
            x (int): The value that can be added or subtracted in each operation.

        Returns:
            int: The minimum number of operations needed to make the grid uni-value,
                 or -1 if it's impossible.

        Example:
            >>> Solution().minOperations([[2,4],[6,8]], 2)
            4
        """
        # Count occurrences of each value in the grid
        c = Counter(n for arr in grid for n in arr)

        # Check if all elements have the same remainder when divided by x
        # If any element has a different remainder, it's impossible to make the grid uni-value
        for k in c:
            if (grid[0][0] - k) % x:
                return -1

        # Initialize variables for dynamic calculation
        # a: accumulates prefix sums, prv: previous sum, cur: current counter sum
        # mn/mx: min/max values in the grid
        a, prv, cur, mn, mx = [], 0, 0, min(c), max(c)

        # Forward pass: calculate prefix sums for each possible value
        for n in range(mn, mx + 1, x):
            a.append(prv + cur)
            prv, cur = a[-1], cur + c[n]

        # Backward pass: calculate minimum operations
        # ret: stores minimum operations, cur: running sum of values
        # nxt: accumulator for next values
        ret, cur, nxt = inf, 0, 0
        for n in range(mx, mn - 1, -x):
            # For each possible target value, calculate operations needed
            ret = min(ret, a.pop() + cur + nxt)
            cur, nxt = cur + c[n], cur + nxt

        return ret
