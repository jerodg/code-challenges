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
 * Function to reverse a string
 *
 * @param {string} s - The string to reverse
 * @throws {Error} - If the input is not a string
 */
function reverseString(s) {
    try {
        // Attempt to reverse the string
        console.log(s.split("").reverse().join(""));
    } catch (e) {
        // Log the error message if the input is not a string
        console.log(e.message);
        // Log the original input
        console.log(s);
    }
}

/**
 * The main function to execute the program
 */
function main() {
    const s = eval(readLine());

    reverseString(s);
}
