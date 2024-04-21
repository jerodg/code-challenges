/**
 * @fileoverview This module provides a function to calculate the perimeter of an island in a 2D grid.
 */

/**
 * Calculates the perimeter of an island in a 2D grid.
 * The grid is represented as a 2D array where 0 represents water and 1 represents land.
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 * Assume all four edges of the grid are surrounded by water.
 *
 * @param {number[][]} grid - The 2D grid representation of the map.
 * @return {number} The perimeter of the island.
 *
 * @throws {TypeError} If the input grid is not a 2D array.
 * @throws {Error} If the grid does not contain any land (1s).
 */
let islandPerimeter = function (grid) {
    // Validate the input grid.
    if (!Array.isArray(grid) || !Array.isArray(grid[0])) {
        throw new TypeError('The input grid must be a 2D array.');
    }

    let peri = 0;  // Initialize the perimeter of the island.

    // Iterate over the rows of the grid.
    for (let i = 0; i < grid.length; i++) {
        // Iterate over the columns of the grid.
        for (let j = 0; j < grid[0].length; j++) {
            // If the current cell is land, calculate the possible perimeter.
            if (1 === grid[i][j]) {
                let poss = 4;  // Initialize the possible perimeter.

                // Check the left cell.
                if (1 === grid[i][j - 1]) {
                    poss--;
                }

                // Check the right cell.
                if (1 === grid[i][j + 1]) {
                    poss--;
                }

                // Check the bottom cell.
                if (i + 1 < grid.length) {
                    if (1 === grid[i + 1][j]) {
                        poss--;
                    }
                }

                // Check the top cell.
                if (0 <= i - 1) {
                    if (1 === grid[i - 1][j]) {
                        poss--;
                    }
                }

                // Add the possible perimeter to the total perimeter.
                peri += poss;
            }
        }
    }

    // If the perimeter is still 0, there is no land in the grid.
    if (0 === peri) {
        throw new Error('The grid does not contain any land.');
    }

    // Return the perimeter of the island.
    return peri;
};
