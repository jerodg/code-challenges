/** The `Solution` object contains methods to solve the trapping rain water problem.
  */
object Solution {

  /** This method calculates the total amount of water that can be trapped between the bars.
    *
    * @param height
    *   An array of integers where each integer represents the height of a bar.
    * @return
    *   The total amount of water that can be trapped.
    */
  def trap(height: Array[Int]): Int = {
    // If the height array is empty, return 0
    if (height.isEmpty) 0
    else {
      var left         = 0
      var right        = height.length - 1
      var leftMax      = height(left)
      var rightMax     = height(right)
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
