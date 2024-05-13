"""
leet_code/861.py

This module contains a solution for a problem from LeetCode. The problem is about manipulating a binary matrix to maximize its score.

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

import collections


class Solution:
    """
    This class provides a solution for the problem. It contains a method called matrixScore which calculates the maximum score of a binary matrix.
    """

    def matrixScore(self, grid: list[list[int]]) -> int:
        """
        This method calculates the maximum score of a binary matrix. The score of a matrix is calculated by treating its rows as binary numbers and summing them up.

        Parameters:
        grid (list[list[int]]): A 2D list representing the binary matrix.

        Returns:
        int: The maximum score that can be achieved by flipping the binary matrix.

        """
        rows, cols = len(grid), len(grid[0])
        # Flip the rows of the matrix so that the first element of each row is 1
        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols):
                    # Flip the elements of the row
                    if grid[r][c] == 0:
                        grid[r][c] = 1
                    else:
                        grid[r][c] = 0

        # Count the number of zeros in each column
        counts = collections.defaultdict(int)
        for c in range(1, cols):
            for r in range(rows):
                if grid[r][c] == 0:
                    counts[c] += 1

        # Calculate the score of the matrix
        res = rows * (2 ** (cols - 1))
        for c in range(1, cols):
            # Add the maximum possible score for each column to the total score
            res += max(counts[c], rows - counts[c]) * 2 ** (cols - c - 1)

        return res
