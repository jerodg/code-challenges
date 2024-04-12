"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs_1 = require("fs");
/**
 * @fileoverview This module contains a solution for the "Number Line Jumps" problem from HackerRank.
 * The problem is solved by checking if the kangaroos meet on a jump.
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
/**
 * Reads a line from the input.
 * @return {string} The next line from the input.
 */
function readLine() {
    return inputLines[currentLine++];
}
/**
 * Determines if the two kangaroos meet on a jump.
 * @param {number} x1 - The starting position of the first kangaroo.
 * @param {number} v1 - The jump distance of the first kangaroo.
 * @param {number} x2 - The starting position of the second kangaroo.
 * @param {number} v2 - The jump distance of the second kangaroo.
 * @return {string} "YES" if the kangaroos meet on a jump, "NO" otherwise.
 */
function kangaroo(x1, v1, x2, v2) {
    // If the first kangaroo jumps farther and the difference in starting positions is divisible by the difference in jump distances
    if (v1 > v2 && (x2 - x1) % (v1 - v2) === 0) {
        return "YES";
    }
    return "NO";
}
/**
 * Main function that reads the input and writes the output.
 */
function main() {
    var ws = (0, fs_1.createWriteStream)(process.env["OUTPUT_PATH"]);
    var firstMultipleInput = readLine().replace(/\s+$/g, "").split(" ");
    var x1 = parseInt(firstMultipleInput[0], 10);
    var v1 = parseInt(firstMultipleInput[1], 10);
    var x2 = parseInt(firstMultipleInput[2], 10);
    var v2 = parseInt(firstMultipleInput[3], 10);
    var result = kangaroo(x1, v1, x2, v2);
    ws.write(result + "\n");
    ws.end();
}
