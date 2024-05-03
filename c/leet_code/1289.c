/**
 * @file leet_code/1289.c
 * @brief This module provides a function to calculate the minimum falling path
 * sum in a grid.
 *
 * A falling path starts at any element in the first row and chooses the element
 * in the next row which is either directly below or diagonally left/right.
 * Specifically, the path can only move to the neighboring cells in the next row
 * down. The function `minFallingPathSum` takes a 2D grid as input, and returns
 * the minimum sum of a falling path through non-zero cells. The function uses
 * dynamic programming to keep track of the minimum sum.
 */

#pragma GCC optimize("O3,unroll-loops")
#include <limits.h>

/**
 * @brief Calculates the minimum falling path sum in a grid.
 *
 * This function iterates over the grid from the top to the bottom. For each
 * cell, it calculates the minimum sum of a falling path that ends at this cell.
 * It keeps track of the minimum sum and the column of the cell with the minimum
 * sum in the previous row. After the iteration, it returns the minimum sum of a
 * falling path in the grid.
 *
 * @param grid Pointer to the 2D grid.
 * @param gridSize The size of the grid.
 * @param gridColSize The size of the columns in the grid.
 * @return The minimum sum of a falling path in the grid, as an integer.
 */
int minFallingPathSum(int **grid, const int gridSize, int *gridColSize) {
  int c_min = 0, p_min = 0,
      p_col = -1; // The minimum sum, the previous minimum sum, and the column
                  // of the cell with the previous minimum sum.
  const int n = gridSize; // The size of the grid.

  // Iterate over the grid from the top to the bottom.
  for (int i = 0; i < n; ++i) {
    int nc_min = INT_MAX, np_min = INT_MAX,
        nc_col = -1; // The new minimum sum, the new previous minimum sum, and
                     // the column of the cell with the new minimum sum.

    // Iterate over the cells in the current row.
    for (int j = 0; j < n; ++j) {
      const int t = (p_col != j ? c_min : p_min) +
                    grid[i][j]; // The sum of the current cell and the minimum
                                // sum of the previous row.

      // Update the new minimum sum and the column of the cell with the new
      // minimum sum.
      if (t < nc_min)
        np_min = nc_min, nc_min = t, nc_col = j;
      else if (t < np_min)
        np_min = t;
    }

    // Update the minimum sum, the previous minimum sum, and the column of the
    // cell with the minimum sum.
    c_min = nc_min, p_min = np_min, p_col = nc_col;
  }

  return c_min; // Return the minimum sum of a falling path in the grid.
}
