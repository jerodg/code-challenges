/**
 * This module provides a solution for the LeetCode problem #200, "Number of Islands".
 * It uses depth-first search (DFS) to count the number of islands in a 2D grid.
 *
 * @module leet_code/200.ws.kts
 */

import kotlin.Array // Array is a built-in Kotlin class, no need to import

/**
 * Solution class for the "Number of Islands" problem.
 */
class Solution {
    // Directions for DFS to move in the grid
    private val directions = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1))

    /**
     * Counts the number of islands in a 2D grid.
     *
     * @param grid The 2D grid represented as an array of character arrays.
     * @return The number of islands in the grid.
     */
    fun numIslands(grid: Array<CharArray>): Int {
        var result = 0
        for (x in grid.indices)
            for (y in grid[x].indices)
                if (grid[x][y] == '1') {
                    result++
                    dfs(grid, x, y)
                }
        return result
    }

    /**
     * Performs a depth-first search (DFS) from a given cell in the grid.
     *
     * @param grid The 2D grid represented as an array of character arrays.
     * @param x The x-coordinate of the starting cell.
     * @param y The y-coordinate of the starting cell.
     */
    fun dfs(grid: Array<CharArray>, x: Int, y: Int) {
        if (!isCoordsValid(grid, x, y) || grid[x][y] == '0')
            return

        grid[x][y] = '0'
        for (dir in directions) {
            dfs(grid, x + dir[0], y + dir[1])
        }
    }

    /**
     * Checks if a given coordinate is valid in the grid.
     *
     * @param grid The 2D grid represented as an array of character arrays.
     * @param x The x-coordinate to check.
     * @param y The y-coordinate to check.
     * @return True if the coordinate is valid, false otherwise.
     */
    fun isCoordsValid(grid: Array<CharArray>, x: Int, y: Int) =
        x >= 0 && y >= 0 && x < grid.size && y < grid[0].size
}

/**
 * Example usage:
 * val solution = Solution()
 * val grid = arrayOf(
 *     charArrayOf('1','1','1','1','0'),
 *     charArrayOf('1','1','0','1','0'),
 *     charArrayOf('1','1','0','0','0'),
 *     charArrayOf('0','0','0','0','0')
 * )
 * val result = solution.numIslands(grid)
 * println(result) // Outputs: 1
 */
