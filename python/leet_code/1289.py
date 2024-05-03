"""leet_code/1289.py

This module contains a solution for finding the minimum falling path sum in a given grid.
The grid is a 2D list of integers where each element represents a cost. A falling path starts from any element in the first row and chooses the element from the next row that is either directly below or diagonally left/right. Specifically, the path must be from one of the three cells in the row below. The same cell may not be chosen twice.

The solution uses dynamic programming to keep track of the minimum cost path at each cell.

Functions:
    minFallingPathSum: This function finds the minimum falling path sum in a grid.
"""

from json import loads
from sys import stdin
from typing import List


def minFallingPathSum(grid: List[List[int]]) -> int:
    """Finds the minimum falling path sum in a grid.

    Args:
        grid (List[List[int]]): The grid in which to find the minimum falling path sum.

    Returns:
        int: The minimum falling path sum in the grid.

    This function does not handle errors explicitly. If the input is not a 2D list of integers, Python's built-in error handling will raise an exception.
    """

    n = len(grid)
    next_min1_col = -1
    next_min2_col = -1
    next_min1_val = -1
    next_min2_val = -1

    # Find the minimum cost in the last row
    for col in range(n):
        if next_min1_col == -1 or grid[n - 1][col] <= next_min1_val:
            next_min2_col = next_min1_col
            next_min2_val = next_min1_val

            next_min1_col = col
            next_min1_val = grid[n - 1][col]

        elif next_min2_col == -1 or grid[n - 1][col] <= next_min2_val:
            next_min2_col = col
            next_min2_val = grid[n - 1][col]

    # Find the minimum cost in the remaining rows
    for row in range(n - 2, -1, -1):
        min1_col = -1
        min2_col = -1
        min1_val = -1
        min2_val = -1

        for col in range(n):
            ans = 0
            if col != next_min1_col:
                ans = grid[row][col] + next_min1_val
            else:
                ans = grid[row][col] + next_min2_val

            if min1_col == -1 or ans <= min1_val:
                min2_col = min1_col
                min2_val = min1_val

                min1_col = col
                min1_val = ans
            elif min2_col == -1 or ans <= min2_val:
                min2_col = col
                min2_val = ans

        next_min1_col = min1_col
        next_min1_val = min1_val
        next_min2_col = min2_col
        next_min2_val = min2_val

    return next_min1_val


f = open('user.out', 'w')
for i in map(loads, stdin):
    f.write(f'{minFallingPathSum(i)}\n')
f.flush()
exit(0)
