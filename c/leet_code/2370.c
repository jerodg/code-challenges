/**
 * @file leet_code/2370.c
 * @brief This module contains the implementation of the longestIdealString function.
 *
 * The function calculates the longest ideal string based on the given string and an integer.
 * An ideal string is defined as a string where the difference between the ASCII values of any two characters is less than or equal to k.
 */

#include <string.h>

/**
 * @brief Calculates the longest ideal string.
 *
 * This function uses dynamic programming to calculate the longest ideal string.
 * It iterates over the string from the end to the beginning, and for each character, it calculates the maximum length of the ideal string that can be formed.
 *
 * @param s The input string. It is a pointer to a constant character.
 * @param k The maximum allowed difference between the ASCII values of any two characters in the ideal string.
 * @return The length of the longest ideal string. The return type is int.
 */
int longestIdealString(const char *s, const int k) {
    int dp[27] = {0}; // Dynamic programming array to store the maximum length of the ideal string for each character.
    const int n = strlen(s); // The length of the input string.

    // Iterate over the string from the end to the beginning.
    for (int i = n - 1; i >= 0; i--) {
        const char cc = s[i]; // The current character.
        const int idx = cc - 'a'; // The index of the current character in the dynamic programming array.
        int maxi = -__INT_MAX__; // The maximum length of the ideal string that can be formed with the current character.

        // Calculate the range of characters that can be used to form the ideal string with the current character.
        const int left = (idx - k) > 0 ? (idx - k) : 0;
        const int right = (idx + k) < 26 ? (idx + k) : 26;

        // Find the maximum length of the ideal string that can be formed with the current character.
        for (int j = left; j <= right; j++) {
            maxi = maxi > dp[j] ? maxi : dp[j];
        }

        // Update the dynamic programming array.
        dp[idx] = maxi + 1;
    }

    // Find the maximum length of the ideal string.
    int max = -__INT_MAX__;
    for (int i = 0; i < 27; i++) {
        if (dp[i] > max)
            max = dp[i];
    }

    return max; // Return the maximum length of the ideal string.
}
