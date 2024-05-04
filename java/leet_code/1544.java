import java.util.Stack;

/**
 * This class provides a solution for the problem of making a string good.
 * A string is good if it doesn't have two adjacent characters that are the same, but one is
 * uppercase and the other is lowercase.
 * The problem is solved by using a stack to keep track of the characters in the string.
 * If the current character and the top character of the stack are the same but have different
 * cases, the top character of the stack is removed.
 * Otherwise, the current character is pushed onto the stack.
 * Finally, the characters in the stack are popped and appended to a string builder, which is then
 * reversed and returned as a string.
 *
 * @author jerodg
 */
class Solution {

    /**
     * Makes a string good by removing adjacent characters that are the same but have different cases.
     *
     * @param s The input string. It is a string of characters, which can include both uppercase
     *          and lowercase letters.
     *
     * @return The good string. It is a string of characters, which can include both uppercase
     *         and lowercase letters.
     */
    public String makeGood(final String s) {
        // Initialize a stack to keep track of the characters in the string
        final Stack<Character> stack = new Stack<>();

        // Iterate over the characters in the string
        for (final char c : s.toCharArray()) {
            // If the stack is not empty and the current character and the top character of the stack are the same but have different cases,
            // remove the top character of the stack
            if (!stack.isEmpty() && 32 == Math.abs(stack.peek() - (int) c)) {
                stack.pop();
            } else {
                // Otherwise, push the current character onto the stack
                stack.push(c);
            }
        }

        // Initialize a string builder
        final StringBuilder sb = new StringBuilder();

        // Pop the characters from the stack and append them to the string builder
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }

        // Reverse the string builder and return it as a string
        return sb.reverse().toString();
    }
}
