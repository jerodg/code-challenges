/**
 * This is the Solution object. It contains a method to remove all instances of a specific value in-place from an array.
 * The method returns the new length of the array after the specified value has been removed.
 *
 * @example
 * val nums = Array(3,2,2,3)
 * val result = Solution.removeElement(nums, 3)
 * // result: 2
 * // nums: Array(2,2)
 *
 * @note The method modifies the input array by moving the non-specified elements to the front of the array.
 */
object Solution {
  /**
   * Removes all instances of a specific value in-place from an array.
   *
   * @param nums An array of integers.
   * @param `val` The value to be removed.
   * @return The new length of the array after the specified value has been removed.
   */
  def removeElement(nums: Array[Int], `val`: Int): Int = {
    var i = 0
    // Iterate over the array
    for (j <- 0 until nums.length) {
      // If the current element is not equal to the specified value
      if (nums(j) != `val`) {
        // Move the non-specified element to the front of the array
        nums(i) = nums(j)
        i += 1
      }
    }
    // Return the new length of the array
    i
  }
}
