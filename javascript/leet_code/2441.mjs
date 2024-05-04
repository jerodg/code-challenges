/**
 * @fileoverview This module provides a function to find the maximum absolute value of an integer in an array
 * that also contains its negative counterpart.
 * The function uses a Set to store the numbers and then checks for each number if its negative counterpart
 * is in the Set. If it is, it updates the maximum absolute value found so far.
 */
/**
 * Finds the maximum absolute value of an integer in an array that also contains its negative counterpart.
 *
 * @param {number[]} nums - The input array of numbers.
 * @returns {number} - The maximum absolute value of an integer in the array that also contains its negative
 *     counterpart. If no such number exists, it returns -1.
 */
const findMaxK = function (nums) {
    // Initialize the largest absolute value found so far to -1
    let largest = -1;

    // Initialize a Set to store the numbers
    let hash = new Set();

    // Iterate over the numbers in the array
    for (let i = 0; i < nums.length; i++) {
        // Calculate the negative counterpart of the current number
        let valueToFind = nums[i] >= 0 ? -1 * nums[i] : Math.abs(nums[i]);

        // If the negative counterpart is in the Set, update the largest absolute value
        if (hash.has(valueToFind)) {
            largest = Math.max(largest, Math.abs(valueToFind));
        } else {
            // If the negative counterpart is not in the Set, add the current number to the Set
            hash.add(nums[i]);
        }
    }

    // Return the largest absolute value found
    return largest;
};
