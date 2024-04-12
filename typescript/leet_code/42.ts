/**
 * @fileoverview This module contains a solution for the "Trapping Rain Water" problem from LeetCode.
 * The problem is solved using a two-pointer approach.
 */

/**
 * Function to calculate the amount of trapped rain water.
 * @param {number[]} height - An array where each element represents a bar in the histogram.
 * @return {number} The total amount of rain water that can be trapped.
 */
function trap(height: number[]): number {
    let left = 0;
    let right = height.length - 1;
    let leftMax = 0;
    let rightMax = 0;
    let result = 0;

    // Iterate until the two pointers meet
    while (left < right) {
        // Calculate the minimum height between the two sides
        const minHeight = Math.min(leftMax, rightMax);
        if (height[left] < height[right]) {
            // If the left side is shorter
            if (height[left] > leftMax) {
                // Update the maximum height on the left
                leftMax = height[left];
            } else {
                // Add the difference between the maximum height and the current height to the result
                result += leftMax - height[left];
            }
            // Move the left pointer to the right
            left++;
        } else {
            // If the right side is shorter or equal
            if (height[right] > rightMax) {
                // Update the maximum height on the right
                rightMax = height[right];
            } else {
                // Add the difference between the maximum height and the current height to the result
                result += rightMax - height[right];
            }
            // Move the right pointer to the left
            right--;
        }
    }
    // Return the total amount of trapped rain water
    return result;
}
