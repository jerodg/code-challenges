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
function findMaxK(nums: number[]): number {
    if (!Array.isArray(nums) || !nums.every(num => typeof num === 'number')) {
        throw new TypeError('Input must be an array of numbers');
    }

    let max: number = -1;
    const previousNums: Set<number> = new Set<number>();

    for (const num of nums) {
        if (num > 0) {
            const negative: number = -Math.abs(num);
            // If the negative counterpart of the current number exists in the set, update the max value
            if (previousNums.has(negative)) {
                max = Math.max(max, num);
            }
        } else {
            const positive: number = Math.abs(num);
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
