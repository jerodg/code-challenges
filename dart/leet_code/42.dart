// Importing Dart's core library.
import 'dart:core';

/// The `Solution` class provides a method to solve the trapping rain water problem.
class Solution {
  /// This method calculates the maximum amount of water that can be trapped.
  ///
  /// It uses two pointers to traverse the height list from both ends and calculates
  /// the amount of water that can be trapped at each index.
  ///
  /// @param height A list of non-negative integers representing the height of each bar.
  /// @return The maximum amount of water that can be trapped.
  int trap(List<int> height) {
    int n = height.length;
    // If there are no bars, no water can be trapped.
    if (n == 0) return 0;

    // Initialize left and right lists with the height of the first and last bar respectively.
    List<int> left = List.filled(n, 0);
    List<int> right = List.filled(n, 0);
    left[0] = height[0];
    right[n - 1] = height[n - 1];

    // Fill the left list with the maximum height of the bar from the start to the current index.
    for (int i = 1; i < n; i++) {
      left[i] = left[i - 1] > height[i] ? left[i - 1] : height[i];
    }

    // Fill the right list with the maximum height of the bar from the end to the current index.
    for (int i = n - 2; i >= 0; i--) {
      right[i] = right[i + 1] > height[i] ? right[i + 1] : height[i];
    }

    // Calculate the total amount of water that can be trapped.
    int ans = 0;
    for (int i = 0; i < n; i++) {
      ans += left[i] < right[i] ? left[i] - height[i] : right[i] - height[i];
    }

    // Return the total amount of water that can be trapped.
    return ans;
  }
}
