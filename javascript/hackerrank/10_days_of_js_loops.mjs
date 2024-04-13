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
 * Function to print vowels and consonants of a string separately
 *
 * @param {string} s - The string to process.
 */
const vowelsAndConsonants = s => {
    let vowels = ["a", "e", "i", "o", "u"];
    let consonants = [];
    for (let i = 0; i < s.length; i++) {
        // If the character is a vowel, print it
        if (vowels.includes(s[i])) {
            console.log(s[i]);
        } else {
            // If the character is a consonant, add it to the consonants array
            consonants.push(s[i]);
        }
    }
    // Print all the consonants
    for (let i = 0; i < consonants.length; i++) {
        console.log(consonants[i]);
    }
};

/**
 * The main function to execute the program
 */
function main() {
    const s = readLine();

    vowelsAndConsonants(s);
}
