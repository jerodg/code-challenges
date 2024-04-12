/**
 * @fileoverview This module contains a solution for the "Make The String Great" problem from LeetCode.
 * The problem is solved by using a stack to keep track of the characters in the string.
 */
/**
 * Function to make a string good.
 * A string is good if there are no two adjacent characters that are the same letter but different case.
 * The function iterates over the string and uses a stack to keep track of the characters.
 * If it encounters a character that is the same letter but different case as the top of the stack, it pops the stack.
 * Otherwise, it pushes the character to the stack.
 *
 * @param {string} s - The input string.
 * @returns {string} The string after making it good.
 */
function makeGood(s) {
    // Initialize the stack
    var stack = [];
    // Iterate over the characters in the string
    for (var i = 0; i < s.length; i++) {
        // If the stack is empty, push the current character to the stack
        if (stack.length === 0) {
            stack.push(s[i]);
        }
        else {
            // Get the top of the stack
            var top_1 = stack[stack.length - 1];
            // If the top of the stack and the current character are the same letter but different case
            if (top_1.toLowerCase() === s[i].toLowerCase() && top_1 !== s[i]) {
                // Pop the stack
                stack.pop();
            }
            else {
                // Otherwise, push the current character to the stack
                stack.push(s[i]);
            }
        }
    }
    // Join the stack into a string and return it
    return stack.join("");
}
