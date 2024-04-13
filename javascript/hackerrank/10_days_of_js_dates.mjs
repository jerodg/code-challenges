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
 * Function to get the day of the week for a given date
 *
 * @param {string} dateString - The date in string format.
 * @returns {string} - The day of the week.
 */
function getDayName(dateString) {
    let dayName;
    const date = new Date(dateString);
    const day = date.getDay();

    // Determine the day of the week based on the day number
    switch (day) {
        case 0:
            dayName = "Sunday";
            break;
        case 1:
            dayName = "Monday";
            break;
        case 2:
            dayName = "Tuesday";
            break;
        case 3:
            dayName = "Wednesday";
            break;
        case 4:
            dayName = "Thursday";
            break;
        case 5:
            dayName = "Friday";
            break;
        case 6:
            dayName = "Saturday";
            break;
    }
    return dayName;
}

/**
 * The main function to execute the program
 */
function main() {
    const d = +readLine();

    // Loop through the number of dates to be processed
    for (let i = 0; i < d; i++) {
        const date = readLine();

        console.log(getDayName(date));
    }
}
