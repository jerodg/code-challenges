const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

// Event listener for data input
process.stdin.on("data", function (inputStdin) {
    inputString += inputStdin;
});

// Event listener for end of data input
process.stdin.on("end", function () {
    inputString = inputString.split("\n");

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
 * Function to perform dynamic array operations
 *
 * @param {number} n - The number of sequences
 * @param {Array} queries - The list of queries
 * @returns {Array} - The results of each type 2 query
 */
function dynamicArray(n, queries) {
    let lastAnswer = 0;
    let seqList = [];
    let result = [];

    // Initialize seqList with n empty sequences
    for (let i = 0; i < n; i++) {
        seqList.push([]);
    }

    // Process each query
    for (let i = 0; i < queries.length; i++) {
        let query = queries[i];
        let type = query[0];
        let x = query[1];
        let y = query[2];
        let index = (x ^ lastAnswer) % n;

        // Perform the operation based on the type of the query
        if (1 === type) {
            seqList[index].push(y);
        } else if (2 === type) {
            let size = seqList[index].length;
            lastAnswer = seqList[index][y % size];
            result.push(lastAnswer);
        }
    }

    return result;
}

/**
 * The main function to execute the program
 */
function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const firstMultipleInput = readLine().replace(/\s+$/g, "").split(" ");
    const n = parseInt(firstMultipleInput[0], 10);
    const q = parseInt(firstMultipleInput[1], 10);
    let queries = Array(q);

    // Read each query
    for (let i = 0; i < q; i++) {
        queries[i] = readLine().replace(/\s+$/g, "").split(" ").map(queriesTemp => parseInt(queriesTemp, 10));
    }

    const result = dynamicArray(n, queries);

    ws.write(result.join("\n") + "\n");
    ws.end();
}
