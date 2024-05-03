/**
 * @fileoverview This module provides a function to count the number of 'wonderful' substrings in a word.
 * A 'wonderful' substring is defined as a substring where no more than one character appears an odd number of times.
 * The function uses a bitmask to keep track of the parity of the character counts and a frequency array to store the number of times each bitmask value has been encountered.
 */

/**
 * Counts the number of 'wonderful' substrings in a word.
 *
 * @param {string} word - The word to find 'wonderful' substrings in.
 * @returns {number} - The number of 'wonderful' substrings in the word.
 */
const wonderfulSubstrings = function (word) {
    // Initialize the count of 'wonderful' substrings
    let count = 0;

    // Initialize the frequency array with a size of 1024 (2^10) to cover all possible bitmask values
    const freq = new Array(1024).fill(0);

    // The bitmask value of 0 has been encountered once at the start
    freq[0] = 1;

    // Initialize the bitmask
    let mask = 0;

    // Iterate over the characters in the word
    for (let i = 0; i < word.length; i++) {
        // Get the index of the current character in the bitmask
        const charIndex = word.charCodeAt(i) - 97;

        // Toggle the bit at the current character's index in the bitmask
        mask ^= (1 << charIndex);

        // Add the frequency of the current bitmask value to the count
        count += freq[mask];

        // Check all possible bitmasks with one bit different from the current bitmask
        for (let j = 0; j < 10; j++) {
            // Add the frequency of the bitmask with one bit different to the count
            count += freq[mask ^ (1 << j)];
        }

        // Increment the frequency of the current bitmask value
        freq[mask]++;
    }

    // Return the count of 'wonderful' substrings
    return count;
};
