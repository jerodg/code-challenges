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
 * This file `2812.mjs` contains a function `maximumSafenessFactor` that calculates the maximum safeness factor of a
 * grid. The safeness factor is defined as the minimum distance from a cell to a cell with a value of 1. The function
 * uses breadth-first search (BFS) to calculate the safeness factor for each cell in the grid.
 */

/**
 * The four possible directions to move in the grid.
 * @type {number[][]}
 */
let ADJ = [[-1, 0], [1, 0], [0, -1], [0, 1]];

/**
 * Function to calculate the maximum safeness factor of a grid.
 *
 * @param {number[][]} grid - The grid represented as a 2D array of numbers.
 * @returns {number} - The maximum safeness factor of the grid.
 */
const maximumSafenessFactor = function (grid) {
    // The width and height of the grid.
    let w = grid[0].length;
    let h = grid.length;

    // Initialize the queue with the cells that have a value of 1.
    let q = [];
    for (let i = 0; i < h; ++i) {
        for (let j = 0; j < w; ++j) {
            if (grid[i][j]) {
                q.push(i, j);
            }
        }
    }

    // Use BFS to calculate the safeness factor for each cell in the grid.
    let q2 = [];
    let dist = 2;
    while (q.length) {
        let j = q.pop();
        let i = q.pop();

        for (let offset of ADJ) {
            let i2 = i + offset[0];
            let j2 = j + offset[1];

            // If the cell is outside the grid or has a value of 1, skip it.
            if (i2 < 0 || j2 < 0 || i2 >= h || j2 >= w || grid[i2][j2]) {
                continue;
            }

            // Set the safeness factor of the cell and add it to the queue.
            grid[i2][j2] = dist;
            q2.push(i2, j2);
        }

        // If the queue is empty, swap the queues and increase the distance.
        if (!q.length) {
            [q2, q] = [q, q2];
            ++dist;
        }
    }

    // Initialize the queue with the top-left cell and set its safeness factor to negative.
    q = [0];
    let maxDist = grid[0][0] - 1;
    grid[0][0] *= -1;

    // Use BFS to find the maximum safeness factor.
    while (true) {
        let dpIdx = q.pop();
        let j = dpIdx % w;
        let i = Math.floor(dpIdx / w);

        let dist = -grid[i][j];

        // Update the maximum safeness factor.
        maxDist = Math.min(dist - 1, maxDist);

        // If the bottom-right cell is reached, return the maximum safeness factor.
        if (i === h - 1 && j === w - 1) {
            return maxDist;
        }

        // Visit all adjacent cells.
        for (let offset of ADJ) {
            let i2 = i + offset[0];
            let j2 = j + offset[1];

            // If the cell is outside the grid or has been visited, skip it.
            if (i2 < 0 || j2 < 0 || i2 >= h || j2 >= w || grid[i2][j2] < 0) {
                continue;
            }

            // Calculate the index of the cell in the DP table.
            let dpIdx = i2 * w + j2;

            // If the safeness factor of the cell is greater than or equal to the maximum safeness factor, add it to
            // the queue. Otherwise, add it to the secondary queue.
            if (grid[i2][j2] - 1 >= maxDist) {
                q.push(dpIdx);
            } else {
                q2.push(dpIdx);
            }

            // Mark the cell as visited by setting its safeness factor to negative.
            grid[i2][j2] *= -1;
        }

        // If the queue is empty, sort the secondary queue by the safeness factor and swap the queues.
        if (!q.length) {
            q2.sort((b, a) => {
                let j1 = a % w;
                let i1 = Math.floor(a / w);
                let j2 = b % w;
                let i2 = Math.floor(b / w);

                return grid[i1][j1] - grid[i2][j2];
            });

            // Find the index of the first cell in the secondary queue with a safeness factor less than the maximum
            // safeness factor.
            let set = false;
            let i;
            for (i = q2.length - 1; i >= 0; --i) {
                let j1 = q2[i] % w;
                let i1 = Math.floor(q2[i] / w);

                if (set) {
                    if (-grid[i1][j1] - 1 < maxDist) {
                        ++i;
                        break;
                    }
                } else {
                    if (-grid[i1][j1] - 1 >= maxDist) {
                        continue;
                    }
                    set = true;
                    maxDist = -grid[i1][j1] - 1;
                }
            }

            // Swap the queues and update the maximum safeness factor.
            i = Math.max(i, 0);
            q = q2.slice(i);
            q2.length = i;
        }
    }
};
