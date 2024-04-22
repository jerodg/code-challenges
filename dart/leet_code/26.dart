/// Dart implementation of the LeetCode problem 26: Remove Duplicates from Sorted Array.
///
/// This module contains a class `Solution` with a method `removeDuplicates`.
/// The `removeDuplicates` method takes in one parameter:
/// - `nums`: A list of integers sorted in non-decreasing order.
///
/// The method returns an integer representing the number of unique elements in the array.
///
/// Error Handling:
/// - This method assumes that the input parameter is well-formed, i.e., `nums` is a list of integers sorted in non-decreasing order.
/// - If the input parameter is not well-formed, the behavior of the method is undefined.

import 'dart:core';

class Solution {
  /// Removes duplicates from a sorted array and returns the number of unique elements.
  ///
  /// This method uses two pointers to traverse the array. The first pointer `i` represents the position to place the next unique element.
  /// The second pointer `j` scans through the array to find the next unique element.
  ///
  /// @param nums The sorted array.
  /// @return The number of unique elements in the array.
  int removeDuplicates(List<int> nums) {
    // If the array is empty, return 0.
    if (nums.isEmpty) return 0;

    // Initialize the first pointer at the first element.
    int i = 0;

    // Start the second pointer from the second element and scan through the array.
    for (int j = 1; j < nums.length; j++) {
      // If the current element is different from the element at the first pointer, it is a unique element.
      if (nums[j] != nums[i]) {
        // Move the first pointer to the next position.
        i++;

        // Place the unique element at the position of the first pointer.
        nums[i] = nums[j];
      }
    }

    // The number of unique elements is the position of the first pointer plus one.
    return i + 1;
  }
}
