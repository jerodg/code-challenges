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
 *   Calculate the area of a rectangle.
 *
 *   @param {number} length - The length of the rectangle.
 *   @param {number} width - The width of the rectangle.
 *
 *   @returns {number} - The rectangle's area.
 **/
function getArea(length, width) {
    // Calculate the area
    return length * width;
}

/**
 *   Calculate the perimeter of a rectangle.
 *
 *   @param {number} length - The length of the rectangle.
 *   @param {number} width - The width of the rectangle.
 *
 *   @returns {number} - The perimeter of a rectangle.
 **/
function getPerimeter(length, width) {
    // Calculate the perimeter
    return 2 * (length + width);
}

/**
 * The main function to execute the program
 */
function main() {
    // Read the length and width
    const length = +readLine();
    const width = +readLine();

    // Print the area and perimeter
    console.log(getArea(length, width));
    console.log(getPerimeter(length, width));
}
