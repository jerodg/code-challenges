/**
 * @file This module contains a function to find the number of wonderful substrings in a word.
 * @module leet_code/1915
 */
/**
 * Finds the number of wonderful substrings in a word.
 *
 * A wonderful string is a string where at most one letter appears an odd number of times.
 * This function uses a bitmask to keep track of the parity of the count of each letter in the word.
 * It iterates over the word, updating the bitmask and the count of each bitmask encountered.
 * It then iterates over the counts of each bitmask, adding to the result the count of the current bitmask and the counts of the bitmasks that differ from the current bitmask by one bit.
 *
 * @param {string} word - The word to search. It is expected to be a string of lowercase English letters.
 * @returns {number} The number of wonderful substrings in the word.
 *
 * @throws {TypeError} If the input is not a string of lowercase English letters.
 */
function wonderfulSubstrings(word) {
    if (typeof word !== 'string' || !/^[a-z]*$/.test(word)) {
        throw new TypeError('Input must be a string of lowercase English letters');
    }
    var maskCounts = new Array(1024).fill(0);
    var mask = (1 << 10) - 1;
    maskCounts[mask] = 1;
    var result = 0;
    for (var i = 0; i < word.length; i++) {
        var char = word.charCodeAt(i) - 'a'.charCodeAt(0);
        mask ^= (1 << char);
        result += maskCounts[mask]++;
    }
    for (var j = 0; j < maskCounts.length; j++) {
        var count = maskCounts[j];
        if (count >= 1) {
            var letterMask = 1;
            for (var letter = 0; letter < 10; letter++) {
                if (!(j & letterMask)) {
                    result += count * maskCounts[j ^ letterMask];
                }
                letterMask *= 2;
            }
        }
    }
    return result;
}
