/**
 * @fileoverview This module provides a function to find all farmlands in a 2D grid.
 */

/**
 * Finds all farmlands in a 2D grid.
 * The grid is represented as a 2D array where 0 represents water and 1 represents farmland.
 * A farmland is formed by connecting adjacent lands horizontally or vertically.
 * The function returns a list of all farmlands, where each farmland is represented by a list of four integers [row, col, bottomRow, bottomCol],
 * where (row, col) is the top-left corner of the farmland, and (bottomRow, bottomCol) is the bottom-right corner of the farmland.
 *
 * @param {number[][]} land - The 2D grid representation of the map.
 * @return {number[][]} A list of all farmlands.
 *
 * @throws {TypeError} If the input land is not a 2D array.
 */
let findFarmland = function (land) {
    // Validate the input land.
    if (!Array.isArray(land) || !Array.isArray(land[0])) {
        throw new TypeError('The input land must be a 2D array.');
    }

    const result = [];  // Initialize the result list.
    let bottomCol = 0;  // Initialize the bottom column index.
    let bottomRow = 0;  // Initialize the bottom row index.

    /**
     * Performs a depth-first search on the grid to find all farmlands.
     * @param {number} i - The current row index.
     * @param {number} j - The current column index.
     */
    const dfs = (i, j) => {
        // If the current cell is out of the grid or is water, return.
        if (i < 0 || j < 0 || i >= land.length || j >= land[i].length || 0 === land[i][j]) {
            return;
        }

        land[i][j] = 0;  // Mark the current cell as visited.

        // Update the bottom row and column indices.
        if (i > bottomRow) {
            bottomRow = i;
        }
        if (j > bottomCol) {
            bottomCol = j;
        }

        // Continue the search in the right and bottom cells.
        dfs(i + 1, j);
        dfs(i, j + 1);
    };

    // Iterate over the cells of the grid.
    for (let i = 0; i < land.length; i++) {
        for (let j = 0; j < land[i].length; j++) {
            // If the current cell is farmland, perform a depth-first search.
            if (1 === land[i][j]) {
                dfs(i, j);
                // Add the farmland to the result list.
                result.push([i, j, bottomRow, bottomCol]);
                // Reset the bottom row and column indices.
                bottomRow = 0;
                bottomCol = 0;
            }
        }
    }

    // Return the result list.
    return result;
};
