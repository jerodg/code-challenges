//! # LeetCode Problem 1915
//!
//! This module contains the solution for LeetCode problem 1915. The problem is about finding the
//! number of wonderful substrings. A wonderful string is a string where at most one letter appears
//! an odd number of times. The function `wonderful_substrings` takes a string as input and returns
//! the number of wonderful substrings. The function uses bitwise operations to solve the problem.
//! The time complexity for the provided Rust code is as follows:
//!
//! - Best Case: O(n), where n is the length of the string `word`. This is because even in the
//! best case, the function needs to iterate over each character in the string at least once.
//!
//! - Average Case: O(n), where n is the length of the string `word`. The function iterates over
//! each character in the string exactly once. The operations inside the loop (calculating the index
//! of the current character, updating the prefix XOR, and adding the number of substrings with the
//! same prefix XOR to the result) all take constant time.
//!
//! - Worst Case: O(n), where n is the length of the string `word`. Even in the worst case, the
//! function still needs to iterate over each character in the string once. The operations inside
//! the loop do not change based on the input, so they always take constant time.
//!
//! The space complexity of the function is O(1). This is because the size of the count vector is
//! fixed at 1024, which does not depend on the size of the input string `word`, so the space
//! complexity is constant.

impl Solution {
    /// Finds the number of wonderful substrings.
    ///
    /// # Parameters
    ///
    /// * `word` - A string consisting of lowercase English letters.
    ///
    /// # Returns
    ///
    /// * A 64-bit integer representing the number of wonderful substrings.
    ///
    /// # Errors
    ///
    /// This function will panic if the string `word` is empty.
    pub fn wonderful_substrings(word: String) -> i64 {
        // Initialize the result to 0
        let mut result: i64 = 0;
        // Initialize a vector to count the number of substrings with a certain prefix XOR
        let mut count = vec![0; 1024];
        // There is one substring (the empty string) with a prefix XOR of 0
        count[0] = 1;
        // Initialize the prefix XOR to 0
        let mut prefix_xor = 0;

        // Iterate over the characters in the word
        for c in word.chars() {
            // Calculate the index of the current character in the alphabet
            let idx = (c as u8 - b'a') as usize;
            // Update the prefix XOR
            prefix_xor ^= 1 << idx;
            // Add the number of substrings with the same prefix XOR to the result
            result += count[prefix_xor];

            // Iterate over the first 10 bits of the prefix XOR
            for i in 0..10 {
                // Add the number of substrings with a prefix XOR that differs in exactly one bit to the result
                result += count[prefix_xor ^ (1 << i)];
            }
            // Increment the count of substrings with the current prefix XOR
            count[prefix_xor] += 1;
        }
        // Return the number of wonderful substrings
        result
    }
}
