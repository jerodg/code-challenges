/// Dart implementation of the LeetCode problem 27: Maximum Depth of a Parentheses String.
///
/// This module contains a class `Solution` with a method `maxDepth`.
/// The `maxDepth` method takes in one parameter:
/// - `s`: A string containing parentheses.
///
/// The method returns an integer representing the maximum depth of valid parentheses in the string.
///
/// Error Handling:
/// - This method assumes that the input parameter is well-formed, i.e., `s` is a string containing only parentheses.
/// - If the input parameter is not well-formed, the behavior of the method is undefined.

import 'dart:core';

class Solution {
  /// Calculates the maximum depth of valid parentheses in a string.
  ///
  /// This method uses a counter to keep track of the depth of parentheses. The counter is incremented when an opening parenthesis is encountered and decremented when a closing parenthesis is encountered.
  /// The maximum depth is updated whenever the counter is incremented.
  ///
  /// @param s The string containing parentheses.
  /// @return The maximum depth of valid parentheses in the string.
  int maxDepth(String s) {
    // Initialize the maximum depth and the counter.
    int max = 0;
    int count = 0;

    // Traverse the string.
    for (int i = 0; i < s.length; i++) {
      // If the current character is an opening parenthesis, increment the counter and update the maximum depth.
      if (s[i] == '(') {
        count++;
        max = count > max ? count : max;
      }
      // If the current character is a closing parenthesis, decrement the counter.
      else if (s[i] == ')') {
        count--;
      }
    }

    // Return the maximum depth.
    return max;
  }
}
