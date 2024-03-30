'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

function hourglassSum(arr) {
    let maxSum = Number.MIN_SAFE_INTEGER;
    for (let i = 1; i < 5; i++) {
        for (let j = 1; j < 5; j++) {
            let top = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1];
            let mid = arr[i][j];
            let bottom = arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1];
            let hourglassSum = top + mid + bottom;
            maxSum = Math.max(maxSum, hourglassSum);
        }
    }
    return maxSum;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    let arr = Array(6);

    for (let i = 0; i < 6; i++) {
        arr[i] = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }

    const result = hourglassSum(arr);

    ws.write(result + '\n');

    ws.end();
}
