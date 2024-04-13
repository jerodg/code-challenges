process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

// Event listener for data input
process.stdin.on("data", function (inputStdin) {
    inputString += inputStdin;
});

// Event listener for end of data input
process.stdin.on("end", function () {
    inputString = inputString.split("\n");

    main();
});

/**
 * Function to read a line of input
 *
 * @returns {string} - A line of input
 */
function readLine() {
    return inputString[currentLine++];
}

/**
 * Function to count the number of apples and oranges that fall on Sam's house
 *
 * @param {number} s - The start point of Sam's house location.
 * @param {number} t - The end point of Sam's house location.
 * @param {number} a - The location of the Apple tree.
 * @param {number} b - The location of the Orange tree.
 * @param {number[]} apples - Distances at which each apple falls from the tree.
 * @param {number[]} oranges - Distances at which each orange falls from the tree.
 */
function countApplesAndOranges(s, t, a, b, apples, oranges) {
    const countInRange = (tree, fruits) => {
        return fruits.filter((fruit) => tree + fruit >= s && tree + fruit <= t).length;
    };
    console.log(countInRange(a, apples));
    console.log(countInRange(b, oranges));
}

/**
 * The main function to execute the program
 */
function main() {
    const firstMultipleInput = readLine().replace(/\s+$/g, "").split(" ");
    const s = parseInt(firstMultipleInput[0], 10);
    const t = parseInt(firstMultipleInput[1], 10);
    const secondMultipleInput = readLine().replace(/\s+$/g, "").split(" ");
    const a = parseInt(secondMultipleInput[0], 10);
    const b = parseInt(secondMultipleInput[1], 10);
    const thirdMultipleInput = readLine().replace(/\s+$/g, "").split(" ");
    const m = parseInt(thirdMultipleInput[0], 10);
    const n = parseInt(thirdMultipleInput[1], 10);
    const apples = readLine().replace(/\s+$/g, "").split(" ").map(applesTemp => parseInt(applesTemp, 10));
    const oranges = readLine().replace(/\s+$/g, "").split(" ").map(orangesTemp => parseInt(orangesTemp, 10));
    countApplesAndOranges(s, t, a, b, apples, oranges);
}
