import java.util.HashMap;
import java.util.HashSet;

/**
 * This class provides a solution for checking if two strings are isomorphic.
 * Two strings are isomorphic if the characters in the first string can be replaced to get the second string.
 * The problem is solved by using a hash map to keep track of the mapping from characters in the first string to characters in the second string,
 * and a hash set to keep track of the characters in the second string that have already been mapped to.
 * If a character in the first string has already been mapped to a different character in the second string, or if a character in the second string has already been mapped to,
 * the strings are not isomorphic.
 *
 * @author jerodg
 */
class Solution {

    /**
     * Checks if two strings are isomorphic.
     *
     * @param s The first input string. It is a string of characters.
     * @param t The second input string. It is a string of characters.
     *
     * @return A boolean indicating whether the two strings are isomorphic. It is true if the strings are isomorphic, and false otherwise.
     */
    public static boolean isIsomorphic(final String s, final String t) {
        // If the strings have different lengths, they are not isomorphic
        if (s.length() != t.length()) return false;

        // Initialize a hash map to keep track of the mapping from characters in the first string to characters in the second string
        final HashMap<Character, Character> map = new HashMap<>();
        // Initialize a hash set to keep track of the characters in the second string that have already been mapped to
        final HashSet<Character> set = new HashSet<>();

        // Iterate over the characters in the strings
        for (int i = 0; i < s.length(); i++) {
            final char c1 = s.charAt(i);
            final char c2 = t.charAt(i);

            // If the current character in the first string has already been mapped to a character in the second string
            if (map.containsKey(c1)) {
                // If the current character in the first string is not mapped to the current character in the second string, the strings are not isomorphic
                if (map.get(c1) != c2) return false;
            } else {
                // If the current character in the second string has already been mapped to, the strings are not isomorphic
                if (set.contains(c2)) return false;

                // Map the current character in the first string to the current character in the second string
                map.put(c1, c2);
                // Add the current character in the second string to the set of characters that have been mapped to
                set.add(c2);
            }
        }

        // If all characters in the first string can be replaced to get the second string, the strings are isomorphic
        return true;
    }
}
