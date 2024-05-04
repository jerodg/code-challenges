/**
 * This enum provides a solution for the problem of checking if a string is valid.
 * A string is valid if it can be made valid by inserting, deleting, or replacing characters with parentheses.
 * The problem is solved by maintaining a range of possible numbers of open parentheses after processing each character in the string.
 * If a left parenthesis is encountered, the range is increased.
 * If a right parenthesis is encountered, the range is decreased.
 * If an asterisk is encountered, the range is both increased and decreased.
 * If at any point the range is invalid, the string is not valid.
 * If at the end the range includes zero, the string is valid.
 */
enum Solution {
    ;

    /**
     * Checks if a string is valid.
     *
     * @param s The input string. It is a string of characters, which can include left parentheses, right parentheses, and asterisks.
     *
     * @return A boolean indicating whether the string is valid. It is true if the string is valid, and false otherwise.
     */
    public static boolean checkValidString(final String s) {
        // Initialize the low and high ends of the range of possible numbers of open parentheses
        int low = 0, high = 0;

        // Iterate over the characters in the string
        for (final char c : s.toCharArray()) {
            // If a left parenthesis is encountered, increase the range
            if ('(' == c) {
                low++;
                high++;
            } else if (')' == (int) c) {
                // If a right parenthesis is encountered, decrease the range
                low--;
                high--;
            } else {
                // If an asterisk is encountered, both increase and decrease the range
                low--;
                high++;
            }

            // If at any point the range is invalid, return false
            if (0 > high) {
                return false;
            }

            // Ensure the low end of the range is not less than zero
            low = Math.max(low, 0);
        }

        // If at the end the range includes zero, return true
        return 0 == low;
    }
}
