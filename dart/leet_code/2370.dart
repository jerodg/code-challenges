/// Dart module: leet_code/2370.dart
///
/// This module contains a solution for a problem from LeetCode. The problem is about finding the longest ideal string.
/// The solution is implemented in the `Solution` class, which has a method `longestIdealString`.
///
/// The `longestIdealString` method takes a string and an integer as input, and returns the length of the longest ideal string.
/// An ideal string is defined as a string where the difference between the ASCII values of any two characters is not more than `k`.
///
/// This module uses Dart 3.3 syntax and follows Dart and Google Style Guide standards.
library;

import 'dart:math';

class Solution {
  /// ASCII value of character 'a'.
  final int a = 'a'.codeUnitAt(0);

  /// Method: longestIdealString
  ///
  /// This method takes a string `s` and an integer `k` as input, and returns the length of the longest ideal string.
  /// An ideal string is defined as a string where the difference between the ASCII values of any two characters is not more than `k`.
  ///
  /// Parameters:
  /// - `s`: The input string. It is expected to be a string of lowercase English letters.
  /// - `k`: The maximum allowed difference between the ASCII values of any two characters in the ideal string.
  ///
  /// Returns:
  /// The length of the longest ideal string that can be formed from the input string `s`.
  ///
  /// Error Handling:
  /// This method does not explicitly handle errors. It assumes that the input parameters are of the correct type and within the expected range.
  int longestIdealString(String s, int k) {
    // Array to store the frequency of each character in the string.
    final List<int> alpha = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      // ASCII value of the current character, normalized to start from 0.
      final int cur = s.codeUnitAt(i) - a;
      // Minimum and maximum possible ASCII values for the characters in the ideal string.
      final int mn = max(0, cur - k);
      final int mx = min(25, cur + k);
      int curMax = 0;
      // Find the maximum frequency among the characters in the range [mn, mx].
      for (int j = mn; j <= mx; j++) {
        curMax = max(curMax, alpha[j] + 1);
      }
      // Update the frequency of the current character.
      alpha[cur] = max(1, curMax);
    }
    // Return the maximum frequency, which is the length of the longest ideal string.
    return alpha.reduce(max);
  }
}
