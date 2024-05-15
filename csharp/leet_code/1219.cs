/// <summary>
/// The Solution class contains methods to solve the problem of finding the maximum gold in a grid.
/// </summary>
public class Solution {
    /// <summary>
    /// This method calculates the maximum gold that can be collected from the grid.
    /// </summary>
    /// <param name="grid">A 2D array representing the grid.</param>
    /// <returns>The maximum amount of gold that can be collected.</returns>
    public int GetMaximumGold(int[][] grid) {
        int res = 0;

        // Iterate over each cell in the grid
        for(int i=0; i<grid.Length; i++){
            for(int j=0; j<grid[i].Length; j++){
                // If the cell is not empty (contains gold)
                if(grid[i][j]!=0){
                    // Update the maximum gold collected so far
                    res = Math.Max(res, GetMaximumGoldHelper(grid, i, j));
                }
            }
        }

        // Return the maximum gold collected
        return res;
    }

    /// <summary>
    /// This helper method calculates the maximum gold that can be collected starting from a specific cell.
    /// </summary>
    /// <param name="grid">A 2D array representing the grid.</param>
    /// <param name="row">The row index of the starting cell.</param>
    /// <param name="column">The column index of the starting cell.</param>
    /// <returns>The maximum amount of gold that can be collected starting from the specified cell.</returns>
    private int GetMaximumGoldHelper(int[][] grid, int row, int column){
        // If the cell is out of bounds or empty (does not contain gold), return 0
        if(row < 0 || row >= grid.Length || column < 0 || column >= grid[row].Length || grid[row][column] == 0){
            return 0;
        }

        // Store the amount of gold in the current cell
        int current = grid[row][column];
        // Mark the current cell as visited (empty)
        grid[row][column] = 0;

        // Calculate the maximum gold that can be collected from the neighboring cells
        int count = current + Math.Max(GetMaximumGoldHelper(grid, row-1, column),
            Math.Max(GetMaximumGoldHelper(grid, row+1, column),
                Math.Max(GetMaximumGoldHelper(grid, row, column-1),
                    GetMaximumGoldHelper(grid, row, column+1))));

        // Restore the amount of gold in the current cell
        grid[row][column] = current;

        // Return the maximum gold collected
        return count;
    }
}
