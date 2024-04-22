/// Dart implementation of the LeetCode problem 88: Merge Sorted Array.
///
/// This module contains a class `Solution` with a method `merge`.
/// The `merge` method takes in four parameters:
/// - `nums1`: A list of integers representing the first sorted array.
/// - `m`: An integer representing the number of initial elements in `nums1`.
/// - `nums2`: A list of integers representing the second sorted array.
/// - `n`: An integer representing the number of elements in `nums2`.
///
/// The method does not return anything. It modifies `nums1` in-place such that it contains the elements of both `nums1` and `nums2` in sorted order.
///
/// Error Handling:
/// - This method assumes that the input parameters are well-formed, i.e., `nums1` and `nums2` are lists of integers, and `m` and `n` are integers.
/// - If the input parameters are not well-formed, the behavior of the method is undefined.

class Solution {
  /// Merges two sorted arrays in-place.
  ///
  /// This method uses three pointers to traverse `nums1` and `nums2` from the end and places the larger element at the end of `nums1`.
  ///
  /// @param nums1 The first sorted array.
  /// @param m The number of initial elements in `nums1`.
  /// @param nums2 The second sorted array.
  /// @param n The number of elements in `nums2`.
  void merge(List<int> nums1, int m, List<int> nums2, int n) {
    // Initialize the pointers at the end of `nums1`, `nums2`, and the merged array.
    int i = m - 1;
    int j = n - 1;
    int k = m + n - 1;

    // While there are elements in both `nums1` and `nums2`, place the larger element at the end of the merged array.
    while (i >= 0 && j >= 0) {
      if (nums1[i] > nums2[j]) {
        nums1[k--] = nums1[i--];
      } else {
        nums1[k--] = nums2[j--];
      }
    }

    // If there are remaining elements in `nums2`, place them at the beginning of the merged array.
    while (j >= 0) {
      nums1[k--] = nums2[j--];
    }
  }
}
