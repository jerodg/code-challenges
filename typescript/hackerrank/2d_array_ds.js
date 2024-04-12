"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs_1 = require("fs");
/**
 * @fileoverview This module contains a solution for the "2D Array - DS" problem from HackerRank.
 * The problem is solved using a nested loop to iterate over the 2D array.
 */
process.stdin.resume();
process.stdin.setEncoding("utf-8");
var inputString = "";
var inputLines = [];
var currentLine = 0;
process.stdin.on("data", function (inputStdin) {
    inputString += inputStdin;
});
process.stdin.on("end", function () {
    inputLines = inputString.split("\n");
    inputString = "";
    main();
});
function readLine() {
    return inputLines[currentLine++];
}
/**
 * Function to calculate the maximum hourglass sum in a 2D array.
 * @param {number[][]} arr - The 2D array.
 * @return {number} The maximum hourglass sum.
 */
function hourglassSum(arr) {
    var maxSum = -63;
    // Iterate over the rows of the array
    for (var i = 0; i < 4; i++) {
        // Iterate over the columns of the array
        for (var j = 0; j < 4; j++) {
            // Calculate the sum of the current hourglass
            var sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2];
            // Update the maximum sum if the current sum is greater
            maxSum = Math.max(maxSum, sum);
        }
    }
    // Return the maximum hourglass sum
    return maxSum;
}
function main() {
    var ws = (0, fs_1.createWriteStream)(process.env["OUTPUT_PATH"]);
    var arr = Array(6);
    for (var i = 0; i < 6; i++) {
        arr[i] = readLine().replace(/\s+$/g, "").split(" ").map(function (arrTemp) { return parseInt(arrTemp, 10); });
    }
    var result = hourglassSum(arr);
    ws.write(result + "\n");
    ws.end();
}
