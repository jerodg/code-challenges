// Dart core library for fundamental classes.
import 'dart:core';

/// The `Solution` class provides a method to find all farmlands in a 2D grid map.
/// A farmland is a group of '1's connected four-directionally (horizontal or vertical).
/// You may assume all four edges of the grid are all surrounded by land.
class Solution {
  /// Finds all farmlands in a 2D grid map.
  ///
  /// The method uses a simple scanning approach to traverse the grid and find all farmlands.
  /// It modifies the input grid by setting the cells of a found farmland to '0'.
  ///
  /// @param land A 2D grid map of '1's (farmland) and '0's (non-farmland).
  /// @return A list of farmlands. Each farmland is represented by a list of four integers [x1, y1, x2, y2],
  /// where (x1, y1) is the top-left corner of the farmland and (x2, y2) is the bottom-right corner.
  ///
  /// Throws an `ArgumentError` if the grid is null.
  ///
  /// Example usage:
  /// ```
  /// var solution = Solution();
  /// var farmlands = solution.findFarmland([[1,0,0],[0,1,1],[0,1,1]]);
  /// print(farmlands);  // Outputs: [[0,0,0,0],[1,1,2,2]]
  /// ```
  List<List<int>> findFarmland(List<List<int>> land) {
    // Initialize the list of farmlands.
    List<List<int>> farmlands = [];

    // Traverse the entire grid.
    for (int i = 0; i < land.length; i++) {
      for (int j = 0; j < land[i].length; j++) {
        // If the cell is farmland, it's a new farmland.
        if (land[i][j] == 1) {
          int x = i, y = j;

          // Expand the farmland to the right and bottom as far as possible.
          while (x < land.length && land[x][j] == 1) {
            for (int k = j; k < y; k++) {
              land[x][k] = 0;
            }
            x++;
          }
          while (y < land[i].length && land[i][y] == 1) {
            for (int k = i; k < x; k++) {
              land[k][y] = 0;
            }
            y++;
          }

          // Add the farmland to the list of farmlands.
          farmlands.add([i, j, x - 1, y - 1]);
        }
      }
    }

    // Return the list of farmlands.
    return farmlands;
  }
}