import {createWriteStream, WriteStream} from "fs";

/**
 * @fileoverview This module contains a solution for the "2D Array - DS" problem from HackerRank.
 * The problem is solved using a nested loop to iterate over the 2D array.
 */

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString: string = "";
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on("data", function (inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on("end", function (): void {
    inputLines = inputString.split("\n");
    inputString = "";

    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

/**
 * Function to calculate the maximum hourglass sum in a 2D array.
 * @param {number[][]} arr - The 2D array.
 * @return {number} The maximum hourglass sum.
 */
function hourglassSum(arr: number[][]): number {
    let maxSum: number = -63;
    // Iterate over the rows of the array
    for (let i: number = 0; i < 4; i++) {
        // Iterate over the columns of the array
        for (let j: number = 0; j < 4; j++) {
            // Calculate the sum of the current hourglass
            let sum: number = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2];
            // Update the maximum sum if the current sum is greater
            maxSum = Math.max(maxSum, sum);
        }
    }
    // Return the maximum hourglass sum
    return maxSum;
}

function main() {
    const ws: WriteStream = createWriteStream(process.env["OUTPUT_PATH"]);

    let arr: number[][] = Array(6);

    for (let i: number = 0; i < 6; i++) {
        arr[i] = readLine().replace(/\s+$/g, "").split(" ").map(arrTemp => parseInt(arrTemp, 10));
    }

    const result: number = hourglassSum(arr);

    ws.write(result + "\n");

    ws.end();
}
