'use strict';

import {createWriteStream, WriteStream} from "fs";

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on('data', function (inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function (): void {
    inputLines = inputString.split('\n');
    inputString = '';

    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

/*
 * Complete the 'dynamicArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

function dynamicArray(n: number, queries: number[][]): number[] {
    let seqList: number[][] = Array(n).fill(0).map(() => []);
    let lastAnswer: number = 0;
    let result: number[] = [];
    for (let i: number = 0; i < queries.length; i++) {
        let query: number[] = queries[i];
        let queryType: number = query[0];
        let x: number = query[1];
        let y: number = query[2];
        let seqIndex: number = (x ^ lastAnswer) % n;
        if (queryType === 1) {
            seqList[seqIndex].push(y);
        } else if (queryType === 2) {
            let seq: number[] = seqList[seqIndex];
            lastAnswer = seq[y % seq.length];
            result.push(lastAnswer);
        }
    }
    return result;
}

function main() {
    const ws: WriteStream = createWriteStream(process.env['OUTPUT_PATH']);

    const firstMultipleInput: string[] = readLine().replace(/\s+$/g, '').split(' ');

    const n: number = parseInt(firstMultipleInput[0], 10);

    const q: number = parseInt(firstMultipleInput[1], 10);

    let queries: number[][] = Array(q);

    for (let i: number = 0; i < q; i++) {
        queries[i] = readLine().replace(/\s+$/g, '').split(' ').map(queriesTemp => parseInt(queriesTemp, 10));
    }

    const result: number[] = dynamicArray(n, queries);

    ws.write(result.join('\n') + '\n');

    ws.end();
}
