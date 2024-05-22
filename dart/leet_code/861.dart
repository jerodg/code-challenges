/// Copyright ©2010-2024 JerodG <https://github.com/jerodg/>
///
/// This program is free software: you can redistribute it and/or modify it under the terms of the
/// Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
/// or (at your option) any later version.
///
/// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
/// even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
/// for more details.
///
/// The above copyright notice and this permission notice shall be included in all copies or
/// substantial portions of the Software. You should have received a copy of the SSPL along with this
/// program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
library;

import 'dart:math';

/// A solution class for solving a specific problem.
///
/// This class provides a method to calculate the maximum score of a binary matrix after flipping.
class Solution {
  /// Calculates the maximum score of a binary matrix after flipping.
  ///
  /// The method works by first flipping the rows of the matrix so that the first bit of each row is 1.
  /// Then, for each column, it counts the number of 1s and flips the column if the number of 0s is greater.
  /// The score is calculated by treating each row of the matrix as a binary number.
  ///
  /// @param grid The binary matrix represented as a list of lists of integers.
  /// @return The maximum score that can be achieved after flipping.
  int matrixScore(List<List<int>> grid) {
    int rowCount = grid.length;
    int colCount = grid[0].length;

    // Initialize the score with the contribution of the first column (which will always be 1s after flipping the rows).
    int score = (1 << (colCount - 1)) * rowCount;

    // Iterate over the rest of the columns.
    for (int j = 1; j < colCount; j++) {
      int countOfOnes = 0;

      // Count the number of 1s in the column.
      for (int i = 0; i < rowCount; i++) {
        countOfOnes += grid[i][j] ^ grid[i][0];
      }

      // Add the maximum of the count of 1s and the count of 0s to the score.
      score += max(countOfOnes, rowCount - countOfOnes) * (1 << (colCount - j - 1));
    }

    return score;
  }
}
