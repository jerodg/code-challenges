/**
 * @fileoverview This module provides a function to calculate the maximum depth of valid parentheses in a string.
 */
/**
 * Calculates the maximum depth of valid parentheses in a string.
 * @param {string} s - The input string.
 * @return {number} - The maximum depth of valid parentheses.
 */
const maxDepth = function (s) {
    // Variable to keep track of the maximum depth
    let maxDepth = 0;
    // Variable to keep track of the current depth
    let currentDepth = 0;
    for (let i = 0; i < s.length; i++) {
        // If the current character is an opening parenthesis, increment the current depth
        // and update the maximum depth if necessary
        if ("(" === s[i]) {
            currentDepth++;
            if (currentDepth > maxDepth) {
                maxDepth = currentDepth;
            }
        }
        // If the current character is a closing parenthesis, decrement the current depth
        else if (")" === s[i]) {
            currentDepth--;
        }
    }
    // Return the maximum depth
    return maxDepth;
};
