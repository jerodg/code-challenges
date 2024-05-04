/**
 * This Kotlin module provides a solution for the LeetCode problem 1249. Minimum Remove to Make Valid Parentheses.
 * The solution removes the minimum number of parentheses to make the input string valid.
 *
 * @module leet_code/1249.ws.kts
 */

/**
 * Solution class provides a method to remove the minimum number of parentheses to make the input string valid.
 */
class Solution {

    /**
     * This function removes the minimum number of parentheses to make the input string valid.
     *
     * @param s The input string which may contain invalid parentheses.
     * @return A string that is the same as the input string, except with the minimum number of parentheses removed to make it valid.
     *
     * The function uses a stack to keep track of the indices of the open parentheses. It iterates over the characters in the string.
     * If the character is an open parenthesis, it adds the index to the stack.
     * If the character is a close parenthesis, it checks if the stack is not empty. If the stack is not empty, it removes the top index from the stack.
     * If the stack is empty, it replaces the close parenthesis with a space in the string.
     * After iterating over all the characters in the string, it replaces any remaining open parentheses in the string with spaces.
     * Finally, it removes all spaces from the string and returns the result.
     *
     * Example usage:
     * val solution = Solution()
     * val s = "lee(t(c)o)de)"
     * val validString = solution.minRemoveToMakeValid(s)
     * // validString will be "lee(t(c)o)de"
     */
    fun minRemoveToMakeValid(s: String): String {
        val stack = mutableListOf<Int>()
        val sb = StringBuilder(s)
        for (i in s.indices) {
            if (s[i] == '(') {
                stack.add(i)
            } else if (s[i] == ')') {
                if (stack.isNotEmpty()) {
                    stack.removeAt(stack.size - 1)
                } else {
                    sb.setCharAt(i, ' ')
                }
            }
        }
        for (i in stack) {
            sb.setCharAt(i, ' ')
        }
        return sb.toString().replace(" ", "")
    }
}
