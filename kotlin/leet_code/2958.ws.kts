/**
 * This Kotlin module provides a solution for a hypothetical problem where the maximum length of a subarray with at most `k` distinct elements is to be found.
 *
 * @module leet_code/2958.ws.kts
 */

/**
 * Solution class provides a method to calculate the maximum length of a subarray with at most `k` distinct elements.
 */
class Solution {

    /**
     * This function calculates the maximum length of a subarray with at most `k` distinct elements.
     *
     * @param nums The input array of integers where the subarray is to be found.
     * @param k The maximum number of distinct elements allowed in the subarray.
     * @return An integer representing the maximum length of a subarray with at most `k` distinct elements.
     *
     * The function uses a sliding window approach. It maintains a window of elements with at most `k` distinct elements.
     * It uses a map to keep track of the count of each element in the window.
     * It starts with a window at the left end of the array and tries to extend it to the right as much as possible while keeping the number of distinct elements in the window less than or equal to `k`.
     * When it is not possible to extend the window to the right, it moves the left end of the window to the right.
     * It keeps track of the maximum length of the window, which represents the maximum length of a subarray with at most `k` distinct elements.
     *
     * Example usage:
     * val solution = Solution()
     * val nums = intArrayOf(1, 2, 1, 2, 3)
     * val k = 2
     * val maxLength = solution.maxSubarrayLength(nums, k)
     * // maxLength will be 4 as the maximum length of a subarray with at most 2 distinct elements is 4
     */
    fun maxSubarrayLength(nums: IntArray, k: Int): Int {
        var left = 0
        val counter = mutableMapOf<Int, Int>()
        var maxLength = 0
        for (right in nums.indices) {
            counter[nums[right]] = counter.getOrDefault(nums[right], 0) + 1
            while (counter.size > k) {
                counter[nums[left]] = counter[nums[left]]!! - 1
                if (counter[nums[left]]!! == 0) {
                    counter.remove(nums[left])
                }
                left++
            }
            maxLength = maxOf(maxLength, right - left + 1)
        }
        return maxLength
    }
}
