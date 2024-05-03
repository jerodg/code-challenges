/**
 * @file This module contains a function to find the minimum falling path sum in a grid.
 * @module leet_code/1289
 */

/**
 * Finds the minimum falling path sum in a grid.
 *
 * This function uses dynamic programming to find the minimum falling path sum in a grid.
 * It iterates over the grid, maintaining a tabulation of the minimum path sum to each cell.
 * For each cell, it considers the minimum path sum to the cells above it and adds the value of the current cell.
 * It then updates the tabulation with the minimum path sum to the current cell.
 *
 * @param {number[][]} grid - The grid of numbers. It is expected to be a 2D array of numbers.
 * @returns {number} The minimum falling path sum in the grid.
 *
 * @throws {TypeError} If the input is not a 2D array of numbers.
 */
function minFallingPathSum(grid: number[][]): number {
    if (!Array.isArray(grid) || !grid.every(row => Array.isArray(row) && row.every(cell => typeof cell === 'number'))) {
        throw new TypeError('Input must be a 2D array of numbers');
    }

    const rowCount: number = grid.length, colCount: number = grid[0].length;
    let retVal: number = Infinity;

    const tabulation_3 = () => {
        if (rowCount === 1) {
            retVal = grid[0][0];
            return;
        }

        let a = 0, b = 1, c = grid[0][a], d = grid[0][b];
        if (d < c) {
            [a, b, c, d] = [b, a, d, c];
        }

        for (let f = 2; f < colCount; f++) {
            if (grid[0][f] < c) {
                [b, a, d, c] = [a, f, c, grid[0][f]];
            } else if (grid[0][f] < d) {
                [b, d] = [f, grid[0][f]];
            }
        }

        for (let i = 1; i < rowCount; i++) {
            let u = 0, v = 1;
            let w = (0 === a ? d : c) + grid[i][0], x = (1 === a ? d : c) + grid[i][1];
            if (x < w) {
                [u, v, w, x] = [v, u, x, w];
            }

            for (let j = 2; j < colCount; j++) {
                const z = (j === a ? d : c) + grid[i][j];
                if (z < w) {
                    [v, u, x, w] = [u, j, w, z];
                } else if (z < x) {
                    [v, x] = [j, z];
                }
            }
            [a, b, c, d] = [u, v, w, x];
        }
        retVal = c;
    };

    tabulation_3();

    return retVal;
}
