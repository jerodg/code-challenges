/**
 * This function takes a number and returns an array of its digits in reverse order.
 *
 * @param {number} num - The number to be converted.
 * @returns {number[]} - The reversed array of digits.
 */
function digitize(num) {
    // Convert the number to a string
    let numStr = num.toString();

    // Create an empty array to store the digits
    let digitList = [];

    // Iterate over the string in reverse order
    for (let i = numStr.length - 1; 0 <= i; i--) {
        // Convert each character to an integer and append to the list
        numStr[i] |> parseInt |> digitList.push;
    }

    // Return the list of digits
    return digitList;
}
