/// Module: leet_code/2441.dart
///
/// This module contains a solution for a problem from LeetCode.
/// The problem is about finding the maximum number `k` in a list of integers,
/// where `k` and `-k` both exist in the list. If no such number exists, the
/// function returns `-1`.
///
/// Class: Solution
///
/// This class encapsulates the solution for the problem. It has a single
/// method `findMaxK`.

class Solution {
  /// Method: findMaxK
  ///
  /// This method takes a list of integers and finds the maximum number `k` such
  /// that both `k` and `-k` exist in the list.
  ///
  /// Parameters:
  ///
  /// `nums` (List<int>): A list of integers. It is expected to contain both
  /// positive and negative numbers.
  ///
  /// Returns:
  ///
  /// int: The maximum number `k` such that both `k` and `-k` exist in the list.
  /// If no such number exists, it returns `-1`.
  ///
  /// Error Handling:
  ///
  /// This method does not explicitly handle errors. It assumes that the input
  /// is a list of integers.
  ///
  /// Time Complexity:
  /// Best-case scenario:
  /// The best-case scenario would be O(1), which would occur if the first
  /// element in the list has its negative counterpart in the list.
  /// Worst-case scenario:
  /// The worst-case scenario is O(n^2). This is because for each element in the
  /// list, the function checks if its negative counterpart exists in the list.
  /// The contains method itself has a time complexity of O(n), so the overall
  /// time complexity becomes O(n^2).
  /// Average-case scenario:
  /// The average-case scenario is also O(n^2) for the same reasons as the
  /// worst-case scenario.
  /// Space Complexity: The space complexity of the function is O(1). This is
  /// because the function only uses a fixed amount of space to store the
  /// maximum number found, regardless of the size of the input list. The space
  /// used does not increase with the size of the input list, so the space
  /// complexity is constant.
  int findMaxK(List<int> nums) {
    // Initialize the maximum number to -1
    int numver = -1;

    // Iterate over the list of numbers
    for (int i = 0; i < nums.length; i++) {
      // If the list contains the negative of the current number and the current
      // number is greater than the current maximum, update the maximum
      if (nums.contains(-nums[i]) && nums[i] > numver) {
        numver = nums[i];
      }
    }
    // Return the maximum number found, or -1 if no such number was found
    return numver;
  }
}
