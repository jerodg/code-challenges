/**
 * @fileoverview This module provides a function to calculate the longest ideal string.
 * The function takes a string and a number as input and returns the length of the longest ideal string.
 * An ideal string is defined as a string where the ASCII difference between any two characters is less than or equal to k.
 */
/**
 * Calculates the length of the longest ideal string.
 *
 * @param {string} s - The input string. It should only contain lowercase English letters.
 * @param {number} k - The maximum ASCII difference allowed between any two characters in an ideal string.
 *
 * @returns {number} The length of the longest ideal string that can be formed from the input string.
 *
 * @throws {TypeError} If the input parameters are not of the expected types.
 */
function longestIdealString(s, k) {
    if (typeof s !== 'string' || typeof k !== 'number') {
        throw new TypeError('Invalid input types. Expected a string and a number.');
    }
    // Initialize an array to keep track of the longest ideal string ending with each character.
    var dp = Array(26).fill(0);
    var codeA = 'a'.charCodeAt(0);
    var max = 0;
    // Iterate over the input string.
    for (var i = 0, n = s.length; i < n; i++) {
        // Calculate the ASCII code of the current character relative to 'a'.
        var code = s.charCodeAt(i) - codeA;
        var best = 0;
        // Find the longest ideal string ending with a character whose ASCII code is within k of the current character's ASCII code.
        for (var j = Math.max(code - k, 0), m = Math.min(code + k, 25); j <= m; j++) {
            if (dp[j] > best) {
                best = dp[j];
            }
        }
        // If the longest ideal string found is longer than the current longest ideal string ending with the current character, update it.
        if (best >= dp[code]) {
            dp[code] = best + 1;
            if (best >= max) {
                max = best + 1;
            }
        }
    }
    // Return the length of the longest ideal string.
    return max;
}
