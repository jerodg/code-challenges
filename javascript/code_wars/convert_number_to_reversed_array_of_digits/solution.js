function digitize(num) {
    // Convert the number to a string
    let numStr = num.toString();

    // Create an empty array
    let digitList = [];

    // Iterate over the string in reverse order
    for (let i = numStr.length - 1; i >= 0; i--) {
        // Convert each character to an integer and append to the list
        digitList.push(parseInt(numStr[i]));
    }

    return digitList;
}
