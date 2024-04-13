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
 * Function to create a regular expression that matches all occurrences of digits in a given string
 *
 * @returns {RegExp} - The regular expression
 */
function regexVar() {
    // The regular expression matches all occurrences of digits in a given string
    return new RegExp("\\d+", "g");
}

/**
 * The main function to execute the program
 */
function main() {
    const re = regexVar();
    const s = readLine();

    const r = s.match(re);

    // Print all the matches
    for (const e of r) {
        console.log(e);
    }
}
