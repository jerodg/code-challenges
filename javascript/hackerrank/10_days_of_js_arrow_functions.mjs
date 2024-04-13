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
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 *
 * @param {number[]} nums - An array of numbers.
 * @returns {number[]} - The modified array.
 */
function modifyArray(nums) {
    // Use the map function to iterate over the array and modify the elements
    return nums.map(n => 0 === n % 2 ? n * 2 : n * 3);
}

/**
 * The main function to execute the program
 */
function main() {
    // Read the number of elements in the array
    const n = +readLine();

    // Read the array
    const a = readLine().split(" ").map(Number);

    // Print the modified array
    console.log(modifyArray(a).toString().split(",").join(" "));
}
