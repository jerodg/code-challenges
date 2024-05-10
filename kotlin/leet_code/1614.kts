/**
 * This Kotlin module provides a solution for the LeetCode problem 1614. Maximum Nesting Depth of the Parentheses.
 * The solution calculates the maximum depth of valid parentheses strings.
 *
 * @module leet_code/1614.ws.kts
 */

/**
 * Solution class provides a method to calculate the maximum depth of valid parentheses strings.
 */
class Solution {

    /**
     * This function calculates the maximum depth of valid parentheses strings.
     *
     * @param s The input string which may contain parentheses.
     * @return An integer representing the maximum depth of valid parentheses strings in the input string.
     *
     * The function uses two counters, max and count. It iterates over the characters in the string.
     * If the character is an open parenthesis, it increments the count and updates the max with the maximum of max and count.
     * If the character is a close parenthesis, it decrements the count.
     * After iterating over all the characters in the string, it returns the max, which represents the maximum depth of valid parentheses strings.
     *
     * Example usage:
     * val solution = Solution()
     * val s = "(1+(2*3)+((8)/4))+1"
     * val maxDepth = solution.maxDepth(s)
     * // maxDepth will be 3 as the deepest nested parentheses is 3 levels deep
     */
    fun maxDepth(s: String): Int {
        var max = 0
        var count = 0
        for (c in s) {
            if (c == '(') {
                count++
                max = maxOf(max, count)
            } else if (c == ')') {
                count--
            }
        }
        return max
    }
}
