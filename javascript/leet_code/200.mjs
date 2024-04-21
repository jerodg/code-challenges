/**
 * @fileoverview This module provides a function to count the number of islands in a 2D grid.
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 * The grid is represented as a 2D array where 0 represents water and 1 represents land.
 */

/**
 * Counts the number of islands in a 2D grid.
 *
 * @param {string[][]} grid - The 2D grid representation of the map.
 * @return {number} The number of islands in the grid.
 *
 * @throws {TypeError} If the input grid is not a 2D array.
 */
const numIslands = function (grid) {
    // Validate the input grid.
    if (!Array.isArray(grid) || !Array.isArray(grid[0])) {
        throw new TypeError('The input grid must be a 2D array.');
    }

    let islands = 0;  // Initialize the island counter.

    /**
     * Performs a depth-first search on the grid to find all islands.
     * @param {number} r - The current row index.
     * @param {number} c - The current column index.
     */
    const dfs = (r, c) => {
        // If the current cell is out of the grid or is water, return.
        if (r >= grid.length || 0 > r || c >= grid[0].length || c < 0 || "0" === grid[r][c]) {
            return;
        }

        grid[r][c] = "0";  // Mark the current cell as visited.

        // Continue the search in the top, bottom, left, and right cells.
        dfs(r - 1, c);
        dfs(r + 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1);
    };

    // Iterate over the cells of the grid.
    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[0].length; c++) {
            // If the current cell is land, perform a depth-first search and increment the island counter.
            if ("1" === grid[r][c]) {
                islands += 1;
                dfs(r, c);
            }
        }
    }

    // Return the number of islands.
    return islands;
};
