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
 * This file `1293.mjs` contains a function `shortestPath` that calculates the shortest path in a grid from the
 * top-left cell to the bottom-right cell. The grid is represented as a 2D array of numbers, where each number
 * represents whether a cell is an obstacle (1) or not (0). The function uses breadth-first search (BFS) to find the
 * shortest path. The path can go through up to `k` obstacles.
 */

/**
 * Function to calculate the shortest path in a grid from the top-left cell to the bottom-right cell.
 *
 * @param {number[][]} grid - The grid represented as a 2D array of numbers.
 * @param {number} k - The maximum number of obstacles that the path can go through.
 * @returns {number} - The length of the shortest path, or -1 if no path exists.
 */
function shortestPath(grid, k) {
    // The number of rows and columns in the grid.
    const rows = grid.length;
    const cols = grid[0].length;

    // Initialize the queue with the top-left cell.
    // Each cell in the queue is represented as a tuple (row, col, steps, remaining k).
    const queue = [[0, 0, 0, k]];

    // Initialize the visited array with -1.
    // visited[i][j] represents the maximum remaining k after reaching the cell (i, j).
    const visited = Array.from({length: rows}, () => Array(cols).fill(-1));

    // The four possible directions to move in the grid.
    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    // Use BFS to find the shortest path.
    while (queue.length > 0) {
        const [row, col, steps, remainingK] = queue.shift();

        // If the bottom-right cell is reached, return the number of steps.
        if (row === rows - 1 && col === cols - 1) {
            return steps;
        }

        // Visit all adjacent cells.
        for (const [dr, dc] of directions) {
            const newRow = row + dr;
            const newCol = col + dc;

            // If the cell is inside the grid.
            if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
                // If the cell is an obstacle, decrease the remaining k.
                const currentObstacle = grid[newRow][newCol];
                const newK = remainingK - currentObstacle;

                // If the remaining k is non-negative and is greater than the maximum remaining k after visiting the
                // cell before, visit the cell.
                if (newK >= 0 && (visited[newRow][newCol] === -1 || visited[newRow][newCol] < newK)) {
                    visited[newRow][newCol] = newK;
                    queue.push([newRow, newCol, steps + 1, newK]);
                }
            }
        }
    }

    // If no path exists, return -1.
    return -1;
}
