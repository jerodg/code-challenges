import 'dart:core';

/// Module for calculating the perimeter of an island in a 2D grid map.
///
/// This module provides a `Solution` class that can be used to calculate the perimeter of an island in a 2D grid map.
/// An island is a group of '1's connected four-directionally (horizontal or vertical).
/// You may assume all four edges of the grid are all surrounded by water.

class Solution {
  /// Calculates the perimeter of an island in a 2D grid map.
  ///
  /// This method uses a simple scanning approach to traverse the grid and calculate the perimeter of the island.
  ///
  /// @param grid A 2D grid map of '1's (land) and '0's (water).
  /// @return The perimeter of the island.
  ///
  /// Example usage:
  /// ```
  /// var solution = Solution();
  /// var perimeter = solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]);
  /// print(perimeter);  // Outputs: 16
  /// ```
  int islandPerimeter(List<List<int>> grid) {
    final rows = grid.length;
    final cols = grid[0].length;
    var perimeter = 0;

    for (var i = 0; i < rows; i++) {
      for (var j = 0; j < cols; j++) {
        if (grid[i][j] == 1) {
          perimeter += 4;
          if (i > 0 && grid[i - 1][j] == 1) perimeter -= 2;
          if (j > 0 && grid[i][j - 1] == 1) perimeter -= 2;
        }
      }
    }
    return perimeter;
  }
}
