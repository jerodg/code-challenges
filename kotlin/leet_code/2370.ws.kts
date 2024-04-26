/**
 * This module provides a solution for finding the longest ideal string.
 * An ideal string is defined by the problem statement (not provided here).
 * The solution is implemented in the Solution class.
 */

class Solution {
    /**
     * Finds the longest ideal string in the given string `s` with a maximum distance `k`.
     *
     * @param s The string to search for the longest ideal string. Expected type: String.
     * @param k The maximum distance between characters in the ideal string. Expected type: Int.
     * @return The length of the longest ideal string. Return type: Int.
     */
    fun longestIdealString(s: String, k: Int): Int {
        // If k is 25, return the length of the string as the longest ideal string.
        if (k == 25) return s.length

        // Initialize an array to store the frequency of each character in the string.
        val alphabet = IntArray(128)

        // Initialize variables to keep track of the maximum length and current length of the ideal string.
        var maxLength = 1
        var curLength = 0

        // Iterate over each character in the string.
        for (ch in s) {
            // Update the current length by finding the maximum length in the range and incrementing it by 1.
            curLength = maxInRange(alphabet, ch.code, k) + 1
            // Update the frequency of the current character.
            alphabet[ch.code] = curLength
            // Update the maximum length if the current length is greater.
            maxLength = Math.max(curLength, maxLength)
        }

        // Return the maximum length of the ideal string.
        return maxLength
    }

    /**
     * Finds the maximum length in the range of characters around `ch` within the distance `k`.
     *
     * @param alphabet The array storing the frequency of each character. Expected type: IntArray.
     * @param ch The character to find the range around. Expected type: Int.
     * @param k The distance to find the range within. Expected type: Int.
     * @return The maximum length in the range. Return type: Int.
     */
    private fun maxInRange(alphabet: IntArray, ch: Int, k: Int): Int {
        // Calculate the range around the character.
        val from = ch - k
        val to = (ch + k).coerceAtMost(122)
        // Initialize the maximum length with the frequency of the character at the end of the range.
        var max = alphabet[to]

        // Iterate over the range.
        for (i in from until to) {
            // Update the maximum length if the frequency of the current character is greater.
            max = Math.max(alphabet[i], max)
        }
        // Return the maximum length in the range.
        return max
    }
}
