/// Dart implementation of the LeetCode problem 85: Maximal Rectangle.
///
/// This module contains a class `Solution` with a method `maximalRectangle`.
/// The `maximalRectangle` method takes in one parameter:
/// - `matrix`: A 2D list of strings representing the binary matrix.
///
/// The method returns an integer representing the area of the maximal rectangle in the binary matrix.
///
/// Error Handling:
/// - This method assumes that the input parameter is well-formed, i.e., `matrix` is a 2D list of strings.
/// - If the input parameter is not well-formed, the behavior of the method is undefined.
library;

import 'dart:math';

class Solution {
  /// Finds the maximal rectangle in a binary matrix.
  ///
  /// This method uses dynamic programming to calculate the maximal width at each point in the matrix.
  /// Then it calculates the maximal area using the calculated widths.
  ///
  /// @param matrix The binary matrix.
  /// @return The area of the maximal rectangle.
  int maximalRectangle(List<List<String>> matrix) {
    // If the matrix is empty, return 0.
    if (matrix.isEmpty) return 0;

    // Get the dimensions of the matrix.
    int m = matrix.length;
    int n = matrix[0].length;

    // Initialize a 2D list to store the maximal width at each point in the matrix.
    List<List<int>> dp = List.generate(m, (_) => List.filled(n, 0));

    // Calculate the maximal width at each point in the matrix.
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (matrix[i][j] == '1') {
          dp[i][j] = j == 0 ? 1 : dp[i][j - 1] + 1;
        }
      }
    }

    // Initialize the maximal area to 0.
    int maxArea = 0;

    // Calculate the maximal area using the calculated widths.
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (matrix[i][j] == '1') {
          int width = dp[i][j];
          int area = width;
          for (int k = i - 1; k >= 0; k--) {
            width = min(width, dp[k][j]);
            area = max(area, width * (i - k + 1));
          }
          maxArea = max(maxArea, area);
        }
      }
    }

    // Return the maximal area.
    return maxArea;
  }
}
