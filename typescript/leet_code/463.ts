/**
 * @fileoverview This module provides a function to calculate the perimeter of an island in a given grid.
 * @module leet_code/463
 */

/**
 * Function to calculate the perimeter of an island in a given grid.
 * The function iterates over the grid and for each cell that is part of the island, it checks its four neighbors.
 * If a neighbor is out of bounds or is water, it increments the perimeter.
 *
 * @param {number[][]} grid - The grid where 0 represents water and 1 represents an island.
 * @returns {number} - The perimeter of the island.
 */
function islandPerimeter(grid: number[][]): number {
    // The number of rows in the grid
    const row = grid.length;
    // The number of columns in the grid
    const col = grid[0].length;
    // The perimeter of the island
    let ans = 0;

    // Iterate over the grid
    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            // Check if the current cell is part of the island
            if (grid[i][j] === 1) {
                // Check the top neighbor
                if (i < 1 || grid[i - 1][j] === 0) {
                    ans++;
                }
                // Check the bottom neighbor
                if (i === row - 1 || grid[i + 1][j] === 0) {
                    ans++;
                }
                // Check the left neighbor
                if (j < 1 || grid[i][j - 1] === 0) {
                    ans++;
                }
                // Check the right neighbor
                if (j === col - 1 || grid[i][j + 1] === 0) {
                    ans++;
                }
            }
        }
    }

    // Return the perimeter of the island
    return ans;
}
