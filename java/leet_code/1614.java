/**
 * This class provides a solution for the problem of finding the maximum depth of valid parentheses
 * in a string.
 * The problem is solved by iterating over the string and maintaining a current depth of parentheses.
 * If an opening parenthesis is encountered, the current depth is increased.
 * If a closing parenthesis is encountered, the current depth is decreased.
 * The maximum depth is updated at each step.
 *
 * @author jerodg
 */
class Solution {

    /**
     * Finds the maximum depth of valid parentheses in a string.
     *
     * @param s The input string. It is a string of characters, which can include opening and
     *          closing parentheses.
     *
     * @return The maximum depth of valid parentheses in the string. It is a non-negative integer.
     */
    public static int maxDepth(final String s) {
        // Initialize the maximum depth to 0
        int maxDepth = 0;

        // Initialize the current depth to 0
        int currentDepth = 0;

        // Iterate over the string
        for (int i = 0; i < s.length(); i++) {
            // If an opening parenthesis is encountered, increase the current depth
            // and update the maximum depth
            if ('(' == s.charAt(i)) {
                currentDepth++;
                maxDepth = Math.max(maxDepth, currentDepth);
            } else if (')' == s.charAt(i)) {
                // If a closing parenthesis is encountered, decrease the current depth
                currentDepth--;
            }
        }

        // Return the maximum depth
        return maxDepth;
    }
}
