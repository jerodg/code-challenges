/** This module provides a solution to the problem of merging two sorted integer arrays into one sorted array. The first
  * array has a size that is large enough to hold the elements of the second array. The function `merge` is the main
  * function in this module.
  */
object Solution {

  /** Function to merge two sorted integer arrays into one sorted array. The first array has a size that is large enough
    * to hold the elements of the second array.
    *
    * @param nums1
    *   an Array[Int] representing the first sorted array. It has a size that is large enough to hold the elements of
    *   nums2.
    * @param m
    *   an Int representing the number of elements initially in nums1.
    * @param nums2
    *   an Array[Int] representing the second sorted array.
    * @param n
    *   an Int representing the number of elements in nums2.
    * @return
    *   Unit. The function modifies nums1 in-place to hold the merged array.
    */
  def merge(nums1: Array[Int], m: Int, nums2: Array[Int], n: Int): Unit = {
    // Initialize three pointers to keep track of the current index in nums1, nums2, and the merged array, respectively
    var i = m - 1
    var j = n - 1
    var k = m + n - 1

    // While there are elements in both nums1 and nums2
    while (i >= 0 && j >= 0) {
      // If the current element in nums1 is greater than the current element in nums2
      if (nums1(i) > nums2(j)) {
        // Place the current element in nums1 at the current index in the merged array
        nums1(k) = nums1(i)
        // Move to the previous element in nums1
        i -= 1
      } else {
        // Place the current element in nums2 at the current index in the merged array
        nums1(k) = nums2(j)
        // Move to the previous element in nums2
        j -= 1
      }
      // Move to the previous index in the merged array
      k -= 1
    }

    // If there are remaining elements in nums2
    while (j >= 0) {
      // Place the remaining elements in nums2 at the corresponding indices in the merged array
      nums1(k) = nums2(j)
      // Move to the previous element in nums2 and the previous index in the merged array
      j -= 1
      k -= 1
    }
  }
}
