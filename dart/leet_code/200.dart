/// Dart implementation of the LeetCode problem 200: Number of Islands.
///
/// This module contains a class `Solution` with a method `numIslands`.
/// The `numIslands` method takes in one parameter:
/// - `grid`: A 2D list of strings representing the grid map of '1's (land) and '0's (water).
///
/// The method returns an integer representing the number of islands in the grid map.
/// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
///
/// Error Handling:
/// - This method assumes that the input parameter is well-formed, i.e., `grid` is a 2D list of strings.
/// - If the input parameter is not well-formed, the behavior of the method is undefined.
/// - If the grid is null, an `ArgumentError` is thrown.
library;

class Solution {
  /// Counts the number of islands in a 2D grid map.
  ///
  /// This method uses Depth-First Search (DFS) to traverse the grid and count the number of islands.
  /// It uses an iterative approach with a stack and a separate visited matrix to avoid modifying the input grid.
  ///
  /// @param grid A 2D grid map of '1's (land) and '0's (water).
  /// @return The number of islands.
  int numIslands(List<List<String>> grid) {
    // Initialize the count of islands to 0.
    int count = 0;

    // Initialize a 2D list to keep track of visited cells.
    List<List<bool>> visited = List.generate(grid.length, (_) => List.generate(grid[0].length, (_) => false));

    /// Performs a Depth-First Search from a given cell.
    ///
    /// @param row The row index of the cell.
    /// @param col The column index of the cell.
    void dfs(int row, int col) {
      // Define the four possible directions to move in the grid.
      List<List<int>> directions = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
      ];

      // Initialize a stack and add the starting cell to it.
      List<List<int>> stack = [
        [row, col]
      ];

      // While there are cells in the stack, continue the DFS.
      while (stack.isNotEmpty) {
        // Pop a cell from the stack.
        List<int> node = stack.removeLast();
        int r = node[0], c = node[1];

        // For each direction, check if the adjacent cell is within the grid and is a land cell.
        for (List<int> direction in directions) {
          int newRow = r + direction[0], newCol = c + direction[1];
          if (newRow >= 0 &&
              newRow < grid.length &&
              newCol >= 0 &&
              newCol < grid[0].length &&
              grid[newRow][newCol] == '1' &&
              !visited[newRow][newCol]) {
            // If the adjacent cell is a valid land cell, add it to the stack and mark it as visited.
            stack.add([newRow, newCol]);
            visited[newRow][newCol] = true;
          }
        }
      }
    }

    // Traverse the grid.
    for (int i = 0; i < grid.length; i++) {
      for (int j = 0; j < grid[i].length; j++) {
        // If the current cell is a land cell and has not been visited, start a DFS from it and increment the count of islands.
        if (grid[i][j] == '1' && !visited[i][j]) {
          count++;
          dfs(i, j);
        }
      }
    }

    // Return the count of islands.
    return count;
  }
}
