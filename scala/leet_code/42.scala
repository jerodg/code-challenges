/** This module provides a solution to the problem of trapping rain water.
  * Given an array of integers representing an elevation map where the width of each bar is 1,
  * compute how much water it can trap after raining.
  */
object Solution {

  /** Function to calculate the total amount of water that can be trapped between the bars.
    *
    * @param height an Array[Int] representing the heights of the bars.
    * @return an Int representing the total amount of water that can be trapped.
    */
  def trap(height: Array[Int]): Int = {
    // If the height array is empty, return 0
    if (height.isEmpty) 0
    else {
      var left = 0
      var right = height.length - 1
      var leftMax = 0
      var rightMax = 0
      var trappedWater = 0

      // Iterate until the left pointer is less than the right pointer
      while (left < right) {
        // If the height of the bar on the left is less than the height of the bar on the right
        if (height(left) < height(right)) {
          // If the height of the bar on the left is greater than or equal to the maximum height on the left
          if (height(left) >= leftMax) {
            // Update the maximum height on the left
            leftMax = height(left)
          } else {
            // Add the difference between the maximum height on the left and the height of the bar on the left to the trappedWater
            trappedWater += leftMax - height(left)
          }
          // Move the left pointer to the right
          left += 1
        } else {
          // If the height of the bar on the right is greater than or equal to the maximum height on the right
          if (height(right) >= rightMax) {
            // Update the maximum height on the right
            rightMax = height(right)
          } else {
            // Add the difference between the maximum height on the right and the height of the bar on the right to the trappedWater
            trappedWater += rightMax - height(right)
          }
          // Move the right pointer to the left
          right -= 1
        }
      }

      // Return the trappedWater
      trappedWater
    }
  }
}
