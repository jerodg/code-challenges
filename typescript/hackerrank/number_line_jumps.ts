import {createWriteStream, WriteStream} from "fs";

/**
 * @fileoverview This module contains a solution for the "Number Line Jumps" problem from HackerRank.
 * The problem is solved by checking if the kangaroos meet on a jump.
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

/**
 * Reads a line from the input.
 * @return {string} The next line from the input.
 */
function readLine(): string {
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
function kangaroo(x1: number, v1: number, x2: number, v2: number): string {
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
    const ws: WriteStream = createWriteStream(process.env["OUTPUT_PATH"]);
    const firstMultipleInput: string[] = readLine().replace(/\s+$/g, "").split(" ");
    const x1: number = parseInt(firstMultipleInput[0], 10);
    const v1: number = parseInt(firstMultipleInput[1], 10);
    const x2: number = parseInt(firstMultipleInput[2], 10);
    const v2: number = parseInt(firstMultipleInput[3], 10);
    const result: string = kangaroo(x1, v1, x2, v2);

    ws.write(result + "\n");
    ws.end();
}
