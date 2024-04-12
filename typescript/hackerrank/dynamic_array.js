"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs_1 = require("fs");
/**
 * @fileoverview This module contains a solution for the "Dynamic Array" problem from HackerRank.
 * The problem is solved using a dynamic array and bitwise XOR operation.
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
 * Solves the "Dynamic Array" problem from HackerRank.
 * @param {number} n - The number of sequences.
 * @param {number[][]} queries - The list of queries.
 * @return {number[]} The results of each type 2 query.
 */
function dynamicArray(n, queries) {
    var seqList = Array(n).fill(0).map(function () { return []; });
    var lastAnswer = 0;
    var result = [];
    // Iterate over the queries
    for (var i = 0; i < queries.length; i++) {
        var query = queries[i];
        var queryType = query[0];
        var x = query[1];
        var y = query[2];
        var seqIndex = (x ^ lastAnswer) % n;
        // If the query type is 1, append y to the seqIndex-th sequence
        if (queryType === 1) {
            seqList[seqIndex].push(y);
        }
        // If the query type is 2, find the y-th element of the seqIndex-th sequence, update lastAnswer and append it to the result
        else if (queryType === 2) {
            var seq = seqList[seqIndex];
            lastAnswer = seq[y % seq.length];
            result.push(lastAnswer);
        }
    }
    // Return the result
    return result;
}
/**
 * Main function that reads the input and writes the output.
 */
function main() {
    var ws = (0, fs_1.createWriteStream)(process.env["OUTPUT_PATH"]);
    var firstMultipleInput = readLine().replace(/\s+$/g, "").split(" ");
    var n = parseInt(firstMultipleInput[0], 10);
    var q = parseInt(firstMultipleInput[1], 10);
    var queries = Array(q);
    // Read the queries from the input
    for (var i = 0; i < q; i++) {
        queries[i] = readLine().replace(/\s+$/g, "").split(" ").map(function (queriesTemp) { return parseInt(queriesTemp, 10); });
    }
    // Call the dynamicArray function and write the result to the output
    var result = dynamicArray(n, queries);
    ws.write(result.join("\n") + "\n");
    ws.end();
}
