/**
 * @fileoverview This module contains a solution for a problem where you need to find the maximum length of a subarray
 *     with at most K distinct elements. The problem is solved by using a sliding window approach and a counter to keep
 *     track of the number of occurrences of each element in the subarray.
 */

/**
 * Function to calculate the maximum length of a subarray with at most K distinct elements.
 * The function iterates over the nums array and uses a sliding window approach to find the subarray.
 * It uses a counter to keep track of the number of occurrences of each element in the subarray.
 * If the number of occurrences of an element exceeds K, it shrinks the window from the left until the condition is
 * satisfied again. It keeps track of the maximum length of the subarray during the process.
 *
 * @param {number[]} nums - The input array of numbers.
 * @param {number} k - The maximum number of distinct elements in the subarray.
 * @returns {number} The maximum length of a subarray with at most K distinct elements.
 */
function maxSubarrayLength(nums: number[], k: number): number {
    // Initialize the left pointer, the counter, and the maximum length
    let left: number = 0;
    let counter: { [key: number]: number } = {};
    let max_length: number = 0;

    // Iterate over the nums array with the right pointer
    for (let right: number = 0; right < nums.length; right++) {
        // Get the current number
        let num: number = nums[right];
        // Increment the count of the current number in the counter
        counter[num] = (counter[num] || 0) + 1;

        // While the count of the current number in the counter exceeds K
        while (counter[num] > k) {
            // Decrement the count of the number at the left pointer in the counter
            counter[nums[left]] -= 1;
            // If the count of the number at the left pointer in the counter is 0, remove it from the counter
            if (counter[nums[left]] === 0) {
                delete counter[nums[left]];
            }
            // Increment the left pointer
            left += 1;
        }

        // Update the maximum length if necessary
        max_length = Math.max(max_length, right - left + 1);
    }

    // Return the maximum length
    return max_length;
}
