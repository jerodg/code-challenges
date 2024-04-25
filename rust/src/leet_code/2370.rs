//! # LeetCode Problem 2370
//!
//! This module contains the solution for LeetCode problem 2370. The problem is about finding the longest ideal string.
//! The function `longest_ideal_string` takes a string and an integer as input and returns the length of the longest ideal string.
//! An ideal string is defined as a string where the difference between the ASCII values of any two characters is less than or equal to `k`.
//! The function uses dynamic programming to solve the problem.

impl Solution {
    /// Finds the length of the longest ideal string.
    ///
    /// # Parameters
    ///
    /// * `s` - A string consisting of lowercase English letters.
    /// * `k` - An integer representing the maximum allowed difference between the ASCII values of any two characters in an ideal string.
    ///
    /// # Returns
    ///
    /// * An integer representing the length of the longest ideal string.
    ///
    /// # Errors
    ///
    /// This function will panic if the string `s` is empty.
    pub fn longest_ideal_string(s: String, k: i32) -> i32 {
        // Convert the string into bytes for easier manipulation
        let s = s.as_bytes();
        // Initialize a memoization array to store the maximum length of the ideal string ending at each character
        let mut memo = [0_u32; 26];

        // Iterate over the characters in the string in reverse order
        for cur_c in s.into_iter().rev().map(|c| (c - b'a') as usize) {
            // Calculate the range of characters that can be included in the ideal string ending at the current character
            let min_c = if cur_c as i32 - k >= 0 {
                cur_c - k as usize
            } else {
                0
            };
            let max_c = if cur_c as i32 + k <= 25 {
                cur_c + k as usize
            } else {
                25
            };
            // Initialize the maximum length of the ideal string ending at the current character
            let mut max_sequence: u32 = 0;
            // Find the maximum length of the ideal string ending at a character within the range
            for i in min_c..=max_c {
                max_sequence = max_sequence.max(memo[i]);
            }
            // Update the memoization array
            memo[cur_c] = max_sequence + 1;
        }
        // Return the maximum length of the ideal string
        memo.into_iter().max().unwrap() as i32
    }
}
