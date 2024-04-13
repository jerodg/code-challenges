/**
 * @fileoverview This module provides a function to calculate the maximal rectangle in a binary matrix.
 * @author jerodg
 */
/**
 * Calculates the maximal rectangle in a binary matrix.
 * The function uses dynamic programming to calculate the maximum height, left, and right boundary for each cell in the matrix.
 * The maximum area of the rectangle is then calculated as the height times the difference between the right and left boundaries.
 * This is done for each cell in the matrix, and the maximum area is updated if a larger area is found.
 * @param {string[][]} matrix - The input binary matrix.
 * @return {number} The area of the maximal rectangle.
 */
function maximalRectangle(matrix) {
    // Early return if the matrix is empty
    if (matrix.length === 0 || matrix[0].length === 0)
        return 0;
    var rows = matrix.length;
    var cols = matrix[0].length;
    var maxArea = 0;
    // Initialize arrays to store the maximum height and the left and right boundaries for each cell
    var left = new Array(cols).fill(0);
    var right = new Array(cols).fill(cols);
    var height = new Array(cols).fill(0);
    // Iterate over each cell in the matrix
    for (var i = 0; i < rows; i++) {
        var curLeft = 0, curRight = cols;
        for (var j = 0; j < cols; j++) {
            // If the cell is '1', increment the height and update the left boundary
            if (matrix[i][j] === "1") {
                height[j]++;
                left[j] = Math.max(left[j], curLeft);
            }
            else {
                // If the cell is '0', reset the height and left boundary, and update curLeft for the next cell
                height[j] = 0;
                left[j] = 0;
                curLeft = j + 1;
            }
        }
        // Iterate from right to left to update the right boundaries
        for (var j = cols - 1; j >= 0; j--) {
            if (matrix[i][j] === "1") {
                right[j] = Math.min(right[j], curRight);
            }
            else {
                right[j] = cols;
                curRight = j;
            }
        }
        // Calculate the maximum area for each cell
        for (var j = 0; j < cols; j++) {
            maxArea = Math.max(maxArea, (right[j] - left[j]) * height[j]);
        }
    }
    // Return the maximum area
    return maxArea;
}
