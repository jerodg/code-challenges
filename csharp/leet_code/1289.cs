using System;
using System.Linq;

/// <summary>
/// This module contains the Solution class which provides a method to find the minimum falling path sum in a 2D grid.
/// </summary>
public class Solution {
    /// <summary>
    /// Finds the minimum falling path sum in a 2D grid.
    /// </summary>
    /// <param name="grid">A 2D array of integers representing the grid.</param>
    /// <returns>
    /// The minimum falling path sum in the grid.
    /// </returns>
    public int MinFallingPathSum(int[][] grid) {
        // Get the number of rows in the grid
        int n = grid.Length;
        // Get the number of columns in the grid
        int m = grid[0].Length;
        // Initialize a 2D array to store the dynamic programming state
        int[][] dp = new int[n][];

        // Initialize the dynamic programming state with the first row of the grid
        for (int i = 0; i < n; i++)
            dp[i] = new int[m];
        Array.Copy(grid[0], dp[0], m);

        // Iterate over the rows of the grid starting from the second row
        for (int r = 1; r < n; r++) {
            // Get the previous row from the dynamic programming state
            int[] prevRow = dp[r - 1];
            // Initialize the indices of the minimum and second minimum elements in the previous row
            int minIndex = 0;
            int secondMinIndex = 1;
            // Swap the indices if the second element is smaller than the first
            if (prevRow[minIndex] > prevRow[secondMinIndex]) {
                int temp = minIndex;
                minIndex = secondMinIndex;
                secondMinIndex = temp;
            }
            // Update the indices of the minimum and second minimum elements
            for (int i = 2; i < m; i++) {
                if (prevRow[i] < prevRow[minIndex]) {
                    secondMinIndex = minIndex;
                    minIndex = i;
                } else if (prevRow[i] < prevRow[secondMinIndex]) {
                    secondMinIndex = i;
                }
            }

            // Update the current row in the dynamic programming state
            for (int c = 0; c < m; c++) {
                if (c == minIndex) {
                    dp[r][c] = grid[r][c] + prevRow[secondMinIndex];
                } else {
                    dp[r][c] = grid[r][c] + prevRow[minIndex];
                }
            }
        }
        // Return the minimum element in the last row of the dynamic programming state
        return dp[n - 1].Min();
    }
}
