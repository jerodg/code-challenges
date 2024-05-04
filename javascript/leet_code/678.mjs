/**
 * Function to check if a string is valid based on the following rules:
 * - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
 * - Any right parenthesis ')' must have a corresponding left parenthesis '('.
 * - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
 * - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
 *
 * @param {string} s - The input string
 * @returns {boolean} - True if the string is valid, false otherwise
 */
let checkValidString = function (s) {
    // Initialize counters for left and right parentheses
    let left = 0;
    let right = 0;

    // Iterate over each character in the string
    for (let i = 0; i < s.length; i++) {
        // If the current character is a left parenthesis or a '*', increment the left counter
        // Otherwise, decrement the left counter
        left += "(" === s[i] ? 1 : -1;
        // If the current character is a right parenthesis or a '*', decrement the right counter
        // Otherwise, increment the right counter
        right += ")" === s[i] ? -1 : 1;

        // If the right counter is negative, the string is not valid
        if (0 > right) {
            break;
        }

        // Reset the left counter to 0 if it is negative
        left = Math.max(left, 0);
    }

    // The string is valid if the left counter is 0
    return 0 === left;
};
