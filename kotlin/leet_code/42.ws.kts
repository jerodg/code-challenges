/**
 * Solution class for LeetCode problem 42: Trapping Rain Water.
 */
class Solution {
    /**
     * Function to calculate the total area of trapped rain water.
     * @param height an integer array representing the height of bars.
     * @return totalArea the total area of trapped rain water.
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