/// Module: leet_code/881.dart
///
/// This module contains a solution for the LeetCode problem 881. "Boats to Save People".
/// The main class `Solution` provides a method `numRescueBoats` to solve the problem.
///
/// The `numRescueBoats` method calculates the minimum number of boats required to rescue
/// people whose weights are given in a list. Each boat can carry a maximum weight of `limit`.
///
/// Time Complexity:
/// - Best-case: O(n log n), where n is the length of the list `a`. This is due to the sorting operation.
/// - Worst-case: O(n log n), same reason as above.
/// - Average-case: O(n log n), same reason as above.
///
/// Space Complexity: O(1), no additional space is used.
library;

class Solution {
  /// Calculates the minimum number of boats required to rescue people.
  ///
  /// The function sorts the list of weights and uses a two-pointer technique to pair the heaviest
  /// and lightest person until all people are paired or only the heaviest people remain. Each pair
  /// or single person requires one boat.
  ///
  /// @param a: A list of integers representing the weights of each person.
  /// @param limit: An integer representing the maximum weight a boat can carry.
  ///
  /// @return: The minimum number of boats required to rescue all people.
  ///
  /// Error Handling: This function assumes that all inputs are valid. That is, `a` is a non-empty
  /// list of positive integers and `limit` is a positive integer.
  int numRescueBoats(List<int> a, int limit) {
    int count = 0; // Initialize the count of boats
    a.sort(); // Sort the list of weights
    int left = 0; // Pointer to the lightest person
    int right = a.length - 1; // Pointer to the heaviest person

    // Continue until all people are paired or only the heaviest people remain
    while (left <= right) {
      // If the lightest and heaviest person can be paired, move both pointers
      if (a[left] + a[right] <= limit) {
        left++;
        right--;
      } else {
        // If not, only move the pointer to the heaviest person
        right--;
      }
      // Increase the count of boats
      count++;
    }
    // Return the count of boats
    return count;
  }
}
