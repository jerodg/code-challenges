/**
 * Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see SSPL.
 */

/**
 * Package leet_code
 *
 * This file `1219.mjs` contains a function `getMaximumGold` that calculates the maximum amount of gold that can be
 * collected from a grid. The grid is represented as a 2D array of numbers, where each number represents the amount of
 * gold in a cell. The function uses depth-first search (DFS) to find the path that collects the maximum amount of
 * gold.
 */

/**
 * Function to calculate the maximum amount of gold that can be collected from a grid.
 *
 * @param {number[][]} grid - The grid represented as a 2D array of numbers.
 * @returns {number} - The maximum amount of gold that can be collected.
 */
const getMaximumGold = function (grid) {
    // Check if the grid contains a cell with a value of 0.
    const sum = isZeroPresent(grid);
    if (sum !== -1) {
        return sum;
    }

    // Initialize the maximum amount of gold that can be collected.
    let max = 0;

    // Iterate over each cell in the grid.
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            // Update the maximum amount of gold that can be collected.
            max = Math.max(max, maxPath(grid, i, j));
        }
    }

    // Return the maximum amount of gold that can be collected.
    return max;
};

/**
 * Function to check if the grid contains a cell with a value of 0.
 *
 * @param {number[][]} grid - The grid represented as a 2D array of numbers.
 * @returns {number} - The sum of the values in the grid if it does not contain a cell with a value of 0, -1 otherwise.
 */
const isZeroPresent = (grid) => {
    // Initialize the sum of the values in the grid.
    let sum = 0;

    // Iterate over each cell in the grid.
    for (const row of grid) {
        for (const val of row) {
            // If the cell has a value of 0, return -1.
            if (!val) {
                return -1;
            }

            // Update the sum of the values in the grid.
            sum += val;
        }
    }

    // Return the sum of the values in the grid.
    return sum;
};

/**
 * Function to calculate the maximum amount of gold that can be collected from a cell using DFS.
 *
 * @param {number[][]} grid - The grid represented as a 2D array of numbers.
 * @param {number} i - The row index of the cell.
 * @param {number} j - The column index of the cell.
 * @returns {number} - The maximum amount of gold that can be collected from the cell.
 */
const maxPath = (grid, i, j) => {
    // If the cell is outside the grid or has a value of 0, return 0.
    if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || !grid[i][j]) {
        return 0;
    }

    // Store the value of the cell and set it to 0 to mark it as visited.
    const val = grid[i][j];
    grid[i][j] = 0;

    // Calculate the maximum amount of gold that can be collected from the adjacent cells.
    const upPath = maxPath(grid, i, j - 1);
    const downPath = maxPath(grid, i, j + 1);
    const leftPath = maxPath(grid, i - 1, j);
    const rightPath = maxPath(grid, i + 1, j);

    // Restore the value of the cell.
    grid[i][j] = val;

    // Return the maximum amount of gold that can be collected from the cell.
    return val + Math.max(Math.max(upPath, downPath), Math.max(leftPath, rightPath));
};
