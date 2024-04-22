/// <summary>
/// This class provides a solution for the problem of calculating the perimeter of an island in a 2D grid map.
/// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
/// </summary>
public class Solution
{
    /// <summary>
    /// This method calculates the perimeter of an island in the given grid.
    /// </summary>
    /// <param name="grid">A 2D grid map of '1's (land) and '0's (water).</param>
    /// <returns>The perimeter of the island.</returns>
    public int IslandPerimeter(int[][] grid)
    {
        int res = 0; // The perimeter of the island.

        // Iterate over each cell in the grid.
        for (int i = 0; i < grid.Length; i++)
        {
            for (int j = 0; j < grid[i].Length; j++)
            {
                // If the cell is land, check its four sides for water or grid boundary and increment the perimeter accordingly.
                if (grid[i][j] == 1)
                {
                    if (i == 0 || grid[i - 1][j] == 0)
                        res++;
                    if (i == grid.Length - 1 || grid[i + 1][j] == 0)
                        res++;
                    if (j == 0 || grid[i][j - 1] == 0)
                        res++;
                    if (j == grid[i].Length - 1 || grid[i][j + 1] == 0)
                        res++;
                }
            }
        }
        return res; // Return the perimeter of the island.
    }
}
