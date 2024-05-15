/// This file contains the implementation of a solution for the problem of finding the maximum gold in a grid.
/// The grid is represented as a 2D list of integers, where each integer represents the amount of gold at that cell.
/// The solution uses depth-first search (DFS) to explore all possible paths in the grid.
///
/// Copyright © 2010-2024 JerodG <https://github.com/jerodg/>
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
import 'dart:math';

/// The `Solution` class provides a method to find the maximum amount of gold that can be collected in a grid.
class Solution {
  /// A 2D list of booleans to keep track of the cells that have been visited during the DFS.
  List<List<bool>> vis = [];

  /// A copy of the original grid.
  List<List<int>> copyGrid = [];

  /// The current sum of gold collected during the DFS.
  int sum = 0;

  /// The maximum amount of gold collected so far.
  int ans = 0;

  /// The `dfs` method performs a depth-first search on the grid starting from the cell at position (i, j).
  /// It updates the `sum` and `ans` variables to keep track of the current and maximum amount of gold collected.
  ///
  /// Parameters:
  /// - `i`: The row index of the current cell.
  /// - `j`: The column index of the current cell.
  void dfs(int i, int j) {
    if (i < 0 || i >= copyGrid.length || j < 0 || j >= copyGrid[0].length || copyGrid[i][j] == 0 || vis[i][j]) return;
    vis[i][j] = true;
    sum += copyGrid[i][j];
    ans = max(ans, sum);
    dfs(i + 1, j);
    dfs(i - 1, j);
    dfs(i, j + 1);
    dfs(i, j - 1);
    vis[i][j] = false;
    sum -= copyGrid[i][j];
  }

  /// The `getMaximumGold` method finds the maximum amount of gold that can be collected in the given grid.
  ///
  /// Parameters:
  /// - `grid`: A 2D list of integers representing the grid.
  ///
  /// Returns:
  /// - The maximum amount of gold that can be collected.
  int getMaximumGold(List<List<int>> grid) {
    ans = 0;
    copyGrid = grid;
    vis = List.generate(grid.length, (_) => List.generate(grid[0].length, (_) => false));
    for (int i = 0; i < grid.length; i++) {
      for (int j = 0; j < grid[0].length; j++) {
        dfs(i, j);
      }
    }
    return ans;
  }
}
