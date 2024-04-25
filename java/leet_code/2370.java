/**
 * This module is part of a leet code solution. It contains a single class, Solution, which
 * provides a method to find the longest ideal string given a character sequence and an integer.
 * The method uses dynamic programming to solve the problem.
 */
class Solution {

    /**
     * This method calculates the longest ideal string from a given character sequence.
     * An ideal string is defined as a string where the ASCII value difference between any two characters is not more than k.
     *
     * @param s The input character sequence. It is expected to be a non-null CharSequence.
     * @param k The maximum allowed ASCII value difference between any two characters in an ideal string. It is expected to be an integer.
     *
     * @return The length of the longest ideal string that can be formed from the input character sequence. The return type is an integer.
     */
    public static int longestIdealString(final CharSequence s, final int k) {

        // dp array to store the longest ideal string ending at each character in the alphabet
        final int[] dp = new int[27];
        final int n = s.length();

        // Iterate over the character sequence in reverse
        for (int i = n - 1; 0 <= i; i--) {
            final char cc = s.charAt(i);
            // Convert the character to its corresponding index in the dp array
            final int idx = (int) cc - 97;
            int max = Integer.MIN_VALUE;

            // Calculate the range of characters that can be included in the ideal string
            final int left = Math.max((idx - k), 0);
            final int right = Math.min((idx + k), 26);

            // Find the maximum length of an ideal string ending at a character within the range
            for (int j = left; j <= right; j++) {
                max = Math.max(max, dp[j]);
            }

            // Update the dp array with the maximum length of an ideal string ending at the current character
            dp[idx] = max + 1;
        }

        int max = Integer.MIN_VALUE;

        // Find the maximum length of an ideal string from the dp array
        for (final int ele : dp) {
            max = Math.max(ele, max);
        }
        return max;
    }
}
