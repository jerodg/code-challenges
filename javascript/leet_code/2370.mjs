/**
 * @fileoverview This module provides a function to calculate the longest ideal string.
 * The ideal string is defined as the longest substring where the ASCII difference between
 * any two characters is not more than `k`.
 *
 * @module leet_code/2370
 */

/**
 * Calculates the longest ideal string.
 *
 * The function uses dynamic programming to calculate the longest ideal string. It iterates
 * over each character in the string, and for each character, it calculates the maximum length
 * of the ideal string that can be formed with that character as the end character. It does this
 * by looking at the maximum length of the ideal string for all characters within `k` ASCII values
 * of the current character, and adding 1 to the maximum of these lengths.
 *
 * @param {string} s - The input string. It is expected to be a string of ASCII characters.
 * @param {number} k - The maximum ASCII difference between any two characters in an ideal string.
 * It is expected to be a non-negative integer.
 *
 * @returns {number} The length of the longest ideal string in `s` where the ASCII difference
 * between any two characters is not more than `k`.
 *
 * @throws {TypeError} If `s` is not a string or `k` is not a number, the function will throw a TypeError.
 */
const longestIdealString = function (s, k) {
    if (typeof s !== 'string' || typeof k !== 'number') {
        throw new TypeError('Invalid input types. Expected a string and a number.');
    }

    // Initialize the dynamic programming array with zeros.
    let dp = new Array(128).fill(0);
    let maxLen = 0;

    // Iterate over each character in the string.
    for (let char of s) {
        let ascii = char.charCodeAt(0);
        let maxForChar = 0;

        // For each character, calculate the maximum length of the ideal string that can be formed
        // with that character as the end character.
        for (let i = Math.max(0, ascii - k); i <= Math.min(127, ascii + k); i++) {
            maxForChar = Math.max(maxForChar, dp[i]);
        }

        // Update the dynamic programming array and the maximum length.
        dp[ascii] = maxForChar + 1;
        maxLen = Math.max(maxLen, dp[ascii]);
    }

    // Return the maximum length.
    return maxLen;
};
