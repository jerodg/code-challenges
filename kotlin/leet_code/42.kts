/**
 * This Kotlin module provides a solution for the LeetCode problem 42: Trapping Rain Water.
 * The solution calculates the total area of trapped rain water given the heights of bars.
 *
 * @module leet_code/42.ws.kts
 */

/**
 * Solution class provides methods to calculate the total area of trapped rain water.
 */
class Solution {

    /**
     * This function calculates the total area of trapped rain water given the heights of bars.
     *
     * @param height An integer array representing the height of bars.
     * @return The total area of trapped rain water.
     *
     * @throws IllegalArgumentException If the input array is null.
     *
     * Example usage:
     * val solution = Solution()
     * val height = intArrayOf(0,1,0,2,1,0,1,3,2,1,2,1)
     * val totalArea = solution.trap(height)
     * // totalArea will be 6
     */
    fun trap(height: IntArray): Int {
        // Initialize total area of trapped rain water
        var totalArea = 0

        // Initialize left and right heights
        var leftHeight = 0
        var rightHeight = 0

        // Initialize left index
        var leftIndex = 0

        // Iterate from left to right
        for (i in 0 until height.size) {
            if (height[i] > leftHeight) {
                // Update left height and index if current height is greater
                leftHeight = height[i]
                leftIndex = i
            } else if (height[i] < leftHeight) {
                // Add the difference between left height and current height to total area
                totalArea += leftHeight - height[i]
            }
        }

        // Iterate from right to left index
        for (i in height.size - 1 downTo leftIndex) {
            if (height[i] > rightHeight) {
                // Update total area and right height if current height is greater
                totalArea -= leftHeight - height[i]
                rightHeight = height[i]
            } else if (height[i] <= rightHeight) {
                // Subtract the difference between left height and right height from total area
                totalArea -= leftHeight - rightHeight
            }
        }

        // Return the total area of trapped rain water
        return totalArea
    }
}
