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
 * Function to calculate the shortest path in a grid with obstacles.
 *
 * @param {number[][]} grid - The grid represented as a 2D array of numbers. Each cell in the grid is either 0 (free)
 *     or 1 (obstacle).
 * @param {number} k - The maximum number of obstacles that can be eliminated.
 * @returns {number} - The minimum number of steps to reach the bottom-right corner of the grid from the top-left
 *     corner. If it is not possible to reach the bottom-right corner, returns -1.
 *
 * The function uses dynamic programming and memoization to calculate the shortest path. It starts from the top-left
 *     corner of the grid and tries to move to the bottom-right corner. At each step, it can move to the right or down.
 *     If it encounters an obstacle, it can choose to eliminate it. The number of obstacles that can be eliminated is
 *     limited by the parameter `k`.
 */
function shortestPath(grid, k) {
    // If the number of obstacles that can be eliminated is greater than or equal to the sum of the dimensions of the
    // grid minus 2, return the sum of the dimensions of the grid minus 2.
    if (k >= grid.length + grid[0].length - 2) {
        return grid.length + grid[0].length - 2;
    }
    // Initialize the memoization table.
    var memo = {};
    // Define the possible directions to move in the grid.
    var direction = {
        '[-1,0]': [[0, 1], [-1, 0], [0, -1]],
        '[0,-1]': [[1, 0], [-1, 0], [0, -1]],
        '[1,0]': [[1, 0], [0, 1], [0, -1]],
        '[0,1]': [[1, 0], [0, 1], [-1, 0]],
    };
    // Define the dynamic programming function.
    var dp = function (x, y, power, possibleWay) {
        // If the current cell is out of the grid, return a large number.
        switch (x + y) {
            case y - 1:
            case x - 1:
            case grid.length + y:
            case grid[x].length + x:
                return 1601;
            // If the current cell is the bottom-right corner of the grid, return 1.
            case grid.length - 1 + grid[0].length - 1:
                if (x === grid.length - 1) {
                    return 1;
                }
            default:
                // If the current cell is an obstacle and the number of obstacles that can be eliminated is less than
                // the value of the cell, return a large number.
                if (grid[x][y] > power) {
                    return 1601;
                }
                // If the current cell has not been visited before, calculate the minimum number of steps to reach it.
                if (memo["".concat(x, ",").concat(y, "-").concat(power)] === undefined) {
                    memo["".concat(x, ",").concat(y, "-").concat(power)] = 1601;
                    for (var _i = 0, possibleWay_1 = possibleWay; _i < possibleWay_1.length; _i++) {
                        var direc = possibleWay_1[_i];
                        if (memo["".concat(x, ",").concat(y, "-").concat(power)] < 1601 && direc[0] + direc[1] === -1) {
                            break;
                        }
                        memo["".concat(x, ",").concat(y, "-").concat(power)] = Math.min(memo["".concat(x, ",").concat(y, "-").concat(power)], dp(x + direc[0], y + direc[1], power - grid[x][y], direction[JSON.stringify(direc)]));
                    }
                    memo["".concat(x, ",").concat(y, "-").concat(power)] += 1;
                }
                return memo["".concat(x, ",").concat(y, "-").concat(power)];
        }
    };
    // Calculate the minimum number of steps to reach the bottom-right corner of the grid.
    var res = dp(0, 0, k, [[0, 1], [1, 0]]);
    // If the minimum number of steps is greater than or equal to a large number, return -1. Otherwise, return the
    // minimum number of steps minus 1.
    return res >= 1601 ? -1 : res - 1;
}
