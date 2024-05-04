import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

/**
 * This class provides a solution for the problem of removing the minimum number of parentheses to
 * make a string valid.
 * A string is valid if it has balanced parentheses.
 * The problem is solved by using a stack to keep track of the indices of the parentheses in the
 * string.
 * If a closing parenthesis is encountered and the stack is empty or the top of the stack is another
 * closing parenthesis, the index of the closing parenthesis is added to a set of indices to be removed.
 * If a closing parenthesis is encountered and the top of the stack is an opening parenthesis,
 * the top of the stack is removed.
 * If an opening parenthesis is encountered, its index is pushed onto the stack.
 * After iterating over the string, any indices remaining in the stack are added to the set of
 * indices to be removed.
 * Finally, a new string is built by appending the characters at the indices not in the set.
 */
class Solution {

    /**
     * Removes the minimum number of parentheses to make a string valid.
     *
     * @param s The input string. It is a string of characters, which can include opening and
     *          closing parentheses.
     *
     * @return The valid string. It is a string of characters, which can include opening and
     *         closing parentheses.
     */
    public String minRemoveToMakeValid(final String s) {
        // Initialize a stack to keep track of the indices of the parentheses in the string
        final Stack<Integer> stack = new Stack<>();

        // Initialize a set to keep track of the indices to be removed
        final Set<Integer> remove = new HashSet<>();

        // Iterate over the characters in the string
        for (int i = 0; i < s.length(); i++) {
            // If an opening parenthesis is encountered, push its index onto the stack
            if ('(' == s.charAt(i)) {
                stack.add(i);
            } else if (')' == s.charAt(i)) {
                // If a closing parenthesis is encountered and the stack is empty or the top of the
                // stack is another closing parenthesis,
                // add the index of the closing parenthesis to the set of indices to be removed
                if (stack.isEmpty() || ')' == s.charAt(stack.peek())) {
                    remove.add(i);
                } else {
                    // If a closing parenthesis is encountered and the top of the stack is an
                    // opening parenthesis,
                    // remove the top of the stack
                    stack.pop();
                }
            }
        }

        // Add any indices remaining in the stack to the set of indices to be removed
        while (!stack.isEmpty()) {
            remove.add(stack.pop());
        }

        // Initialize a string builder
        final StringBuilder sb = new StringBuilder();

        // Append the characters at the indices not in the set to the string builder
        for (int i = 0; i < s.length(); i++) {
            if (!remove.contains(i)) {
                sb.append(s.charAt(i));
            }
        }

        // Return the string builder as a string
        return sb.toString();
    }
}
