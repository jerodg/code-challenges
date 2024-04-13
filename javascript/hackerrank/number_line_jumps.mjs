const fs = require("fs");

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
 * Function to determine if two kangaroos can meet on a number line
 *
 * @param {number} x1 - The starting point of the first kangaroo
 * @param {number} v1 - The jump distance of the first kangaroo
 * @param {number} x2 - The starting point of the second kangaroo
 * @param {number} v2 - The jump distance of the second kangaroo
 * @returns {string} - "YES" if the kangaroos can meet, "NO" otherwise
 */
function kangaroo(x1, v1, x2, v2) {
    // If the first kangaroo jumps less distance than the second, they will never meet
    if (v1 <= v2) {
        return "NO";
    }

    // Calculate the number of jumps needed for the kangaroos to meet
    let jumpsToMeet = (x2 - x1) / (v1 - v2);

    // If the number of jumps is an integer and is not negative, the kangaroos can meet
    if (Number.isInteger(jumpsToMeet) && 0 <= jumpsToMeet) {
        return "YES";
    } else {
        return "NO";
    }
}

/**
 * The main function to execute the program
 */
function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const firstMultipleInput = readLine().replace(/\s+$/g, "").split(" ");
    const x1 = parseInt(firstMultipleInput[0], 10);
    const v1 = parseInt(firstMultipleInput[1], 10);
    const x2 = parseInt(firstMultipleInput[2], 10);
    const v2 = parseInt(firstMultipleInput[3], 10);
    const result = kangaroo(x1, v1, x2, v2);
    ws.write(result + "\n");
    ws.end();
}
