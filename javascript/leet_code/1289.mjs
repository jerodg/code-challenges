/**
 * @fileoverview This module provides a function to calculate the minimum falling path sum in a matrix.
 * A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right.
 * Specifically, the index difference between two consecutive rows' elements is at most one.
 * This function uses dynamic programming to keep track of the minimum sum of the falling path up to each element.
 */

/**
 * Calculates the minimum falling path sum in a matrix.
 *
 * @param {number[][]} matrix - The input matrix. It is expected to be a 2D array of numbers.
 * @returns {number} - The minimum falling path sum in the matrix.
 */
const minFallingPathSum = function (matrix) {
    // If the matrix only has one element, return that element
    if (matrix.length === 1) {
        return matrix[0][0];
    }

    // Initialize the minimum first and second values and the position of the first value
    let minFst = 0, minSnd = 0, fstPos = -1;

    // Iterate over each row in the matrix
    for (let i = 0; i < matrix.length; i++) {
        // Initialize the next minimum first and second values and the position of the first value
        let nextFst = Infinity, nextSnd = Infinity, nextPos = -1;

        // Iterate over each element in the row
        for (let j = 0; j < matrix[0].length; j++) {
            // Calculate the value of the falling path ending at the current element
            const val = matrix[i][j] + (j === fstPos ? minSnd : minFst);

            // Update the next minimum first and second values and the position of the first value
            if (nextFst >= val) {
                nextSnd = nextFst;
                nextFst = val;
                nextPos = j;
            } else if (nextSnd > val) {
                nextSnd = val;
            }
        }

        // Update the minimum first and second values and the position of the first value
        minFst = nextFst;
        minSnd = nextSnd;
        fstPos = nextPos;
    }

    // Return the minimum falling path sum
    return minFst;
};
