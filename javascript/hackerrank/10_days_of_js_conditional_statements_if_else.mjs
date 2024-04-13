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
 * Function to get the grade based on the score
 *
 * @param {number} score - The score.
 * @returns {string} - The grade.
 */
function getGrade(score) {
    let grade;
    // Determine the grade based on the score
    if (25 < score && 30 >= score) {
        grade = "A";
    } else if (20 < score && 25 >= score) {
        grade = "B";
    } else if (15 < score && 20 >= score) {
        grade = "C";
    } else if (10 < score && 15 >= score) {
        grade = "D";
    } else if (5 < score && 10 >= score) {
        grade = "E";
    } else if (0 <= score && 5 >= score) {
        grade = "F";
    }
    return grade;
}

/**
 * The main function to execute the program
 */
function main() {
    const score = +(readLine());

    console.log(getGrade(score));
}
