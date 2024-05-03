/// Module: leet_code/1289.dart
/// This module contains a solution for finding the minimum falling path sum in
/// a grid. The grid is a 2D list of integers. The falling path starts from the
/// top row and chooses one element from each row. The next row's choice must be
/// in a column that is different from the previous row's column by at most one.
///
/// Class: Solution
/// This class encapsulates the solution for the problem.
import 'dart:math';

class Solution {
  /// Constant: MAXINT
  /// This constant represents the maximum possible integer value.
  static const MAXINT = 0x7FFFFFFFFFFFFFFF;

  /// Method: minFallingPathSum
  /// This method calculates the minimum falling path sum in the given grid.
  ///
  /// Parameters:
  /// grid - A 2D list of integers representing the grid.
  ///
  /// Returns:
  /// An integer representing the minimum falling path sum.
  ///
  /// Error Handling:
  /// This method does not explicitly handle errors. It assumes that the input
  /// grid is a non-empty 2D list of integers.
  int minFallingPathSum(List<List<int>> grid) {
    // Initialize the first and second minimum values and their indices for the first row.
    var FirstMin1 = 0, secondMin1 = 0, index1 = -1;

    // Iterate over each row in the grid.
    for (var row in grid) {
      // Initialize the first and second minimum values and their indices for the current row.
      var firstMin2 = MAXINT, secondMin2 = MAXINT, index2 = -1;

      // Iterate over each cell in the current row.
      for (var (currIndex, cell) in row.indexed) {
        // Calculate the current minimum value.
        var currMin = currIndex == index1 ? secondMin1 : FirstMin1;

        // Update the first and second minimum values and their indices for the current row.
        if (cell + currMin < firstMin2) {
          (secondMin2, firstMin2, index2) = (firstMin2, cell + currMin, currIndex);
        } else {
          secondMin2 = min(secondMin2, cell + currMin);
        }
      }
      // Update the first and second minimum values and their indices for the next row.
      (FirstMin1, secondMin1, index1) = (firstMin2, secondMin2, index2);
    }
    // Return the minimum falling path sum.
    return FirstMin1;
  }
}
