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
 * Function to count the total number of objects 'o' satisfying o.x == o.y.
 *
 * @param {Object[]} objects - An array of objects with integer properties 'x' and 'y'
 * @returns {number} - The count of objects where x equals y
 */
function getCount(objects) {
    let count = 0;

    // Iterate over the objects array
    for (let i = 0; i < objects.length; i++) {
        // Check if x equals y for the current object
        if (objects[i].x === objects[i].y) {
            count++;
        }
    }

    return count;
}

/**
 * The main function to execute the program
 */
function main() {
    const n = +readLine();
    let objects = [];

    // Create the objects array
    for (let i = 0; i < n; i++) {
        const [a, b] = readLine().split(" ");

        objects.push({x: +a, y: +b});
    }

    console.log(getCount(objects));
}
