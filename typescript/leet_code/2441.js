/**
 * @file This module contains a function to find the maximum absolute value in an array that also has its negative counterpart.
 * @module leet_code/2441
 */
/**
 * Finds the maximum absolute value in an array that also has its negative counterpart.
 *
 * This function iterates over the array of numbers, maintaining a set of previously encountered numbers.
 * For each number, it checks if the negative of its absolute value (for positive numbers) or its absolute value (for negative numbers)
 * is in the set of previously encountered numbers. If it is, it updates the maximum value found so far.
 *
 * @param {number[]} nums - The array of numbers to search. It is expected to contain both positive and negative numbers.
 * @returns {number} The maximum absolute value in the array that also has its negative counterpart, or -1 if no such number exists.
 *
 * @throws {TypeError} If the input is not an array of numbers.
 */
function findMaxK(nums) {
    if (!Array.isArray(nums) || !nums.every(function (num) { return typeof num === 'number'; })) {
        throw new TypeError('Input must be an array of numbers');
    }
    var max = -1;
    var previousNums = new Set();
    for (var _i = 0, nums_1 = nums; _i < nums_1.length; _i++) {
        var num = nums_1[_i];
        if (num > 0) {
            var negative = -Math.abs(num);
            // If the negative counterpart of the current number exists in the set, update the max value
            if (previousNums.has(negative)) {
                max = Math.max(max, num);
            }
        }
        else {
            var positive = Math.abs(num);
            // If the positive counterpart of the current number exists in the set, update the max value
            if (previousNums.has(positive)) {
                max = Math.max(max, positive);
            }
        }
        // Add the current number to the set of previously encountered numbers
        previousNums.add(num);
    }
    return max;
}
