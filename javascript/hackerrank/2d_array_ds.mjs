"use strict";

// Import the 'fs' module for file system operations
const fs = require("fs");

// Set up the input stream for reading input data
process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

// Event listener for data input
process.stdin.on("data", inputStdin => {
    inputString += inputStdin;
});

// Event listener for end of data input
process.stdin.on("end", () => {
    inputString = inputString.split("\n");

    main();
});

/**
 * Function to read a line of input
 *
 * @returns {string} - A line of input
 */
function readLine() {
    return inputString[currentLine++];
}

/**
 * The 'hourglassSum' function calculates the maximum hourglass sum in a 2D array.
 *
 * @param {number[][]} arr - The 2D array.
 * @returns {number} - The maximum hourglass sum.
 */
function hourglassSum(arr) {
    // Initialize the maximum sum to the smallest possible number
    let maxSum = Number.MIN_SAFE_INTEGER;

    // Iterate over the array, skipping the first and last row
    for (let i = 1; i < 5; i++) {
        // Iterate over the array, skipping the first and last column
        for (let j = 1; j < 5; j++) {
            // Calculate the sum of the top of the hourglass
            let top = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1];

            // Get the middle of the hourglass
            let mid = arr[i][j];

            // Calculate the sum of the bottom of the hourglass
            let bottom = arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1];

            // Calculate the sum of the hourglass
            let hourglassSum = top + mid + bottom;

            // Update the maximum sum if the current hourglass sum is greater
            maxSum = Math.max(maxSum, hourglassSum);
        }
    }

    // Return the maximum sum
    return maxSum;
}

/**
 * The main function to execute the program
 */
function main() {
    // Create a write stream for output
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    // Initialize a 2D array
    let arr = Array(6);

    // Read input data into the 2D array
    for (let i = 0; i < 6; i++) {
        arr[i] = readLine().replace(/\s+$/g, "").split(" ").map(arrTemp => parseInt(arrTemp, 10));
    }

    // Calculate the maximum hourglass sum
    const result = hourglassSum(arr);

    // Write the result to the output
    ws.write(result + "\n");

    // Close the write stream
    ws.end();
}
