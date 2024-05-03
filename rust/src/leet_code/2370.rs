//! # LeetCode Problem 2370
//!
//! This module contains the solution for LeetCode problem 2370. The problem is about finding the
//! longest ideal string. The function `longest_ideal_string` takes a string and an integer as input
//! and returns the length of the longest ideal string. An ideal string is defined as a string where
//! the difference between the ASCII values of any two characters is less than or equal to `k`.
//! The function uses dynamic programming to solve the problem.
//!
//! The time and space complexity for the provided Rust code are as follows:
//!
//! Time Complexity:
//! - Best Case: O(n), where n is the length of the string `s`. This is because even in the best
//! case, the function needs to iterate over each character in the string at least once.
//!
//! - Average Case: O(n), where n is the length of the string `s`. The function iterates over
//! each character in the string exactly once. The operations inside the loop (calculating the range
//! of characters, finding the maximum length of the ideal string within the range, and updating the
//! memoization array) all take constant time.
//!
//! - Worst Case: O(n), where n is the length of the string `s`. Even in the worst case, the
//! function still needs to iterate over each character in the string once. The operations inside
//! the loop do not change based on the input, so they always take constant time.
//!
//! Space Complexity:
//! The space complexity of the function is O(1). This is because the size of the memoization
//! array is fixed at 26, which corresponds to the number of lowercase English letters. The size of
//! the array does not depend on the size of the input string `s`, so the space complexity is constant.

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
