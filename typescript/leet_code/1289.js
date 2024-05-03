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
function minFallingPathSum(grid) {
    if (!Array.isArray(grid) || !grid.every(function (row) { return Array.isArray(row) && row.every(function (cell) { return typeof cell === 'number'; }); })) {
        throw new TypeError('Input must be a 2D array of numbers');
    }
    var rowCount = grid.length, colCount = grid[0].length;
    var retVal = Infinity;
    var tabulation_3 = function () {
        var _a, _b, _c, _d, _e, _f, _g;
        if (rowCount === 1) {
            retVal = grid[0][0];
            return;
        }
        var a = 0, b = 1, c = grid[0][a], d = grid[0][b];
        if (d < c) {
            _a = [b, a, d, c], a = _a[0], b = _a[1], c = _a[2], d = _a[3];
        }
        for (var f = 2; f < colCount; f++) {
            if (grid[0][f] < c) {
                _b = [a, f, c, grid[0][f]], b = _b[0], a = _b[1], d = _b[2], c = _b[3];
            }
            else if (grid[0][f] < d) {
                _c = [f, grid[0][f]], b = _c[0], d = _c[1];
            }
        }
        for (var i = 1; i < rowCount; i++) {
            var u = 0, v = 1;
            var w = (0 === a ? d : c) + grid[i][0], x = (1 === a ? d : c) + grid[i][1];
            if (x < w) {
                _d = [v, u, x, w], u = _d[0], v = _d[1], w = _d[2], x = _d[3];
            }
            for (var j = 2; j < colCount; j++) {
                var z = (j === a ? d : c) + grid[i][j];
                if (z < w) {
                    _e = [u, j, w, z], v = _e[0], u = _e[1], x = _e[2], w = _e[3];
                }
                else if (z < x) {
                    _f = [j, z], v = _f[0], x = _f[1];
                }
            }
            _g = [u, v, w, x], a = _g[0], b = _g[1], c = _g[2], d = _g[3];
        }
        retVal = c;
    };
    tabulation_3();
    return retVal;
}
