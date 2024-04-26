/**
 * @file 2370.cpp
 * @brief This file contains the Solution class which provides a method to find the longest ideal string.
 * @author jerodg
 * @version 1.0
 * @date 2024-1-1
 */

#include <string>

/**
 * @class Solution
 * @brief This class provides a method to find the longest ideal string.
 */
class Solution {
public:
    /**
     * @brief This method finds the longest ideal string.
     *
     * The method uses dynamic programming to find the longest ideal string. It iterates over the input string in reverse order,
     * and for each character, it calculates the maximum length of the ideal string that can be formed using this character as the
     * last character. It does this by checking the lengths of the ideal strings that can be formed using the characters within the
     * range [idx - k, idx + k] (where idx is the index of the current character in the alphabet) as the last character, and
     * choosing the maximum. The result is the maximum length among all characters.
     *
     * @param s The input string. It is a const reference to a std::string. It should only contain lowercase English letters.
     * @param k The maximum difference in the alphabetical index between two consecutive characters in an ideal string. It is an integer.
     * @return The length of the longest ideal string that can be formed from the input string. It is an integer.
     */
    static int longestIdealString(const std::string &s, const int k) {
        // dp[i] stores the maximum length of the ideal string that can be formed using the character with index i as the last character.
        int dp[27] = {0};
        const int n = s.length();

        // Iterate over the input string in reverse order.
        for (int i = n - 1; i >= 0; i--) {
            const char cc = s[i];
            const int idx = cc - 'a';
            int maxi = -__INT_MAX__;

            // Calculate the range [left, right] within which the index of the last character of the ideal string can be.
            const int left = std::max((idx - k), 0);
            const int right = std::min((idx + k), 26);

            // Find the maximum length of the ideal string that can be formed using the characters within the range [left, right] as the last character.
            for (int j = left; j <= right; j++) {
                maxi = std::max(maxi, dp[j]);
            }

            // Update dp[idx] with the maximum length of the ideal string that can be formed using the character with index idx as the last character.
            dp[idx] = maxi + 1;
        }

        // Find the maximum length among all characters.
        int max = -__INT_MAX__;
        for (const int i: dp) {
            if (i > max)
                max = i;
        }

        return max;
    }
};
