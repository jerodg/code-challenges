"""
leet_code/2812.py

This module contains a solution for finding the maximum safeness factor in a grid.
The grid is represented as a 2D list, where 0 represents a safe cell and 1 represents an unsafe cell.
The safeness factor of a cell is the minimum distance to an unsafe cell.
The maximum safeness factor is the maximum of the safeness factors of the cells in the path from the top-left to the bottom-right cell.

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

from collections import deque
from heapq import heappop, heappush


class Solution:
    """
    This class contains a method to solve the problem of finding the maximum safeness factor in a grid.
    """

    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        """
        This method finds the maximum safeness factor in a grid.

        Parameters:
        grid (list[list[int]]): A 2D list representing the grid. 0 represents a safe cell and 1 represents an unsafe cell.

        Returns:
        int: The maximum safeness factor, or -1 if there is no path from the top-left to the bottom-right cell.
        """

        # Get the number of rows and columns in the grid
        row, col = len(grid), len(grid[0])

        # If the start or end cell is unsafe, return 0
        if grid[0][0] == 1 or grid[row - 1][col - 1] == 1:
            return 0

        # Initialize the safeness grid with -1
        safeness = [[-1] * col for _ in range(row)]
        q = deque([])

        # For each cell in the grid, if it is unsafe, set its safeness to 0 and add it to the queue
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    safeness[r][c] = 0
                    q.append((0, r, c))

        # Define the four possible directions to move in the grid
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # While there are cells in the queue, process each cell
        while q:
            dis, r, c = q.popleft()
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                # If the new cell is in the grid and its safeness has not been set yet, set its safeness and add it to the queue
                if 0 <= nr < row and 0 <= nc < col and safeness[nr][nc] == -1:
                    safeness[nr][nc] = dis + 1
                    q.append((dis + 1, nr, nc))

        # Initialize the heap with the end cell and its safeness, and the set of seen cells with the end cell
        heap = [(-safeness[row - 1][col - 1], row - 1, col - 1)]
        seen = {(row - 1, col - 1)}

        # While there are cells in the heap, process each cell
        while heap:
            dis, r, c = heappop(heap)
            # If the current cell is the start cell, return its safeness
            if (r, c) == (0, 0):
                return -dis

            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                # If the new cell is in the grid and it has not been seen yet, add it to the heap and the set of seen cells
                if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in seen:
                    safe = max(dis, -safeness[nr][nc])
                    heappush(heap, (safe, nr, nc))
                    seen.add((nr, nc))

        # If there is no path from the start cell to the end cell, return -1
        return -1
