/**
 * This Kotlin module provides a solution for removing duplicates from a sorted array.
 * The solution modifies the input array in-place such that each element appears only once,
 * returning the new length of the array.
 *
 * @module leet_code/26.ws.kts
 */

/**
 * Solution class provides methods to remove duplicates from a sorted array.
 */
class Solution {

    /**
     * This function removes duplicates from a sorted array in-place and returns the new length of the array.
     *
     * @param nums A sorted integer array from which duplicates are to be removed.
     * @return The new length of the array after removing duplicates.
     *
     * @throws IllegalArgumentException If the input array is null.
     *
     * Example usage:
     * val solution = Solution()
     * val nums = intArrayOf(1, 1, 2)
     * val length = solution.removeDuplicates(nums)
     * // length will be 2 and nums will be [1, 2, 2]
     */
    fun removeDuplicates(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        var i = 0
        for (j in 1 until nums.size) {
            // If the current element is not equal to the previous element, increment the counter and update the element at the counter index
            if (nums[j] != nums[i]) {
                i++
                nums[i] = nums[j]
            }
        }
        return i + 1
    }
}
