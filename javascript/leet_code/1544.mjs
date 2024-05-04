/**
 * @fileoverview This module provides functions to manipulate strings.
 */
/**
 * Removes the minimum number of parentheses to make the input string valid.
 * @param {string} s - The input string.
 * @return {string} - The valid string.
 */
let minRemoveToMakeValid = function (s) {
    // Stack to keep track of the indices of the invalid parentheses
    let stack = [];
    // Array to keep track of the indices to be removed
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
    // Combine the indices of the invalid parentheses and sort them
    stack = stack.concat(remove);
    stack = stack.sort((a, b) => a - b);
    let result = "";
    let j = 0;
    for (let i = 0; i < s.length; i++) {
        if (j < stack.length && stack[j] === i) {
            j++;
        } else {
            result += s[i];
        }
    }
    return result;
};

/**
 * Transforms the input string by removing all instances of two adjacent characters that are the same letter, one lowercase and one
 * uppercase.
 * @param {string} s - The input string.
 * @return {string} - The transformed string.
 */
let makeGood = function (s) {
    // Stack to keep track of the characters
    let stack = [];
    for (let i = 0; i < s.length; i++) {
        if (0 === stack.length) {
            stack.push(s[i]);
        } else {
            let top = stack[stack.length - 1];
            // If the top character of the stack and the current character are the same letter but different case, pop the stack
            if (top.toLowerCase() === s[i].toLowerCase() && top !== s[i]) {
                stack.pop();
            } else {
                stack.push(s[i]);
            }
        }
    }
    return stack.join("");
};
