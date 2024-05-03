/**
 * This class provides a solution for finding the number of wonderful substrings in a given word.
 * A wonderful string is a string where at most one character appears an odd number of times.
 *
 * <p>It uses bitwise operations to keep track of the frequency of characters in the string.
 * The frequency of each character is stored in a binary format where each bit represents a character from 'a' to 'j'.
 * If a bit is set, it means the corresponding character appears an odd number of times, otherwise it appears an even number of times.
 *
 * <p>The class is implemented in Java and adheres to Java 21 syntax.
 */
class Solution {
    // The maximum number of characters
    private static final int CHAR_MAX = 10;

    /**
     * Calculates the number of wonderful substrings in a given word.
     *
     * @param word The input string. It is expected to be a non-null string consisting of lowercase English letters from 'a' to 'j'.
     *
     * @return The number of wonderful substrings in the input word. The return type is long.
     *
     *         <p>This method does not handle errors as it assumes the input is always valid.
     */
    public static long wonderfulSubstrings(final String word) {
        // An array to store the frequency of each combination of characters
        final int[] counts = new int[1 << Solution.CHAR_MAX];

        // Initialize the frequency of the empty string
        counts[0] = 1;

        // Initialize the count of wonderful substrings
        long wonderfulCount = 0;

        // The binary representation of the frequency of characters in the current substring
        int mask = 0;

        // Convert the input word to an array of bytes
        final byte[] wordc = new byte[word.length()];
        word.getBytes(0, word.length(), wordc, 0);

        // Iterate over each character in the word
        for (final int c : wordc) {
            // Update the frequency of the current character and the frequency of the current combination of characters
            counts[mask ^= 1 << (c - 'a')]++;
        }

        // Iterate over each possible combination of characters
        for (int msk = (1 << Solution.CHAR_MAX) - 1; msk >= 0; msk--) {
            // If the current combination of characters appears in the word
            if (counts[msk] != 0) {
                // The frequency of the current combination of characters
                final long cntAtMsk = counts[msk];

                // Add the number of substrings where all characters appear an even number of times
                wonderfulCount += ((cntAtMsk - 1) * cntAtMsk) / 2;

                // Iterate over each possible character
                for (int bit = 1; bit <= msk; bit <<= 1)
                    // If the current character appears an odd number of times in the current combination of characters
                    if (0 != (msk & bit))
                        // Add the number of substrings where exactly one character appears an odd number of times
                        wonderfulCount += counts[msk ^ bit] * cntAtMsk;
            }
        }

        // Return the number of wonderful substrings
        return wonderfulCount;
    }
}
