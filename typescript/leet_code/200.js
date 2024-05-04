/**
 * @fileoverview This module provides functions to count the number of islands in a grid.
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 * @module leet_code/200
 */
/**
 * Depth-first search function to mark the visited spots in the grid.
 *
 * @param {string[][]} grid - The 2D grid map of '1's (land) and '0's (water).
 * @param {number} i - The row index of the spot to start the search.
 * @param {number} j - The column index of the spot to start the search.
 * @returns {void} - This function does not return anything; it modifies the grid in-place.
 */
function dfs(grid, i, j) {
    if (i < 0 || i >= grid.length || j < 0 || j >= grid[i].length || grid[i][j] === '0') {
        return;
    }
    // Mark this spot as visited
    grid[i][j] = '0';
    // Continue the search in the four adjacent spots
    dfs(grid, i + 1, j);
    dfs(grid, i, j + 1);
    dfs(grid, i, j - 1);
    dfs(grid, i - 1, j);
}

/**
 * Function to count the number of islands in a grid.
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 *
 * @param {string[][]} grid - The 2D grid map of '1's (land) and '0's (water).
 * @returns {number} - The number of islands.
 */
function numIslands(grid) {
    var count = 0;
    for (var i = 0; i < grid.length; i++) {
        for (var j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === '1') {
                dfs(grid, i, j);
                count++;
            }
        }
    }
    return count;
}
