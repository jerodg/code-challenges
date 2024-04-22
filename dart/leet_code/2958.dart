/// Dart core library for fundamental classes.
import 'dart:math';

/// Dart implementation of a hypothetical problem.
///
/// This module contains a class `Solution` with a method `maxSubarrayLength`.
/// The `maxSubarrayLength` method takes in two parameters:
/// - `nums`: A list of integers representing the array of numbers.
/// - `k`: An integer representing the maximum frequency of any number in the subarray.
///
/// The method returns an integer representing the maximum length of a subarray where the frequency of any number is at most `k`.
/// The subarray can be any contiguous part of the original array.
///
/// Error Handling:
/// - This method assumes that the input parameters are well-formed, i.e., `nums` is a list of integers and `k` is an integer.
/// - If the input parameters are not well-formed, the behavior of the method is undefined.

class Solution {
  /// Calculates the maximum length of a subarray where the frequency of any number is at most `k`.
  ///
  /// This method uses a sliding window approach to find the maximum length of a subarray that satisfies the condition.
  /// It maintains a counter of the frequency of each number in the current subarray.
  /// It expands the window to the right by adding the number at the right to the counter.
  /// If the frequency of the added number is more than `k`, it shrinks the window from the left until the frequency of the added number is at most `k`.
  /// It keeps track of the maximum length of the subarray during the process.
  ///
  /// @param nums The array of numbers.
  /// @param k The maximum frequency of any number in the subarray.
  /// @return The maximum length of a subarray where the frequency of any number is at most `k`.
  int maxSubarrayLength(List<int> nums, int k) {
    int left = 0;
    Map<int, int> counter = {};
    int max_length = 0;
    for (int right = 0; right < nums.length; right++) {
      counter[nums[right]] = (counter[nums[right]] ?? 0) + 1;
      while (counter[nums[right]]! > k) {
        counter[nums[left]] = counter[nums[left]]! - 1;
        if (counter[nums[left]] == 0) {
          counter.remove(nums[left]);
        }
        left++;
      }
      max_length = max(max_length, right - left + 1);
    }
    return max_length;
  }
}
