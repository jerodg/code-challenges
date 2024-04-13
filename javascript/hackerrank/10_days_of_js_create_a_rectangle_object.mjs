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
 * Rectangle constructor function
 *
 * @param {number} a - The length of the rectangle.
 * @param {number} b - The width of the rectangle.
 */
function Rectangle(a, b) {
    // Length of the rectangle
    this.length = a;
    // Width of the rectangle
    this.width = b;
    // Perimeter of the rectangle
    this.perimeter = 2 * (a + b);
    // Area of the rectangle
    this.area = a * b;
}

/**
 * The main function to execute the program
 */
function main() {
    const a = +readLine();
    const b = +readLine();

    // Create a new Rectangle object
    const rec = new Rectangle(a, b);

    // Log the properties of the Rectangle object
    console.log(rec.length);
    console.log(rec.width);
    console.log(rec.perimeter);
    console.log(rec.area);
}
