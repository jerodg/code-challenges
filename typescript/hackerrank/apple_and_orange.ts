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
 * @fileoverview This module contains a solution for the "Apple and Orange" problem from HackerRank.
 * The problem is solved by calculating the positions of the apples and oranges and checking if they fall within the house's
 *     location.
 */

/**
 * Function to count the number of apples and oranges that fall on Sam's house.
 * @param {number} s - The start point of Sam's house.
 * @param {number} t - The end point of Sam's house.
 * @param {number} a - The location of the apple tree.
 * @param {number} b - The location of the orange tree.
 * @param {number[]} apples - The distances at which each apple falls from the tree.
 * @param {number[]} oranges - The distances at which each orange falls from the tree.
 */
function countApplesAndOranges(s: number, t: number, a: number, b: number, apples: number[], oranges: number[]): void {
    let appleCount: number = 0;
    let orangeCount: number = 0;

    // Calculate the position of each apple and check if it falls on the house
    for (let i: number = 0; i < apples.length; i++) {
        let apple: number = apples[i];
        let applePosition: number = a + apple;
        if (applePosition >= s && applePosition <= t) {
            appleCount++;
        }
    }

    // Calculate the position of each orange and check if it falls on the house
    for (let i: number = 0; i < oranges.length; i++) {
        let orange: number = oranges[i];
        let orangePosition: number = b + orange;
        if (orangePosition >= s && orangePosition <= t) {
            orangeCount++;
        }
    }

    // Print the number of apples and oranges that fall on the house
    console.log(appleCount);
    console.log(orangeCount);
}

function main() {
    const firstMultipleInput: string[] = readLine().replace(/\s+$/g, "").split(" ");
    const s: number = parseInt(firstMultipleInput[0], 10);
    const t: number = parseInt(firstMultipleInput[1], 10);
    const secondMultipleInput: string[] = readLine().replace(/\s+$/g, "").split(" ");
    const a: number = parseInt(secondMultipleInput[0], 10);
    const b: number = parseInt(secondMultipleInput[1], 10);
    const thirdMultipleInput: string[] = readLine().replace(/\s+$/g, "").split(" ");
    const m: number = parseInt(thirdMultipleInput[0], 10);
    const n: number = parseInt(thirdMultipleInput[1], 10);
    const apples: number[] = readLine().replace(/\s+$/g, "").split(" ").map(applesTemp => parseInt(applesTemp, 10));
    const oranges: number[] = readLine().replace(/\s+$/g, "").split(" ").map(orangesTemp => parseInt(orangesTemp, 10));

    countApplesAndOranges(s, t, a, b, apples, oranges);
}
