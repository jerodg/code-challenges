/**
 * @fileoverview This module provides a function to calculate the maximum length of a subarray with at most K distinct elements.
 */

/**
 * Calculates the maximum length of a subarray with at most K distinct elements.
 * @param {number[]} nums - An array of numbers.
 * @param {number} k - The maximum number of distinct elements.
 * @return {number} - The maximum length of a subarray with at most K distinct elements.
 */
let maxSubarrayLength = function (nums, k) {
    // Initialize the left pointer
    // Object to keep track of the count of each number
    // Variable to keep track of the maximum length
    let left = 0, counter = {}, maxLength = 0;
    // Loop through the array
    for (let right = 0; right < nums.length; right++) {
        // Current number
        let num = nums[right];
        // Increase the count of the current number
        counter[num] = (counter[num] || 0) + 1;
        // While the count of the current number is greater than k, move the left pointer to the right
        while (counter[num] > k) {
            // Decrease the count of the number at the left pointer
            counter[nums[left]] -= 1;
            // If the count of the number at the left pointer is 0, remove it from the counter
            if (0 === counter[nums[left]]) {
                delete counter[nums[left]];
            }
            // Move the left pointer to the right
            left += 1;
        }
        // Update the maximum length
        maxLength = Math.max(maxLength, right - left + 1);
    }
    // Return the maximum length
    return maxLength;
};
