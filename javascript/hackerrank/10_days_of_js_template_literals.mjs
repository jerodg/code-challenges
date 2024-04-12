"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", inputStdin => {
    inputString += inputStdin;
});

process.stdin.on("end", _ => {
    inputString = inputString.trim().split("\n").map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function sides(literals, ...expressions) {
    const a = expressions[0];
    const p = expressions[1];

    // Find s1 and s2 by plugging the area and perimeter values into the formula
    const s1 = (p + Math.sqrt(p ** 2 - 16 * a)) / 4;
    const s2 = (p - Math.sqrt(p ** 2 - 16 * a)) / 4;

    // Create an array consisting of s1 and s2, and sort it in ascending order
    const sortedSides = [s1, s2].sort((a, b) => a - b);

    return sortedSides;
}

function main() {
    let s1 = +(readLine());
    let s2 = +(readLine());

    [s1, s2] = [s1, s2].sort();

    const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;

    console.log((s1 === x) ? s1 : -1);
    console.log((s2 === y) ? s2 : -1);
}
