/**
 * This Kotlin module provides a solution for the LeetCode problem 1544. Make The String Great.
 * The solution makes the string "good" by removing a pair of adjacent characters that are the same but have different cases.
 *
 * @module leet_code/1544.ws.kts
 */

/**
 * Solution class provides a method to make the string "good".
 */
class Solution {

    /**
     * This function makes the string "good" by removing a pair of adjacent characters that are the same but have different cases.
     *
     * @param s The input string which may contain pairs of adjacent characters that are the same but have different cases.
     * @return A string that is the same as the input string, except with all pairs of adjacent characters that are the same but have different cases removed.
     *
     * The function uses a stack to keep track of the characters in the string. It iterates over the characters in the string.
     * If the stack is not empty and the last character in the stack is the same as the current character but has a different case, it removes the last character from the stack.
     * Otherwise, it adds the current character to the stack.
     * After iterating over all the characters in the string, it joins the characters in the stack into a string and returns the result.
     *
     * Example usage:
     * val solution = Solution()
     * val s = "leEeetcode"
     * val goodString = solution.makeGood(s)
     * // goodString will be "leetcode"
     */
    fun makeGood(s: String): String {
        val stack = mutableListOf<Char>()
        for (c in s) {
            if (stack.isNotEmpty() && stack.last().toLowerCase() == c.toLowerCase() && stack.last() != c) {
                stack.removeAt(stack.size - 1)
            } else {
                stack.add(c)
            }
        }
        return stack.joinToString("")
    }
}
