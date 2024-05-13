/**
 * @fileoverview This module contains a function that calculates the maximum score after flipping.
 * The function takes a binary matrix grid as input and returns the maximum score.
 *
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
 * Calculates the maximum score after flipping.
 *
 * The function first calculates the initial score assuming all rows have been flipped such that their first element is
 * 1. Then, for each column starting from the second, it counts the number of 1s in the column (considering that rows
 * can be flipped). The score of the column is the maximum between the number of 1s and the number of 0s (since we can
 * flip the entire column if it contains more 0s than 1s), multiplied by the column's weight. The column's weight is a
 * power of 2, decreasing from left to right. The function finally returns the total score.
 *
 * @param {number[][]} grid - A m x n binary matrix.
 * @returns {number} The maximum score after flipping.
 */
const matrixScore = function (grid) {
    let m = grid.length;
    let n = grid[0].length;
    let res = Math.pow(2, n - 1) * m;

    for (let j = 1; j < n; j++) {
        let curr = 0;

        for (let i = 0; i < m; i++) {
            curr += grid[i][0] === grid[i][j] ? 1 : 0;
        }
        res += Math.max(curr, m - curr) * Math.pow(2, n - 1 - j);
    }
    return res;
};
