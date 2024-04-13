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
 * Function to create a regular expression that matches a string that starts and ends with the same vowel
 *
 * @returns {RegExp} - The regular expression
 */
function regexVar() {
    // The regular expression matches a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
    return /^([aeiou]).*\1$/;
}

/**
 * The main function to execute the program
 */
function main() {
    const re = regexVar();
    const s = readLine();

    console.log(re.test(s));
}
