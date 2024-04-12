/**
 * @fileoverview This module contains a solution for the "Remove Duplicates from Sorted Array" problem from LeetCode.
 * The problem is solved by using two pointers to traverse the array and move non-duplicate elements to the front.
 */

/**
 * Function to remove duplicates from a sorted array in-place and return the new length.
 * @param {number[]} nums - The sorted array.
 * @return {number} The length of the array after duplicates have been removed.
 */
function removeDuplicates(nums: number[]): number {
    // If the array is empty, return 0
    if (nums.length === 0) return 0;

    // Initialize the first pointer
    let i = 0;

    // Iterate over the array with the second pointer
    for (let j = 1; j < nums.length; j++) {
        // If the current element is not equal to the element at the first pointer
        if (nums[j] != nums[i]) {
            // Increment the first pointer
            i++;
            // Move the current element to the position of the first pointer
            nums[i] = nums[j];
        }
    }

    // Return the new length of the array
    return i + 1;
}
