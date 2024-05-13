/**
 * Copyright ©2012-2024 JerodG <https://github.com/jerodg/>
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
 * program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 */

/**
 * Function to calculate the maximum binary matrix score.
 *
 * @param grid - A 2D array of numbers representing a binary matrix.
 * @returns The maximum score that can be achieved by flipping the matrix.
 *
 * The function works by first flipping all rows that start with 0, then counts the number of 0s in each column.
 * The score is calculated by adding the maximum of either the count of 0s or the total rows minus the count of 0s,
 * multiplied by 2 to the power of the number of columns minus the current column index minus 1, to the initial score.
 * The initial score is calculated as the number of rows multiplied by 2 to the power of the number of columns minus 1.
 */
function matrixScore(grid: number[][]): number {
    const rows: number = grid.length;
    const cols: number = grid[0].length;

    // Flip all rows that start with 0
    for (let r = 0; r < rows; r++) {
        if (grid[r][0] === 0) {
            for (let c = 0; c < cols; c++) {
                grid[r][c] = 1 - grid[r][c];
            }
        }
    }

    // Count the number of 0s in each column
    const counts: Map<number, number> = new Map();
    for (let c = 1; c < cols; c++) {
        for (let r = 0; r < rows; r++) {
            if (grid[r][c] === 0) {
                counts.set(c, (counts.get(c) || 0) + 1);
            }
        }
    }

    // Calculate the score
    let res: number = rows * Math.pow(2, cols - 1);
    for (let c = 1; c < cols; c++) {
        const count: number = counts.get(c) || 0;
        res += Math.max(count, rows - count) * Math.pow(2, cols - c - 1);
    }

    return res;
}
