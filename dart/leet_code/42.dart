/// Dart implementation of the LeetCode problem 42: Trapping Rain Water.
///
/// This module contains a class `Solution` with a method `trap`.
/// The `trap` method takes in one parameter:
/// - `height`: A list of non-negative integers representing the height of each bar.
///
/// The method returns an integer representing the maximum amount of water that can be trapped.
///
/// Error Handling:
/// - This method assumes that the input parameter is well-formed, i.e., `height` is a list of non-negative integers.
/// - If the input parameter is not well-formed, the behavior of the method is undefined.

import 'dart:core';

class Solution {
  /// Calculates the maximum amount of water that can be trapped.
  ///
  /// This method uses two pointers to traverse the height list from both ends and calculates
  /// the amount of water that can be trapped at each index.
  ///
  /// @param height A list of non-negative integers representing the height of each bar.
  /// @return The maximum amount of water that can be trapped.
  int trap(List<int> height) {
    // If there are no bars, no water can be trapped.
    if (height.isEmpty) return 0;

    // Initialize left and right lists with the height of the first and last bar respectively.
    List<int> left = List.filled(height.length, 0);
    List<int> right = List.filled(height.length, 0);
    left[0] = height[0];
    right[height.length - 1] = height[height.length - 1];

    // Fill the left list with the maximum height of the bar from the start to the current index.
    for (int i = 1; i < height.length; i++) {
      left[i] = left[i - 1] > height[i] ? left[i - 1] : height[i];
    }

    // Fill the right list with the maximum height of the bar from the end to the current index.
    for (int i = height.length - 2; i >= 0; i--) {
      right[i] = right[i + 1] > height[i] ? right[i + 1] : height[i];
    }

    // Calculate the total amount of water that can be trapped.
    int ans = 0;
    for (int i = 0; i < height.length; i++) {
      ans += left[i] < right[i] ? left[i] - height[i] : right[i] - height[i];
    }

    // Return the total amount of water that can be trapped.
    return ans;
  }
}
