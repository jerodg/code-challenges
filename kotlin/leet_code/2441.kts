/**
 * This module contains the Solution class which is used to solve the problem of finding
 * the maximum absolute number in an array that also appears as its negative in the same array.
 *
 * @file leet_code/2441.ws.kts
 */
class Solution {
    /**
     * This function finds the maximum absolute number in an array that also appears as its negative in the same array.
     *
     * @param nums The input array. It is an array of integers where we need to find the maximum absolute number that also appears as its negative.
     * @return Returns the maximum absolute number that also appears as its negative in the input array. If no such number exists, it returns -1.
     *
     * @throws IllegalArgumentException If the input array is null.
     */
    fun findMaxK(nums: IntArray): Int {
        // Initialize an array to store the count of each number and its negative in the array.
        val counters = IntArray(1024)
        // Initialize the maximum number to -1.
        var max = -1

        // Iterate over each number in the array.
        for (n in nums) {
            // Calculate the absolute value of the current number.
            val an = Math.abs(n)
            // Update the count of the current number and its negative.
            counters[an] = counters[an] or if (n < 0) 1 else 2
            // If the current number and its negative both exist in the array, update the maximum number.
            if (counters[an] == 3) {
                max = Math.max(max, an)
            }
        }

        // Return the maximum number.
        return max
    }
}
