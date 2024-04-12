"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs_1 = require("fs");
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
/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */
function hourglassSum(arr) {
    var maxSum = -63;
    for (var i = 0; i < 4; i++) {
        for (var j = 0; j < 4; j++) {
            var sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2];
            maxSum = Math.max(maxSum, sum);
        }
    }
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
