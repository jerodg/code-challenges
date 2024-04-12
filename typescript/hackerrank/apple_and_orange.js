"use strict";
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
 * Complete the 'countApplesAndOranges' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER s
 *  2. INTEGER t
 *  3. INTEGER a
 *  4. INTEGER b
 *  5. INTEGER_ARRAY apples
 *  6. INTEGER_ARRAY oranges
 */
function countApplesAndOranges(s, t, a, b, apples, oranges) {
    var appleCount = 0;
    var orangeCount = 0;
    for (var i = 0; i < apples.length; i++) {
        var apple = apples[i];
        var applePosition = a + apple;
        if (applePosition >= s && applePosition <= t) {
            appleCount++;
        }
    }
    for (var i = 0; i < oranges.length; i++) {
        var orange = oranges[i];
        var orangePosition = b + orange;
        if (orangePosition >= s && orangePosition <= t) {
            orangeCount++;
        }
    }
    console.log(appleCount);
    console.log(orangeCount);
}
function main() {
    var firstMultipleInput = readLine().replace(/\s+$/g, "").split(" ");
    var s = parseInt(firstMultipleInput[0], 10);
    var t = parseInt(firstMultipleInput[1], 10);
    var secondMultipleInput = readLine().replace(/\s+$/g, "").split(" ");
    var a = parseInt(secondMultipleInput[0], 10);
    var b = parseInt(secondMultipleInput[1], 10);
    var thirdMultipleInput = readLine().replace(/\s+$/g, "").split(" ");
    var m = parseInt(thirdMultipleInput[0], 10);
    var n = parseInt(thirdMultipleInput[1], 10);
    var apples = readLine().replace(/\s+$/g, "").split(" ").map(function (applesTemp) { return parseInt(applesTemp, 10); });
    var oranges = readLine().replace(/\s+$/g, "").split(" ").map(function (orangesTemp) { return parseInt(orangesTemp, 10); });
    countApplesAndOranges(s, t, a, b, apples, oranges);
}
