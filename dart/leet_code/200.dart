/// The `Solution` class provides a method to count the number of islands in a 2D grid map.
/// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
/// You may assume all four edges of the grid are all surrounded by water.
class Solution {
  /// Counts the number of islands in a 2D grid map.
  ///
  /// The method uses Depth-First Search (DFS) to traverse the grid and count the number of islands.
  /// It uses an iterative approach with a stack and a separate visited matrix to avoid modifying the input grid.
  ///
  /// @param grid A 2D grid map of '1's (land) and '0's (water).
  /// @return The number of islands.
  ///
  /// Throws an `ArgumentError` if the grid is null.
  ///
  /// Example usage:
  /// ```
  /// var solution = Solution();
  /// var count = solution.numIslands([['1', '1', '1', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]);
  /// print(count);  // Outputs: 3
  /// ```
  int numIslands(List<List<String>> grid) {
    if (grid == null) {
      throw ArgumentError('Grid must not be null');
    }

    int count = 0;
    List<List<bool>> visited = List.generate(
        grid.length, (_) => List.generate(grid[0].length, (_) => false));

    /// Performs a Depth-First Search from a given cell.
    ///
    /// @param row The row index of the cell.
    /// @param col The column index of the cell.
    void dfs(int row, int col) {
      List<List<int>> directions = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
      ];
      List<List<int>> stack = [
        [row, col]
      ];

      while (stack.isNotEmpty) {
        List<int> node = stack.removeLast();
        int r = node[0], c = node[1];

        for (List<int> direction in directions) {
          int newRow = r + direction[0], newCol = c + direction[1];
          if (newRow >= 0 &&
              newRow < grid.length &&
              newCol >= 0 &&
              newCol < grid[0].length &&
              grid[newRow][newCol] == '1' &&
              !visited[newRow][newCol]) {
            stack.add([newRow, newCol]);
            visited[newRow][newCol] = true;
          }
        }
      }
    }

    for (int i = 0; i < grid.length; i++) {
      for (int j = 0; j < grid[i].length; j++) {
        if (grid[i][j] == '1' && !visited[i][j]) {
          count++;
          dfs(i, j);
        }
      }
    }
    return count;
  }
}
