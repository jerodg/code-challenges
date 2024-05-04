/**
 * @fileoverview This module contains a solution for the "Remove K Digits" problem from LeetCode.
 * The problem is solved by using a stack to keep track of the smallest number that can be formed.
 */

/**
 * Function to remove k digits from the number to make it smallest.
 * @param {string} num - The number from which digits are to be removed.
 * @param {number} k - The count of digits to be removed.
 * @return {string} - The smallest possible number after removing k digits.
 */
function removeKdigits(num: string, k: number): string {
    // Initialize stack and removed digits count
    let stk = [], rem = 0;

    // Iterate over each digit in the number
    for (let n of num) {
        // While stack is not empty and top of stack is greater than current digit and removed digits count is less
        // than k
        while (stk.length && n < stk[stk.length - 1] && rem < k) {
            // Remove the top of stack
            stk.pop();
            // Increment the removed digits count
            rem++;
        }
        // Push the current digit to the stack
        stk.push(n);
    }

    // If there are still digits to remove
    while (rem < k) {
        // Remove the top of stack
        stk.pop();
        // Increment the removed digits count
        rem++;
    }

    // Remove leading zeros
    while (stk[0] === "0") {
        stk.shift();
    }

    // If stack is not empty, join the digits to form the number, else return "0"
    return stk.length ? stk.join("") : "0";
}
