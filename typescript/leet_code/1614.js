/**
 * @fileoverview This module contains a solution for the "Maximum Nesting Depth of the Parentheses" problem from
 *     LeetCode. The problem is solved by using a counter to keep track of the current depth of the parentheses and
 *     another counter to keep track of the maximum depth.
 */
/**
 * Function to calculate the maximum depth of valid parentheses in a string.
 * The function iterates over the string and uses a counter to keep track of the current depth of the parentheses.
 * If it encounters an open parenthesis, it increments the current depth and updates the maximum depth if necessary.
 * If it encounters a close parenthesis, it decrements the current depth.
 *
 * @param {string} s - The input string.
 * @returns {number} The maximum depth of valid parentheses in the string.
 */
function maxDepth(s) {
    // Initialize the maximum depth and the current depth
    var maxDepth = 0;
    var currentDepth = 0;
    // Iterate over the characters in the string
    for (var i = 0; i < s.length; i++) {
        // If the current character is an open parenthesis
        if (s[i] === "(") {
            // Increment the current depth
            currentDepth++;
            // If the current depth is greater than the maximum depth, update the maximum depth
            if (currentDepth > maxDepth) {
                maxDepth = currentDepth;
            }
        }
        else if (s[i] === ")") {
            // If the current character is a close parenthesis, decrement the current depth
            currentDepth--;
        }
    }
    // Return the maximum depth
    return maxDepth;
}
