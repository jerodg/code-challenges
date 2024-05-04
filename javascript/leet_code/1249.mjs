/**
 * @file This module removes invalid parentheses from a string to make it valid.
 * @module leet_code/1249
 */

/**
 * Removes the minimum number of invalid parentheses in order to make the input string valid.
 *
 * The function uses a stack to keep track of the indices of the open parentheses. It also keeps
 * track of the indices of the unmatched closing parentheses. The indices in the stack and the array
 * of unmatched closing parentheses are then merged and sorted. The function then constructs the
 * result string by skipping the characters at the indices in
 * the merged array.
 *
 * @param {string} s - The input string.
 * @returns {string} The input string with the minimum number of parentheses removed to make it valid.
 */
let minRemoveToMakeValid = function (s) {
    // Stack to keep track of the indices of the open parentheses
    let stack = [];
    // Array to keep track of the indices of the unmatched closing parentheses
    let remove = [];
    for (let i = 0; i < s.length; i++) {
        if ("(" === s[i]) {
            stack.push(i);
        } else if (")" === s[i]) {
            if (0 === stack.length) {
                remove.push(i);
            } else {
                stack.pop();
            }
        }
    }
    // Merge and sort the indices in the stack and the array of unmatched closing parentheses
    stack = stack.concat(remove);
    stack = stack.sort((a, b) => a - b);
    // Construct the result string by skipping the characters at the indices in the merged array
    let result = "";
    let j = 0;
    for (let i = 0; i < s.length; i++) {
        if (j < stack.length && stack[j] === i) {
            j++;
        } else {
            result += s[i];
        }
    }
    // Return the input string with the minimum number of parentheses removed to make it valid
    return result;
};
