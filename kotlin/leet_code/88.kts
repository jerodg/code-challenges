/**
 * This Kotlin module provides a solution for the LeetCode problem 88. Merge Sorted Array.
 * The solution merges two sorted integer arrays into one sorted array.
 *
 * @module leet_code/88.ws.kts
 */

/**
 * Solution class provides methods to merge two sorted integer arrays into one sorted array.
 */
class Solution {

    /**
     * This function merges two sorted integer arrays into one sorted array.
     *
     * @param nums1 An integer array representing the first sorted array.
     * @param m An integer representing the number of initial elements of nums1 that are sorted.
     * @param nums2 An integer array representing the second sorted array.
     * @param n An integer representing the number of elements in nums2.
     * @return Unit. This function returns nothing as it modifies the nums1 array in-place.
     *
     * The function uses three pointers, one for each array and one for the current position in the merged array.
     * It starts from the end of each array and compares the elements at the current positions.
     * The larger element is placed at the current position in the merged array and the corresponding pointer is moved.
     * If there are remaining elements in nums2 after all elements in nums1 have been processed, they are copied to nums1.
     *
     * Example usage:
     * val solution = Solution()
     * val nums1 = intArrayOf(1,2,3,0,0,0)
     * val m = 3
     * val nums2 = intArrayOf(2,5,6)
     * val n = 3
     * solution.merge(nums1, m, nums2, n)
     * // nums1 will be [1,2,2,3,5,6]
     */
    fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
        // Initialize pointers for nums1, nums2, and the merged array
        var i = m - 1
        var j = n - 1
        var k = m + n - 1
        // Continue until all elements in nums1 and nums2 have been processed
        while (i >= 0 && j >= 0) {
            // If the current element in nums1 is larger, place it in the merged array
            if (nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--]
            }
            // If the current element in nums2 is larger or equal, place it in the merged array
            else {
                nums1[k--] = nums2[j--]
            }
        }
        // Copy any remaining elements from nums2 to nums1
        while (j >= 0) {
            nums1[k--] = nums2[j--]
        }
    }
}
