/**
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
 */

/**
 * The Solution class is designed to solve the problem of finding the maximum amount of gold that can be collected
 * in a grid. The grid is represented as a 2D array where each cell contains an integer representing the amount of gold.
 */
class Solution {
    /**
     * This function calculates the maximum amount of gold that can be collected from the grid.
     *
     * @param grid A 2D array of integers where each integer represents the amount of gold in a cell.
     * @return The maximum amount of gold that can be collected.
     */
    fun getMaximumGold(grid: Array<IntArray>): Int {
        var ans = 0

        /**
         * This nested function is used to perform a depth-first search (DFS) on the grid.
         * It starts from a cell and explores as far as possible along each branch before backtracking.
         *
         * @param r The row index of the current cell.
         * @param c The column index of the current cell.
         * @param v The current amount of gold collected.
         */
        fun find(r: Int, c: Int, v: Int) {
            // Check if the current cell is out of bounds or if it contains no gold.
            if (r !in grid.indices || c !in grid[0].indices || grid[r][c] == 0) {
                ans = maxOf(ans, v)
                return
            }
            val a = grid[r][c]
            grid[r][c] = 0 // Mark the current cell as visited by setting its value to 0.
            // Explore the neighboring cells.
            find(r + 1, c, v + a)
            find(r - 1, c, v + a)
            find(r, c + 1, v + a)
            find(r, c - 1, v + a)
            grid[r][c] = a // Backtrack by resetting the value of the current cell.
        }

        // Iterate over each cell in the grid.
        for (r in grid.indices) {
            for (c in grid[0].indices) {
                // If the current cell contains gold, start a DFS from this cell.
                if (grid[r][c] != 0) find(r, c, 0)
            }
        }
        return ans // Return the maximum amount of gold that can be collected.
    }
}
