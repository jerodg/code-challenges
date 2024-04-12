/**
 * @fileoverview This module contains a solution for the "Minimum Remove to Make Valid Parentheses" problem from LeetCode.
 * The problem is solved by using a stack to keep track of the indices of the open parentheses.
 */

/**
 * Function to remove the minimum number of parentheses to make the input string valid.
 * The function iterates over the string and uses a stack to keep track of the indices of the open parentheses.
 * If it encounters a close parenthesis and the stack is empty, it removes the close parenthesis.
 * After iterating over the string, it removes any remaining open parentheses.
 *
 * @param {string} s - The input string.
 * @returns {string} The string after removing the minimum number of parentheses to make it valid.
 */
function minRemoveToMakeValid(s: string): string {
    // Initialize the stack
    let stack: number[] = [];
    // Convert the string to an array of characters for easy manipulation
    let sArr: string[] = s.split("");
    // Iterate over the characters in the string
    for (let i = 0; i < sArr.length; i++) {
        // If the current character is an open parenthesis
        if (sArr[i] === "(") {
            // Push the index of the open parenthesis to the stack
            stack.push(i);
        } else if (sArr[i] === ")") {
            // If the current character is a close parenthesis
            if (stack.length > 0) {
                // If the stack is not empty, pop the index of the last open parenthesis from the stack
                stack.pop();
            } else {
                // If the stack is empty, remove the close parenthesis
                sArr[i] = "";
            }
        }
    }
    // Remove any remaining open parentheses
    for (let i = 0; i < stack.length; i++) {
        sArr[stack[i]] = "";
    }
    // Join the array of characters back into a string and return it
    return sArr.join("");
}
