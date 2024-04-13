/*jshint bitwise: true */

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

// Event listener for data input
process.stdin.on("data", inputStdin => {
    inputString += inputStdin;
});

// Event listener for end of data input
process.stdin.on("end", _ => {
    inputString = inputString.trim().split("\n").map(string => {
        return string.trim();
    });

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
 * Function to get the maximum bitwise AND value less than K in the set {1,2,3,...,N}
 *
 * @param {number} n - The maximum number in the set.
 * @param {number} k - The maximum value for the bitwise AND operation.
 * @returns {number} - The maximum bitwise AND value less than K.
 */
function getMaxLessThanK(n, k) {
    let max = 0;
    for (let i = 1; i < n + 1; i++) {
        for (let j = i + 1; j < n + 1; j++) {
            let current = i & j;
            if (current > max && current < k) {
                max = current;
            }
        }
    }
    return max;
}

/**
 * The main function to execute the program
 */
function main() {
    const q = +readLine();

    for (let i = 0; i < q; i++) {
        const [n, k] = readLine().split(" ").map(Number);

        console.log(getMaxLessThanK(n, k));
    }
}
