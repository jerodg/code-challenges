"""
This module provides a solution for finding farmland in a given land matrix.

The land matrix is represented as a 2D list of integers, where 0 represents a plot of land that is barren,
and 1 represents a plot of land that is fertile. The solution identifies all rectangular areas of fertile land
and returns them as a list of rectangles. Each rectangle is represented as a list of four integers: 
[row of top left corner, column of top left corner, row of bottom right corner, column of bottom right corner].

Example Usage:
    solution = Solution()
    land = [[1,0,1], [0,1,0], [1,1,1]]
    print(solution.findFarmland(land))  # Output: [[0, 0, 0, 0], [0, 2, 0, 2], [1, 1, 2, 2]]

This module requires Python 3.12 and uses list comprehension and nested loops for finding the farmland.
"""


class Solution:
    @staticmethod
    def find_farmland(land: list[list[int]]) -> list[list[int]]:
        """
        Find all rectangular areas of fertile land in the given land matrix.

        The function iterates over each cell in the land matrix. If it encounters a fertile plot (1), 
        it identifies the rectangle of fertile land that this plot is a part of. The rectangle is then 
        added to the result list and all cells in the rectangle are marked as visited.

        Parameters:
        land (List[List[int]]): A 2D list of integers representing the land matrix.

        Returns:
        List[List[int]]: A list of rectangles representing the areas of fertile land. Each rectangle is 
        represented as a list of four integers: [row of top left corner, column of top left corner, 
        row of bottom right corner, column of bottom right corner].

        Raises:
        ValueError: If the land matrix is empty or not a 2D list.

        Example:
        >>> solution = Solution()
        >>> land = [[1,0,1], [0,1,0], [1,1,1]]
        >>> solution.find_farmland(land)
        [[0, 0, 0, 0], [0, 2, 0, 2], [1, 1, 2, 2]]
        """
        if not land or not all(isinstance(row, list) for row in land):
            raise ValueError("Invalid land matrix. It must be a 2D list.")

        m, n, res = len(land), len(land[0]), []
        for i in range(m):
            j = 0
            while j < n:
                if land[i][j]:
                    if land[i][j] == 1:
                        k, l = j + 1, i + 1
                        while k < n and land[i][k] == 1:  # Find the right boundary of the rectangle
                            k += 1
                        k += 1
                        while l < m and land[l][j] == 1:  # Find the bottom boundary of the rectangle
                            land[l][j] = -k
                            l += 1
                        if l < m:
                            land[l][j] = 1 - k
                        res.append([i, j, l - 1, k - 2])  # Add the rectangle to the result list
                        j = k
                    else:
                        j = -land[i][j]
                else:
                    j += 1
        return res
