/**
 * This module contains the Solution class which is used to solve the problem of finding
 * the minimum falling path sum in a given grid. The falling path starts from the top row and chooses
 * one element from each row. The next row's choice must be in a column that is different from the
 * previous row's column by at most one.
 *
 * @file leet_code/1289.ws.kts
 */
class Solution {
    /**
     * This function calculates the minimum falling path sum in a given grid.
     *
     * @param grid The input grid. It is a 2D array of integers where we need to find the minimum falling path sum.
     * @return Returns the minimum falling path sum in the input grid.
     *
     * @throws IllegalArgumentException If the input grid is null.
     */
    fun minFallingPathSum(grid: Array<IntArray>): Int {
        // Initialize variables to keep track of the minimum path sum for the current and next row.
        var nextMin1C = -1
        var nextMin2C = -1
        var nextMin1 = -1
        var nextMin2 = -1
        val n = grid.size

        // Calculate the minimum path sum for the last row.
        for (col in 0 until n) {
            if (nextMin1 == -1 || grid[n - 1][col] <= nextMin1) {
                nextMin2 = nextMin1
                nextMin2C = nextMin1C
                nextMin1 = grid[n - 1][col]
                nextMin1C = col
            } else if (nextMin2 == -1 || grid[n - 1][col] <= nextMin2) {
                nextMin2 = grid[n - 1][col]
                nextMin2C = col
            }
        }

        // Calculate the minimum path sum for each row from bottom to top.
        for (row in (n - 2) downTo 0) {
            var min1C = -1
            var min2C = -1
            var min1 = -1
            var min2 = -1

            for (col in 0 until n) {
                var v: Int
                if (col != nextMin1C) {
                    v = grid[row][col] + nextMin1
                } else {
                    v = grid[row][col] + nextMin2
                }

                if (min1 == -1 || v <= min1) {
                    min2 = min1
                    min2C = min1C
                    min1 = v
                    min1C = col
                } else if (min2 == -1 || v <= min2) {
                    min2 = v
                    min2C = col
                }
            }
            nextMin1C = min1C
            nextMin2C = min2C
            nextMin1 = min1
            nextMin2 = min2
        }

        // Return the minimum falling path sum.
        return nextMin1
    }
}
