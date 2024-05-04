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
 *   Return the second largest number in the array.
 *   @param {Number[]} nums - An array of numbers.
 *   @return {Number} The second largest number in the array.
 **/
function getSecondLargest(nums) {
    // Initialize the largest and second largest numbers
    let largest = nums[0];
    let secondLargest = nums[0];

    // Iterate over the array
    for (let i = 1; i < nums.length; i++) {
        // If the current number is larger than the largest, update the largest and second largest
        if (nums[i] > largest) {
            secondLargest = largest;
            largest = nums[i];
        }
            // If the current number is smaller than the largest but larger than the second largest, update the second
        // largest
        else if (nums[i] > secondLargest && nums[i] < largest) {
            secondLargest = nums[i];
        }
    }

    // Return the second largest number
    return secondLargest;
}

/**
 * The main function to execute the program
 */
function main() {
    // Read the number of elements in the array
    const n = +readLine();

    // Read the array
    const nums = readLine().split(" ").map(Number);

    // Print the second largest number in the array
    console.log(getSecondLargest(nums));
}
