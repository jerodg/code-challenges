/**
 * @fileoverview This module contains a solution for the "Merge Sorted Array" problem from LeetCode.
 * The problem is solved by using a two-pointer approach from the end of the arrays.
 */
/**
 * Function to merge two sorted arrays in-place.
 * @param {number[]} nums1 - The first sorted array.
 * @param {number} m - The number of initial elements in nums1.
 * @param {number[]} nums2 - The second sorted array.
 * @param {number} n - The number of elements in nums2.
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1, m, nums2, n) {
    // Initialize two pointers at the end of the initial elements in nums1 and nums2
    var i = m - 1;
    var j = n - 1;
    // Initialize a pointer at the end of nums1
    var k = m + n - 1;
    // While there are elements in both nums1 and nums2
    while (i >= 0 && j >= 0) {
        // If the current element in nums1 is greater than the current element in nums2
        if (nums1[i] > nums2[j]) {
            // Move the current element in nums1 to the end
            nums1[k] = nums1[i];
            // Move the pointer in nums1 to the left
            i--;
        }
        else {
            // Move the current element in nums2 to the end
            nums1[k] = nums2[j];
            // Move the pointer in nums2 to the left
            j--;
        }
        // Move the pointer in nums1 to the left
        k--;
    }
    // If there are remaining elements in nums2
    while (j >= 0) {
        // Move the remaining elements in nums2 to the end
        nums1[k] = nums2[j];
        // Move the pointers in nums2 and nums1 to the left
        j--;
        k--;
    }
}
