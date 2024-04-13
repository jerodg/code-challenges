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
 * Function to calculate the factorial of a number
 *
 * @param {number} n - The number to calculate the factorial of.
 * @returns {number} - The factorial of the number.
 */
function factorial(n) {
    // Base case: if n is 0, return 1
    if (0 === n) {
        return 1;
    }
    // Recursive case: return n times the factorial of n - 1
    return n * factorial(n - 1);
}

/**
 * The main function to execute the program
 */
function main() {
    const n = +readLine();

    console.log(factorial(n));
}
