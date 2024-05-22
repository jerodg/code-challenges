/// Dart implementation of the LeetCode problem 1614: Remove Element.
///
/// This module contains a class `Solution` with a method `removeElement`.
/// The `removeElement` method takes in two parameters:
/// - `nums`: A list of integers representing the array of numbers.
/// - `val`: An integer representing the value to remove.
///
/// The method returns an integer representing the new length of the array after removing all instances of `val`.
///
/// Error Handling:
/// - This method assumes that the input parameters are well-formed, i.e., `nums` is a list of integers and `val` is an integer.
/// - If the input parameters are not well-formed, the behavior of the method is undefined.
library;

class Solution {
  /// Removes all instances of `val` in the array and returns the new length.
  ///
  /// This method uses two pointers to traverse the array. The first pointer `i` is for the current element and the second pointer `j` is for the next element.
  /// It iterates over each element in the array. If the current element is not equal to `val`, it copies the current element to the position of the first pointer and increments the first pointer.
  /// After the iteration, the first pointer is the new length of the array.
  ///
  /// @param nums The array of numbers.
  /// @param val The value to remove.
  /// @return The new length of the array.
  int removeElement(List<int> nums, int val) {
    int i = 0;
    for (int j = 0; j < nums.length; j++) {
      if (nums[j] != val) {
        nums[i] = nums[j];
        i++;
      }
    }
    return i;
  }
}
