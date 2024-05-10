/**
 * This Kotlin module provides a solution for removing an element from an array.
 * The solution modifies the input array in-place such that each occurrence of the target element is removed,
 * returning the new length of the array.
 *
 * @module leet_code/27.ws.kts
 */

/**
 * Solution class provides methods to remove an element from an array.
 */
class Solution {

    /**
     * This function removes all instances of a specific element from an array in-place and returns the new length of the array.
     *
     * @param nums An integer array from which the target element is to be removed.
     * @param `val` The target integer to be removed from the array.
     * @return The new length of the array after removing the target element.
     *
     * @throws IllegalArgumentException If the input array is null.
     *
     * Example usage:
     * val solution = Solution()
     * val nums = intArrayOf(3, 2, 2, 3)
     * val `val` = 3
     * val length = solution.removeElement(nums, `val`)
     * // length will be 2 and nums will be [2, 2, 2, 3]
     */
    fun removeElement(nums: IntArray, `val`: Int): Int {
        var i = 0
        var j = 0
        while (j < nums.size) {
            // If the current element is not equal to the target element, update the element at the counter index and increment the counter
            if (nums[j] != `val`) {
                nums[i] = nums[j]
                i++
            }
            j++
        }
        return i
    }
}
