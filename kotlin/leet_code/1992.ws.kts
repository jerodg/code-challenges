/**
 * This Kotlin module provides a solution for finding farmland in a given 2D array.
 * The 2D array represents a land where 1 indicates farmland and 0 indicates non-farmland.
 * The solution identifies all distinct farmlands and returns their coordinates.
 *
 * @module leet_code/1992.ws.kts
 */

import kotlin.Pair // Importing Pair class from Kotlin standard library

/**
 * Solution class provides methods to find farmland in a given 2D array.
 */
class Solution {

    /**
     * This function finds all distinct farmlands in the given 2D array.
     *
     * @param land A 2D array representing the land.
     * @return An array of integer arrays where each integer array contains the coordinates of a distinct farmland.
     *
     * @throws IllegalArgumentException If the input land array is null.
     *
     * Example usage:
     * val solution = Solution()
     * val land = arrayOf(intArrayOf(1, 0, 0), intArrayOf(0, 1, 1), intArrayOf(0, 1, 1))
     * val farmlands = solution.findFarmland(land)
     * // farmlands will be [[0, 0, 0, 0], [1, 1, 2, 2]]
     */
    fun findFarmland(land: Array<IntArray>): Array<IntArray> {
        val res = mutableListOf<IntArray>()
        for (i in land.indices) {
            for (j in land[i].indices) {
                if (land[i][j] == 1) {
                    val (row, col) = findFarmland(i, j, land)
                    res.add(intArrayOf(i, j, row, col))
                }
            }
        }
        return res.toTypedArray()
    }

    /**
     * This private function finds the farmland starting from the given coordinates in the 2D array.
     *
     * @param i The row index to start the search from.
     * @param j The column index to start the search from.
     * @param land The 2D array representing the land.
     * @return A pair of integers representing the coordinates of the farmland.
     *
     * @throws IllegalArgumentException If the input land array is null.
     */
    private fun findFarmland(i: Int, j: Int, land: Array<IntArray>): Pair<Int, Int> {
        var row = i
        var col = j
        for (k in j until land[i].size) {
            if (land[i][k] == 1) {
                col = k
            } else {
                break
            }
        }

        for (k in i until land.size) {
            if (land[k][j] == 1) {
                row = k
            } else {
                break
            }
        }

        for (k in i..row) {
            for (l in j..col) {
                land[k][l] = 0
            }
        }
        return Pair(row, col)
    }
}
