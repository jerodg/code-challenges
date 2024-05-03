//! # LeetCode Problem 2441
//!
//! This module contains the solution for LeetCode problem 2441. The main function in this module is `find_max_k`,
//! which finds the maximum integer `k` such that both `-k` and `k` exist in the given array.
//!
//! # Examples
//!
//! ```
//! let nums = vec![3, 2, -2, 5, -3];
//! assert_eq!(Solution::find_max_k(nums), 3);
//! ```

impl Solution {
    /// Finds the maximum integer `k` such that both `-k` and `k` exist in the given array.
    ///
    /// This function iterates over the given array and keeps track of the positive and negative numbers it has seen.
    /// If it encounters a number `n` and `-n` has already been seen (or vice versa), it updates the maximum `k`.
    ///
    /// # Parameters
    ///
    /// * `nums: Vec<i32>` - The input array of 32-bit integers.
    ///
    /// # Returns
    ///
    /// * `i32` - Returns the maximum `k` such that both `-k` and `k` exist in the array. If no such `k` exists, it returns -1.
    ///
    /// # Errors
    ///
    /// This function does not return any errors. If the input array is empty, it simply returns -1.
    pub fn find_max_k(nums: Vec<i32>) -> i32 {
        // Boolean arrays to keep track of the positive and negative numbers we have seen
        let mut seen_neg = vec![false; 1001];
        let mut seen_pos = vec![false; 1001];

        // The maximum `k` we have found so far
        let mut max = -1;

        // Iterate over the numbers in the array
        for n in nums {
            if n > 0 {
                // If the number is positive, mark it as seen in the positive array
                seen_pos[n as usize] = true;
                // If the negative counterpart has been seen, update the maximum `k`
                if seen_neg[n as usize] {
                    max = max.max(n);
                }
            } else {
                // If the number is negative, mark it as seen in the negative array
                seen_neg[-n as usize] = true;
                // If the positive counterpart has been seen, update the maximum `k`
                if seen_pos[-n as usize] {
                    max = max.max(-n);
                }
            };
        }

        // Return the maximum `k` we have found
        max
    }
}
