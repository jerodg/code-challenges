/** This object represents a solution for finding the maximum absolute value in an array of integers. The maximum
  * absolute value is defined as the maximum value of the absolute values of the integers in the array. If there are
  * both positive and negative values of the same absolute value in the array, the maximum absolute value is considered
  * as the positive value.
  */
object Solution {

  /** Finds the maximum absolute value in an array of integers.
    *
    * This method first sorts the array and removes duplicate values. It then groups the values by their absolute values
    * and filters out the groups that contain both positive and negative values of the same absolute value. Finally, it
    * finds the maximum value among the remaining values.
    *
    * @param nums
    *   The input array of integers.
    * @return
    *   The maximum absolute value in the array. It returns an integer.
    */
  def findMaxK(nums: Array[Int]): Int = {
    // Concatenate -1 to the array to ensure that the `max` method does not throw an exception when the array is empty
    // Sort the array and remove duplicate values
    // Group the values by their absolute values and filter out the groups that contain both positive and negative values of the same absolute value
    // Find the maximum value among the remaining values
    (Seq(-1) ++
      nums.sorted.distinct
        .groupBy { _.abs }
        .values
        .filter { _.size == 2 }
        .flatten).max
  }
}
