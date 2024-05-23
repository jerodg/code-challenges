/*
 *  Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 *  This program is free software: you can redistribute it and/or modify it under the terms of the
 *  Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 *  or (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 *  even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 *  for more details.
 *
 *  The above copyright notice and this permission notice shall be included in all copies or
 *  substantial portions of the Software. You should have received a copy of the SSPL along with this
 *  program. If not, see SSPL.
 */
/**
 * Package leet_code
 *
 * This file contains the implementation of the `minManhattanDistance` and `maximumSafenessFactor` functions.
 * The `minManhattanDistance` function calculates the minimum Manhattan distance from each cell in a grid to the
 * nearest obstacle. The `maximumSafenessFactor` function calculates the maximum safeness factor of a grid.
 */
/**
 * Function to calculate the minimum Manhattan distance from each cell in a grid to the nearest obstacle.
 *
 * @param {number[][]} grid - The grid represented as a 2D array of numbers.
 * @returns {number[][]} - A 2D array of numbers representing the minimum Manhattan distance from each cell to the
 *     nearest obstacle.
 */
function minManhattanDistance(grid) {
    var n = grid.length;
    var res = new Array(n);
    var INF = n * n; // A large number representing infinity
    for (var i = 0; i < n; i++) {
        res[i] = new Array(n).fill(INF); // Initialize the result array with infinity
    }
    // Calculate the minimum distance for each cell
    for (var i = 0; i < n; i++) {
        for (var j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                res[i][j] = 0; // If the cell is an obstacle, its distance is 0
            }
            else {
                var up = i > 0 ? res[i - 1][j] : INF; // Get the distance from the cell above
                var left = j > 0 ? res[i][j - 1] : INF; // Get the distance from the cell to the left
                res[i][j] = Math.min(res[i][j], 1 + Math.min(up, left)); // Update the distance for the current cell
            }
        }
    }
    // Repeat the process in reverse order to ensure all distances are correctly calculated
    for (var i = n - 1; i >= 0; i--) {
        for (var j = n - 1; j >= 0; j--) {
            if (grid[i][j] === 1) {
                continue; // If the cell is an obstacle, skip it
            }
            var down = i + 1 < n ? res[i + 1][j] : INF; // Get the distance from the cell below
            var right = j + 1 < n ? res[i][j + 1] : INF; // Get the distance from the cell to the right
            res[i][j] = Math.min(res[i][j], 1 + Math.min(down, right)); // Update the distance for the current cell
        }
    }
    return res; // Return the result array
}
/**
 * Function to calculate the maximum safeness factor of a grid.
 *
 * @param {number[][]} grid - The grid represented as a 2D array of numbers.
 * @returns {number} - The maximum safeness factor of the grid.
 *
 * The safeness factor of a cell is defined as the minimum Manhattan distance from the cell to the nearest obstacle.
 * The maximum safeness factor of a grid is defined as the maximum safeness factor of any cell in the grid.
 */
function maximumSafenessFactor(grid) {
    var n = grid.length;
    if (grid[0][0] === 1 || grid[n - 1][n - 1] === 1 || n === 1) {
        return 0; // If the grid has an obstacle at the corners or has only one cell, return 0
    }
    var minDist = minManhattanDistance(grid); // Calculate the minimum Manhattan distance for each cell
    // Helper function to check if a safeness factor is possible
    var isPossible = function (target) {
        if (minDist[0][0] < target) {
            return false; // If the safeness factor of the first cell is less than the target, return false
        }
        var visited = new Array(n);
        var dx = [0, 0, -1, 1]; // The change in x-coordinate for each direction
        var dy = [-1, 1, 0, 0]; // The change in y-coordinate for each direction
        for (var i = 0; i < n; i++) {
            visited[i] = new Array(n);
        }
        var curr = [{ row: 0, col: 0 }];
        visited[0][0] = true;
        while (curr.length > 0) {
            var ncurr = [];
            for (var _i = 0, curr_1 = curr; _i < curr_1.length; _i++) {
                var val = curr_1[_i];
                var r_1 = val.row, c = val.col;
                for (var i = 0; i < dx.length; i++) {
                    var nr = r_1 + dx[i];
                    var nc = c + dy[i];
                    if (0 <= nr && nr < n && 0 <= nc && nc < n && minDist[nr][nc] >= target && !visited[nr][nc]) {
                        if (nr === n - 1 && nc === n - 1) {
                            return true; // If we can reach the last cell, return true
                        }
                        visited[nr][nc] = true;
                        ncurr.push({ row: nr, col: nc });
                    }
                }
            }
            curr = ncurr;
        }
        return false; // If we cannot reach the last cell, return false
    };
    // Binary search for the maximum safeness factor
    var l = 0, r = n * n;
    var ans = r;
    while (l <= r) {
        var mid = l + Math.floor((r - l) / 2);
        if (isPossible(mid)) {
            ans = mid;
            l = mid + 1;
        }
        else {
            r = mid - 1;
        }
    }
    return ans; // Return the maximum safeness factor
}
