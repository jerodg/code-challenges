/**
 * @fileoverview This module provides a function to calculate the maximal rectangle in a binary matrix.
 * @author jerodg
 */

/**
 * Calculates the maximal rectangle in a binary matrix.
 * @param {character[][]} matrix - A binary matrix.
 * @return {number} - The area of the maximal rectangle.
 */
function maximalRectangle(matrix) {
    // The number of rows in the matrix
    const rowLength = matrix.length;
    // The number of columns in the matrix
    const columnLength = matrix[0].length;
    // An array to keep track of the heights of the rectangles
    const heights = new Array(columnLength).fill(0);
    // Variable to keep track of the maximum area
    let maximumArea = 0;

    // Loop through each row in the matrix
    for (let rowIndex = 0; rowIndex < rowLength; rowIndex++) {
        // Loop through each column in the matrix
        for (let columnIndex = 0; columnIndex < columnLength; columnIndex++) {
            // If the current cell is '1', increase the height of the rectangle
            // Otherwise, reset the height to 0
            heights[columnIndex] = "1" === matrix[rowIndex][columnIndex] ? heights[columnIndex] + 1 : 0;
        }

        // Stack to keep track of the indices of the rectangles
        const stack = [];
        // Variable to keep track of the current index
        let heightIndex = 0;

        // While there are still rectangles to consider
        while (heightIndex < heights.length) {
            // If the stack is empty or the current rectangle is taller than the last rectangle in the stack
            if (0 === stack.length || heights[heightIndex] >= heights[stack[stack.length - 1]]) {
                // Add the current rectangle to the stack
                stack.push(heightIndex);
                heightIndex++;
            } else {
                // Calculate the area of the last rectangle in the stack
                const height = heights[stack.pop()];
                const isStackEmpty = 0 === stack.length;
                const width = isStackEmpty ? heightIndex : heightIndex - stack[stack.length - 1] - 1;
                maximumArea = Math.max(maximumArea, height * width);
            }
        }

        // While there are still rectangles in the stack
        while (0 !== stack.length) {
            // Calculate the area of the last rectangle in the stack
            const height = heights[stack.pop()];
            const isStackEmpty = 0 === stack.length;
            const width = isStackEmpty ? heightIndex : heightIndex - stack[stack.length - 1] - 1;
            maximumArea = Math.max(maximumArea, height * width);
        }
    }

    // Return the maximum area
    return maximumArea;
}
