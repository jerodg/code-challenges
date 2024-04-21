/**
 * @fileoverview This module provides a function to find farmland in a given land matrix.
 * @module leet_code/1992
 */
/**
 * Function to find farmland in a given land matrix.
 * The function uses a depth-first search approach to traverse the land matrix.
 *
 * @param {number[][]} land - The land matrix where 0 represents water and 1 represents farmland.
 * @returns {number[][]} - The coordinates of the farmland in the format [top-left-x, top-left-y, bottom-right-x, bottom-right-y].
 * @throws {Error} - Throws an error if the input parameter is not valid.
 */
function findFarmland(land) {
    // Output array to store the coordinates of the farmland
    var output = [];
    // Variables to store the coordinates of the top-left and bottom-right corners of the farmland
    var topX = 0;
    var topY = 0;
    var lastX = 0;
    var lastY = 0;
    /**
     * Helper function to perform depth-first search on the land matrix.
     *
     * @param {number} row - The current row.
     * @param {number} col - The current column.
     */
    var traverse = function (row, col) {
        // Check if the current position is valid
        if (row < 0 || row >= land.length || col < 0 || col >= land[0].length) {
            return;
        }
        // Check if the current position is water
        if (land[row][col] === 0) {
            return;
        }
        // Update the coordinates of the top-left and bottom-right corners of the farmland
        topX = topX < row ? topX : row;
        topY = topY < col ? topY : col;
        lastX = lastX > row ? lastX : row;
        lastY = lastY > col ? lastY : col;
        // Mark the current position as visited
        land[row][col] = 0;
        // Recurse on the adjacent positions
        traverse(row - 1, col);
        traverse(row + 1, col);
        traverse(row, col - 1);
        traverse(row, col + 1);
    };
    // Traverse the land matrix
    for (var row = 0; row < land.length; row += 1) {
        for (var col = 0; col < land[0].length; col += 1) {
            // Check if the current position is farmland
            if (land[row][col] === 1) {
                // Initialize the coordinates of the top-left and bottom-right corners of the farmland
                topX = row;
                topY = col;
                lastX = row;
                lastY = col;
                // Start the depth-first search from the current position
                traverse(row, col);
                // Add the coordinates of the farmland to the output array
                output.push([topX, topY, lastX, lastY]);
            }
        }
    }
    // Return the output array
    return output;
}
