/**
 * This module contains the Solution class which is used to solve the problem of finding
 * the number of wonderful substrings in a given word. A wonderful string is a string where
 * no more than one character appears an odd number of times.
 *
 * @file leet_code/1915.ws.kts
 */

/**
 * Solution class provides a method to find the number of wonderful substrings in a word.
 */
class Solution {
    /**
     * This function calculates the number of wonderful substrings in a given word.
     *
     * @param word The input word of type String. It is the word in which we need to find the number of wonderful substrings.
     * @return Returns the number of wonderful substrings in the input word. The return type is Long.
     *
     * @throws IllegalArgumentException If the input word is null.
     */
    fun wonderfulSubstrings(word: String): Long {
        // Array to store the count of each character in the word
        val cnt = IntArray(1024)
        cnt[0] = 1

        // Variable to store the final answer
        var ans: Long = 0L

        // Variable to store the sum of character counts
        var sum: Int = 0

        // Loop through each character in the word
        for (i in 0 until word.length) {
            // XOR the sum with the binary representation of the current character
            sum = sum xor (1 shl (word[i] - 'a'))

            // Add the count of the current sum to the answer
            ans += cnt[sum]

            var j: Int = 1

            // Loop through each bit in the sum
            while (j < 1024) {
                // Add the count of the XOR of the sum and the current bit to the answer
                ans += cnt[sum xor j]

                // Shift the current bit to the left
                j = j shl 1
            }

            // Increment the count of the current sum
            cnt[sum]++
        }

        // Return the final answer
        return ans
    }
}
