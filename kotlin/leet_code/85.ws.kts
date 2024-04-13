// Importing required libraries
import kotlin.math.max
import kotlin.math.min

/**
 * This class provides a solution for finding the maximal rectangle in a binary matrix.
 * The maximal rectangle is the largest rectangle that can be formed only from 1s.
 * The solution uses dynamic programming to keep track of the maximal rectangle at each point.
 */
class Solution {
    /**
     * Function to find the maximal rectangle in a binary matrix.
     * @param matrix: A 2D character array representing the binary matrix.
     * @return The area of the maximal rectangle.
     */
    fun maximalRectangle(matrix: Array<CharArray>): Int {
        // If the matrix is empty, return 0
        if (matrix.isEmpty())
            return 0

        // Get the dimensions of the matrix
        val m: Int = matrix.size
        val n: Int = matrix[0].size

        // Initialize arrays to keep track of the height, left, and right boundaries of the maximal rectangle
        val height = IntArray(n) {0}
        val left = IntArray(n) {0}
        val right = IntArray(n) {n}

        // Initialize the maximal area to 0
        var maxArea = 0

        // Iterate over the rows of the matrix
        for (i in 0 until m) {
            var curLeft = 0
            var curRight = n

            // Update the height and left arrays
            for (j in 0 until n) {
                if (matrix[i][j] == '1')
                    height[j] += 1
                else height[j] = 0

                if (matrix[i][j] == '1')
                    left[j] = max(left[j], curLeft)
                else {
                    left[j] = 0
                    curLeft = j+1
                }
            }

            // Update the right array
            for (j in n-1 downTo 0) {
                if (matrix[i][j] == '1')
                    right[j] = min(right[j], curRight)
                else {
                    right[j] = n
                    curRight = j
                }
            }

            // Update the maximal area
            for (j in 0 until n) {
                maxArea = max(maxArea, height[j] * (right[j] - left[j]))
            }
        }

        // Return the maximal area
        return maxArea
    }
}