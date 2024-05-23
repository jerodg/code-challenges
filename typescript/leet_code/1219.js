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
 * This file contains the implementation of the `getMaximumGold` function and its helper functions.
 * The `getMaximumGold` function calculates the maximum amount of gold that can be collected from a grid.
 */
/**
 * The maximum amount of gold collected so far.
 */
var maxCount = 0;
/**
 * The possible x-directions to move in the grid.
 */
var xDirection = [0, 1, 0, -1];
/**
 * The possible y-directions to move in the grid.
 */
var yDirection = [-1, 0, 1, 0];
/**
 * Function to check if all cells in the grid have non-zero values.
 *
 * @param {number[][]} grid - The grid represented as a 2D array of numbers.
 * @returns {number} - The sum of all cell values if all cells have non-zero values, 0 otherwise.
 */
function hasNonZerosInMatrix(grid) {
    var result = 0;
    for (var y = 0; y < grid.length; ++y) {
        for (var x = 0; x < grid[y].length; ++x) {
            if (grid[y][x] > 0) {
                result += grid[y][x];
            }
            else {
                return 0;
            }
        }
    }
    return result;
}
/**
 * Function to calculate the maximum amount of gold that can be collected from a grid.
 *
 * @param {number[][]} grid - The grid represented as a 2D array of numbers.
 * @returns {number} - The maximum amount of gold that can be collected.
 */
function getMaximumGold(grid) {
    var temp = hasNonZerosInMatrix(grid);
    if (temp > 0) {
        return temp;
    }
    maxCount = 0;
    for (var y = 0; y < grid.length; ++y) {
        for (var x = 0; x < grid[y].length; ++x) {
            if (grid[y][x] > 0) {
                backtrack(grid, x, y, 0);
            }
        }
    }
    return maxCount;
}
/**
 * Recursive helper function to explore all possible paths in the grid.
 *
 * @param {number[][]} grid - The grid represented as a 2D array of numbers.
 * @param {number} x - The current x-coordinate.
 * @param {number} y - The current y-coordinate.
 * @param {number} count - The current amount of gold collected.
 */
function backtrack(grid, x, y, count) {
    if (x < 0 || y < 0 || x >= grid[0].length || y >= grid.length) {
        return;
    }
    if (grid[y][x] > 0) {
        var temp = grid[y][x];
        grid[y][x] = 0;
        count += temp;
        maxCount = count > maxCount ? count : maxCount;
        for (var i = 0; i < 4; ++i) {
            backtrack(grid, x + xDirection[i], y + yDirection[i], count);
        }
        grid[y][x] = temp;
    }
}
/**
 * Function to print the grid.
 *
 * @param {number[][]} grid - The grid represented as a 2D array of numbers.
 */
function print(grid) {
    console.log();
    for (var y = 0; y < grid.length; ++y) {
        console.log(grid[y].join(' '));
    }
}
