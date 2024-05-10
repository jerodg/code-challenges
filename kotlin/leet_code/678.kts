/**
 * This Kotlin module provides a solution for the LeetCode problem 678. Valid Parenthesis String.
 * The solution checks if a given string is a valid parenthesis string.
 *
 * @module leet_code/678.ws.kts
 */

/**
 * Solution class provides a method to check if a string is a valid parenthesis string.
 */
class Solution {

    /**
     * This function checks if a given string is a valid parenthesis string.
     *
     * @param s The string to be checked.
     * @return A boolean value indicating whether the string is a valid parenthesis string. Returns true if it is valid, false otherwise.
     *
     * The function uses two counters, low and high, to keep track of the balance of the parenthesis.
     * It iterates over the characters in the string. If the character is '(', it increments both counters.
     * If the character is ')', it decrements both counters. If the character is '*', it increments the high counter and decrements the low counter.
     * If at any point the high counter is less than 0, it breaks the loop and returns false.
     * After the loop, if the low counter is 0, it returns true, indicating that the string is a valid parenthesis string.
     *
     * Example usage:
     * val solution = Solution()
     * val s = "(*))"
     * val isValid = solution.checkValidString(s)
     * // isValid will be true as the string is a valid parenthesis string
     */
    fun checkValidString(s: String): Boolean {
        var low = 0
        var high = 0
        for (c in s) {
            low += if (c == '(') 1 else -1
            high += if (c != ')') 1 else -1
            if (high < 0) break
            low = maxOf(low, 0)
        }
        return low == 0
    }
}
