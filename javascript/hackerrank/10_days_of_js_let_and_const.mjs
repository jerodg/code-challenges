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
 * The main function to execute the program
 */
function main() {
    // Define the value of pi
    let pi = Math.PI;
    // Read the radius
    let r = readLine();
    // Print the area of the circle:
    console.log(pi * r * r);
    // Print the perimeter of the circle:
    console.log(2 * pi * r);

    try {
        // Attempt to redefine the value of constant variable PI
        pi = 0;
        // Attempt to print the value of PI
        console.log(pi);
    } catch (error) {
        console.error("You correctly declared 'PI' as a constant.");
    }
}
