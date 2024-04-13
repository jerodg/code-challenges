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
 * Function to check if a number is positive, zero or negative
 *
 * @param {number} a - The number to check
 * @returns {string} - "YES" if the number is positive
 * @throws {Error} - If the number is zero or negative
 */
function isPositive(a) {
    if (0 === a) {
        throw new Error("Zero Error");
    } else if (0 > a) {
        throw new Error("Negative Error");
    } else {
        return "YES";
    }
}

/**
 * The main function to execute the program
 */
function main() {
    const n = +readLine();

    for (let i = 0; i < n; i++) {
        const a = +readLine();

        try {
            console.log(isPositive(a));
        } catch (e) {
            console.log(e.message);
        }
    }
}
