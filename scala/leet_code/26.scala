/**
 * This is the Solution object. It contains a method to remove duplicates from a sorted array in-place.
 * The method returns the new length of the array after duplicates have been removed.
 *
 * @example
 * val nums = Array(1,1,2)
 * val result = Solution.removeDuplicates(nums)
 * // result: 2
 * // nums: Array(1,2)
 *
 * @note The method modifies the input array by moving the non-duplicate elements to the front of the array.
 */
object Solution {
  /**
   * Removes duplicates from a sorted array in-place.
   *
   * @param nums A sorted array of integers.
   * @return The new length of the array after duplicates have been removed.
   * @throws IllegalArgumentException if the input array is not sorted.
   */
  def removeDuplicates(nums: Array[Int]): Int = {
    // Check if the input array is sorted
    if (nums.length > 1 && nums.zip(nums.tail).exists { case (a, b) => a > b }) {
      throw new IllegalArgumentException("Input array must be sorted")
    }

    // Check if the input array is empty
    if (nums.isEmpty) return 0

    var i = 0
    // Iterate over the array
    for (j <- 1 until nums.length) {
      // If the current element is not equal to the previous element
      if (nums(j) != nums(i)) {
        // Move the non-duplicate element to the front of the array
        i += 1
        nums(i) = nums(j)
      }
    }
    // Return the new length of the array
    i + 1
  }
}
