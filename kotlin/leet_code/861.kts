/**
 * Copyright ©2012-2024 JerodG <https://github.com/jerodg/>
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
 * program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 *
 * This class provides a solution for a problem from LeetCode, specifically problem 861.
 * The problem involves manipulating a binary matrix to maximize its score.
 */
class Solution {
    /**
     * This function calculates the maximum score that can be obtained from a binary matrix.
     * The score is calculated by treating each row in the matrix as a binary number and summing them up.
     * The matrix is manipulated by flipping rows and columns to maximize the score.
     *
     * @param grid The binary matrix represented as a 2D array.
     * @return The maximum score that can be obtained from the matrix.
     */
    fun matrixScore(grid: Array<IntArray>): Int {
        // Initialize an array to store the binary numbers represented by each row in the matrix.
        val bits = IntArray(grid.size)
        // Calculate the mask and the most significant bit for bitwise operations.
        val mask = (1 shl grid[0].size) - 1
        val mostSignificantBit = 1 shl (grid[0].size - 1)

        // Convert each row in the matrix to a binary number and store it in the bits array.
        for (y in 0 until grid.size) {
            var number = 0
            val line = grid[y]
            for (x in 0 until line.size) {
                number = number shl 1
                number = number or line[x]
            }
            bits[y] = number
        }

        // Flip the rows in the bits array if their most significant bit is not set.
        for (y in 0 until grid.size) {
            if (bits[y] and mostSignificantBit == 0) bits[y] = bits[y].inv() and mask
        }

        // Flip the columns in the bits array if the number of ones in the column is less than the number of zeros.
        for (x in grid[0].size - 2 downTo 0) {
            val ones = countColumnBits(bits, x)
            if (ones < grid.size - ones) {
                toggleColumn(bits, x)
            }
        }

        // Calculate the score by summing up the binary numbers in the bits array.
        var result = 0
        for (y in 0 until grid.size) {
            result += bits[y]
        }
        return result
    }

    /**
     * This function counts the number of ones in a specific column of the bits array.
     *
     * @param bits The array of binary numbers.
     * @param x The index of the column.
     * @return The number of ones in the column.
     */
    private fun countColumnBits(bits: IntArray, x: Int): Int {
        var count = 0
        val bit = 1 shl x
        for (i in bits.indices) {
            if (bits[i] and bit != 0) count++
        }
        return count
    }

    /**
     * This function flips a specific column in the bits array.
     *
     * @param bits The array of binary numbers.
     * @param x The index of the column.
     */
    private fun toggleColumn(bits: IntArray, x: Int) {
        val bit = 1 shl x
        for (i in bits.indices) {
            bits[i] = bits[i] xor bit
        }
    }
}
