// Importing dart:math library to use the max function.
import 'dart:math';

/// This class provides a solution for finding the maximal rectangle in a binary matrix.
class Solution {
  /// This function finds the maximal rectangle in a binary matrix.
  ///
  /// The function uses dynamic programming to calculate the maximal width at each point in the matrix.
  /// Then it calculates the maximal area using the calculated widths.
  ///
  /// @param matrix The binary matrix represented as a list of lists of strings.
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
