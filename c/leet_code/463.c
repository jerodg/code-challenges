/**
 * This module provides a function to calculate the perimeter of an island in a grid.
 * The island is represented by 1s and the water is represented by 0s.
 * The grid cells are connected horizontally/vertically (not diagonally).
 * The grid is completely surrounded by water, and there is exactly one island.
 */

#include <stdio.h>

/**
 * Function to calculate the perimeter of an island in a grid.
 *
 * The island is represented by 1s and the water is represented by 0s.
 * The grid cells are connected horizontally/vertically (not diagonally).
 * The grid is completely surrounded by water, and there is exactly one island.
 *
 * @param grid A 2D array representing the grid. This function assumes that the grid is well-formed and contains at least one cell.
 * @param gridSize The size of the grid (number of rows). This should be a positive integer.
 * @param gridColSize An array containing the size of each column. Each element should be a positive integer.
 * @return The perimeter of the island. This is a non-negative integer.
 *
 * Example usage:
 * int **grid = ...; // Initialize grid
 * int gridSize = ...; // Initialize gridSize
 * int *gridColSize = ...; // Initialize gridColSize
 * int perimeter = islandPerimeter(grid, gridSize, gridColSize);
 */

int islandPerimeter(int **grid, int gridSize, int *gridColSize) {
    int perimeter = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            if (grid[i][j] == 1) {
                perimeter += 4;

                // Subtract 2 for each adjacent land cell to the right
                if (j < gridColSize[i] - 1 && grid[i][j + 1] == 1) {
                    perimeter -= 2;
                }

                // Subtract 2 for each adjacent land cell below
                if (i < gridSize - 1 && grid[i + 1][j] == 1) {
                    perimeter -= 2;
                }
            }
        }
    }
    return perimeter;
}
