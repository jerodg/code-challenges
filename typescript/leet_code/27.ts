/**
 * @fileoverview This module contains a solution for the "Remove Element" problem from LeetCode.
 * The problem is solved by using two pointers to traverse the array and move non-duplicate elements to the front.
 */

/**
 * Function to remove all instances of a value in-place and return the new length.
 * @param {number[]} nums - The array.
 * @param {number} val - The value to remove.
 * @return {number} The length of the array after the value has been removed.
 */
function removeElement(nums: number[], val: number): number {
    let i = 0;
    // Iterate over the array with the second pointer
    for (let j = 0; j < nums.length; j++) {
        // If the current element is not equal to the value
        if (nums[j] !== val) {
            // Move the current element to the position of the first pointer
            nums[i] = nums[j];
            // Increment the first pointer
            i++;
        }
    }
    // Return the new length of the array
    return i;
}
