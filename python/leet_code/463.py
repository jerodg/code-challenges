"""
This module provides a solution for calculating the perimeter of islands in a given grid.

The grid is represented as a 2D list of integers, where 0 represents a water cell and 1 represents a land cell.
The solution identifies all land cells and calculates the perimeter based on the number of water cells around it.

Example Usage:
    python3 leet_code/463.py < input.txt

This module requires Python 3.12 and uses nested loops for calculating the perimeter.
"""

import json
from sys import stdin


def calculate_perimeter(grid: list[list[int]]) -> int:
    """
    Calculate the perimeter of islands in a given grid.

    The function iterates over each cell in the grid. If a cell is a land cell, it initially adds 4 to the perimeter
    (assuming the cell is surrounded by water). If there's a land cell above or to the left of the current cell,
    it subtracts 2 from the perimeter for each such cell.

    Parameters:
    grid (List[List[int]]): A 2D list of integers representing the grid.

    Returns:
    int: The total perimeter of the islands in the grid.

    Raises:
    ValueError: If the grid is empty or not a 2D list.

    Example:
    >>> calculate_perimeter([[1, 0, 1], [0, 1, 0], [1, 1, 1]])
    12
    """
    if not grid or not all(isinstance(row, list) for row in grid):
        raise ValueError('Invalid grid. It must be a 2D list.')

    perimeter = 0

    # Enumerate over each row in the grid
    for i, row in enumerate(grid):
        # Enumerate over each cell in the row
        for j, cell in enumerate(row):
            # If the cell is a land cell
            if cell == 1:
                # Add 4 to the perimeter (assuming it's surrounded by water)
                perimeter += 4

                # If there's a land cell above, subtract 2 from the perimeter
                if 0 < i and grid[i - 1][j] == 1:
                    perimeter -= 2
                # If there's a land cell to the left, subtract 2 from the perimeter
                if 0 < j and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter


with open('user.out', 'w') as Solution:
    # Loop over each grid in the input
    for grid in map(json.loads, stdin):
        # Write the calculated perimeter to the output file
        Solution.write(f'{calculate_perimeter(grid)}\n')

exit()
