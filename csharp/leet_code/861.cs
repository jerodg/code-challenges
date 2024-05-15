// Copyright ©JerodG <https://github.com/jerodg/> 2010-2024.
//
// This program is free software: you can redistribute it and/or modify it under the terms of the
// Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
// or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
// even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
// for more details.
//
// The above copyright notice and this permission notice shall be included in all copies or
// substantial portions of the Software. You should have received a copy of the SSPL along with this
// program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

/// <summary>
/// The Solution class contains methods to solve the problem.
/// This class is part of a leet code solution.
/// </summary>
public class Solution
{
    /// <summary>
    /// The MatrixScore method calculates the maximum possible score after flipping the binary matrix.
    /// This method is part of a leet code solution.
    /// </summary>
    /// <param name="grid">A 2D integer array representing the binary matrix.</param>
    /// <returns>An integer representing the maximum possible score.</returns>
    public int MatrixScore(int[][] grid)
    {
        // Initialize the result to 0
        var res = 0;

        // Get the dimensions of the grid
        var (m, n) = (grid.Length, grid[0].Length);

        // Flip the rows of the grid if the first element is 0
        for (var i = 0; i < m; i++)
            if (grid[i][0] == 0)
                for (var j = 0; j < n; j++)
                    grid[i][j] = 1 - grid[i][j]; // Flip the element

        // Flip the columns of the grid if the number of 0s is more than half the size of the column
        for (var i = 0; i < n; i++)
        {
            var zeroSum = 0;
            for (var j = 0; j < m; j++)
                if (grid[j][i] == 0)
                    zeroSum++; // Count the number of 0s
            if (zeroSum > m / 2)
                for (var j = 0; j < m; j++)
                    grid[j][i] = 1 - grid[j][i]; // Flip the element
        }

        // Calculate the score for each row and add it to the result
        for (var i = 0; i < m; i++)
        {
            var val = 0;
            for (var j = 0; j < n; j++)
                val = val * 2 + grid[i][j]; // Calculate the score for the row
            res += val; // Add the score to the result
        }

        // Return the result
        return res;
    }
}
