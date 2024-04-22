/// <summary>
/// This class provides a solution for the problem of finding farmland in a 2D grid map.
/// A farmland is a group of '1's (land) connected horizontally and vertically.
/// </summary>
public class Solution
{
    /// <summary>
    /// This method finds all the farmlands in the given grid.
    /// </summary>
    /// <param name="land">A 2D grid map of '1's (land) and '0's (water).</param>
    /// <returns>An array of farmlands where each farmland is represented by an array of four integers [rowStart, colStart, rowEnd, colEnd].</returns>
    public int[][] FindFarmland(int[][] land)
    {
        int m = land.Length; // The number of rows in the grid.
        int n = land[0].Length; // The number of columns in the grid.
        bool[,] visited = new bool[m, n]; // A 2D array to keep track of visited cells.
        var result = new List<int[]>(); // A list to store the farmlands.

        // Iterate over each cell in the grid.
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                // If the cell is land and has not been visited, find the coordinates of the farmland and add it to the result.
                if (land[i][j] == 1 && !visited[i, j])
                {
                    int[] coordinates = FindCoordinates(land, i, j, visited);
                    result.Add(coordinates);
                }
            }
        }
        return result.ToArray(); // Return the farmlands.
    }

    /// <summary>
    /// This method finds the coordinates of a farmland in the grid.
    /// </summary>
    /// <param name="land">A 2D grid map of '1's (land) and '0's (water).</param>
    /// <param name="y">The row index of the current cell.</param>
    /// <param name="x">The column index of the current cell.</param>
    /// <param name="visited">A 2D array to keep track of visited cells.</param>
    /// <returns>An array of four integers [rowStart, colStart, rowEnd, colEnd] representing the farmland.</returns>
    private int[] FindCoordinates(int[][] land, int y, int x, bool[,] visited)
    {
        int yEnd = y; // The row index of the end of the farmland.
        int xEnd = x; // The column index of the end of the farmland.

        // Find the row index of the end of the farmland.
        while (yEnd < land.Length - 1 && land[yEnd + 1][x] == 1)
        {
            ++yEnd;
        }

        // Find the column index of the end of the farmland.
        while (xEnd < land[0].Length - 1 && land[y][xEnd + 1] == 1)
        {
            ++xEnd;
        }

        // Mark all the cells of the farmland as visited.
        for (int i = y; i <= yEnd; i++)
        {
            for (int j = x; j <= xEnd; j++)
            {
                visited[i, j] = true;
            }
        }

        // Return the coordinates of the farmland.
        return new int[] { y, x, yEnd, xEnd };
    }
}
