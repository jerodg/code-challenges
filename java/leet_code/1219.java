/**
 * This class provides a solution for finding the maximum amount of gold that can be collected in a grid.
 * The grid is a 2D array where each cell represents a piece of gold. The goal is to find the path that collects the most gold.
 * The path can start and end at any cell in the grid, and can move up, down, left, or right from the current cell.
 * Each cell can only be visited once in a path.
 * <p>
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 * <p>
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 * <p>
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 * <p>
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <<a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>>.
 */
class Solution {
    /**
     * The maximum amount of gold collected so far.
     */
    public int max = 0;

    /**
     * Recursive method to find all possible paths and update the maximum gold collected.
     *
     * @param grid The 2D grid of gold pieces.
     * @param r    The current row in the grid.
     * @param c    The current column in the grid.
     * @param gold The amount of gold collected so far.
     */
    private void ways(final int[][] grid, final int r, final int c, final int gold) {
        // Update max if current gold is more
        if (gold > this.max) {
            this.max = gold;
        }
        // Return if current cell is empty
        if (grid[r][c] == 0) {
            return;
        }
        // Collect gold from current cell and mark it as empty
        final int a = grid[r][c];
        grid[r][c] = 0;
        // Explore all possible directions
        if (r - 1 >= 0) {
            this.ways(grid, r - 1, c, gold + a);
        }
        if (r + 1 <= grid.length - 1) {
            this.ways(grid, r + 1, c, gold + a);
        }
        if (c + 1 <= grid[0].length - 1) {
            this.ways(grid, r, c + 1, gold + a);
        }
        if (c - 1 >= 0) {
            this.ways(grid, r, c - 1, gold + a);
        }
        // Restore the gold in the current cell after exploring all paths
        grid[r][c] = a;
    }

    /**
     * Method to check if the grid contains any zero cells.
     * If there are no zero cells, it returns the total amount of gold in the grid.
     * Otherwise, it returns -1.
     *
     * @param grid The 2D grid of gold pieces.
     *
     * @return The total amount of gold if there are no zero cells, otherwise -1.
     */
    private static int gridWithNoZeros(final int[][] grid) {
        int count = 0;
        for (final int[] ints : grid) {
            for (int j = 0; j < grid[0].length; j++) {
                if (ints[j] == 0) {
                    return -1;
                } else count += ints[j];
            }
        }
        return count;
    }

    /**
     * Method to find the maximum amount of gold that can be collected in the grid.
     *
     * @param grid The 2D grid of gold pieces.
     *
     * @return The maximum amount of gold that can be collected.
     */
    public final int getMaximumGold(final int[][] grid) {
        // Check if the grid contains any zero cells
        final int count = Solution.gridWithNoZeros(grid);
        // If there are no zero cells, return the total amount of gold
        if (count != -1) return count;
        // Otherwise, find the maximum gold that can be collected
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                this.ways(grid, i, j, 0);
            }
        }
        return this.max;
    }
}
