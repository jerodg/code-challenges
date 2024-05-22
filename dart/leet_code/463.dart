/// Dart implementation of the LeetCode problem 463: Island Perimeter.
///
/// This module contains a class `Solution` with a method `islandPerimeter`.
/// The `islandPerimeter` method takes in one parameter:
/// - `grid`: A 2D list of integers representing the grid map of '1's (land) and '0's (water).
///
/// The method returns an integer representing the perimeter of the island in the grid map.
/// An island is a group of '1's connected four-directionally (horizontal or vertical).
/// You may assume all four edges of the grid are all surrounded by water.
///
/// Error Handling:
/// - This method assumes that the input parameter is well-formed, i.e., `grid` is a 2D list of integers.
/// - If the input parameter is not well-formed, the behavior of the method is undefined.
library;

import 'dart:core';

class Solution {
  /// Calculates the perimeter of an island in a 2D grid map.
  ///
  /// This method uses a simple scanning approach to traverse the grid and calculate the perimeter of the island.
  /// It iterates over each cell in the grid. If the cell is a land cell, it adds 4 to the perimeter.
  /// Then it checks the adjacent cells. If the adjacent cell is also a land cell, it subtracts 2 from the perimeter.
  /// This is because each adjacent land cell reduces the perimeter by 2.
  ///
  /// @param grid A 2D grid map of '1's (land) and '0's (water).
  /// @return The perimeter of the island.
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
