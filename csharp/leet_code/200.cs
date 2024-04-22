/// <summary>
/// This class provides a solution for the problem of counting the number of islands in a 2D grid map.
/// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
/// </summary>
public class Solution
{
    /// <summary>
    /// This method counts the number of islands in the given grid.
    /// </summary>
    /// <param name="grid">A 2D grid map of '1's (land) and '0's (water).</param>
    /// <returns>The number of islands.</returns>
    public int NumIslands(char[][] grid)
    {
        int m = grid.Length; // The number of rows in the grid.
        int n = grid[0].Length; // The number of columns in the grid.
        int ans = 0; // The count of islands.
        bool[,] visited = new bool[m, n]; // A 2D array to keep track of visited cells.

        // Iterate over each cell in the grid.
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                // If the cell is land and has not been visited, traverse the island and increment the count.
                if (!visited[i, j] && grid[i][j] == '1')
                {
                    TraverseIsland(grid, i, j, visited, m, n);
                    ans++;
                }
            }
        }
        return ans; // Return the count of islands.
    }

    /// <summary>
    /// This method traverses an island in the grid using Depth-First Search (DFS).
    /// </summary>
    /// <param name="grid">A 2D grid map of '1's (land) and '0's (water).</param>
    /// <param name="x">The row index of the current cell.</param>
    /// <param name="y">The column index of the current cell.</param>
    /// <param name="visited">A 2D array to keep track of visited cells.</param>
    /// <param name="m">The number of rows in the grid.</param>
    /// <param name="n">The number of columns in the grid.</param>
    private void TraverseIsland(char[][] grid, int x, int y, bool[,] visited, int m, int n)
    {
        // If the current cell is out of the grid's bounds or is water or has been visited, return.
        if (x < 0 || y < 0 || x >= m || y >= n || grid[x][y] != '1' || visited[x, y])
        {
            return;
        }

        visited[x, y] = true; // Mark the current cell as visited.

        // Traverse the adjacent cells.
        TraverseIsland(grid, x + 1, y, visited, m, n);
        TraverseIsland(grid, x - 1, y, visited, m, n);
        TraverseIsland(grid, x, y - 1, visited, m, n);
        TraverseIsland(grid, x, y + 1, visited, m, n);
    }
}
