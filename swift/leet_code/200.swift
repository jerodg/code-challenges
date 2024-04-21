/**
 `Solution` is a class that provides methods to solve the problem of finding the number of islands in a 2D grid. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

 - Note: The grid is represented as a 2D array of `Character` where '1' represents land and '0' represents water.

 - Important: This class uses Depth-First Search (DFS) algorithm to traverse the grid.

 - Requires: The grid should not be empty.

 - Version: 1.0
 - Author: User
 */

import Foundation

class Solution {
    /**
      This method performs a Depth-First Search (DFS) on the grid starting from the cell at the position (i, j).

      - Parameters:
        - grid: The 2D grid represented as an array of `Character`.
        - i: The row index of the starting cell.
        - j: The column index of the starting cell.

      - Note: This method modifies the grid in-place by marking the visited cells as '0'.
     */
    func dfs(_ grid: inout [[Character]], _ i: Int, _ j: Int) {
        if i < 0 || i >= grid.count || j < 0 || j >= grid[i].count || grid[i][j] == "0" {
            return
        }
        grid[i][j] = "0"
        dfs(&grid, i + 1, j)
        dfs(&grid, i - 1, j)
        dfs(&grid, i, j + 1)
        dfs(&grid, i, j - 1)
    }

    /**
      This method returns the number of islands in the given grid.

      - Parameter grid: The 2D grid represented as an array of `Character`.

      - Returns: The number of islands in the grid.

      - Example:
        ```
        let solution = Solution()
        let grid: [[Character]] = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
        print(solution.numIslands(grid)) // Prints: 1
        ```

      - Note: This method uses the `dfs` method to traverse the grid.
     */
    func numIslands(_ grid: [[Character]]) -> Int {
        var grid = grid
        var count = 0
        for i in 0 ..< grid.count {
            for j in 0 ..< grid[i].count {
                if grid[i][j] == "1" {
                    count += 1
                    dfs(&grid, i, j)
                }
            }
        }
        return count
    }
}
