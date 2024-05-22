/// Dart implementation of the LeetCode problem 678: Valid Parenthesis String.
///
/// This module contains a class `Solution` with a method `checkValidString`.
/// The `checkValidString` method takes in one parameter:
/// - `s`: A string representing the input string of parentheses.
///
/// The method returns a boolean indicating whether the input string is valid.
/// The string is valid if it can be made balanced by replacing '*' with '(' or ')' or an empty string.
///
/// Error Handling:
/// - This method assumes that the input parameter is well-formed, i.e., `s` is a string of parentheses and '*'.
/// - If the input parameter is not well-formed, the behavior of the method is undefined.
library;

import 'dart:math';

class Solution {
  /// Checks whether the input string of parentheses is valid.
  ///
  /// This method uses two counters to keep track of the minimum and maximum number of open parentheses.
  /// It iterates over each character in the input string. If the character is '(', it increments both counters.
  /// If the character is ')', it decrements both counters. If the character is '*', it decrements the minimum counter and increments the maximum counter.
  /// If the maximum counter is less than 0, it returns false. If the minimum counter is less than 0, it resets it to 0.
  /// After the iteration, if the minimum counter is 0, it returns true. Otherwise, it returns false.
  ///
  /// @param s The input string of parentheses.
  /// @return A boolean indicating whether the input string is valid.
  bool checkValidString(String s) {
    int low = 0, high = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        low++;
        high++;
      } else if (s[i] == ')') {
        low--;
        high--;
      } else {
        low--;
        high++;
      }
      if (high < 0) {
        return false;
      }
      low = max(low, 0);
    }
    return low == 0;
  }
}
