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
 * Complete the 'kangaroo' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. INTEGER x1
 *  2. INTEGER v1
 *  3. INTEGER x2
 *  4. INTEGER v2
 */
function kangaroo(x1, v1, x2, v2) {
    if (v1 > v2) {
        if ((x2 - x1) % (v1 - v2) === 0) {
            return "YES";
        }
    }
    return "NO";
}
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
