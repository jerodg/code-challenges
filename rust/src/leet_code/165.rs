//! # LeetCode Problem 165
//!
//! This module contains the solution for LeetCode problem 165: Compare Version Numbers.
//! The main function in this module is `compare_version`, which compares two version numbers.
//!
//! # Examples
//!
//! ```
//! let v1 = "1.0.1".to_string();
//! let v2 = "1".to_string();
//! assert_eq!(Solution::compare_version(v1, v2), 1);
//! ```

impl Solution {
    /// Compares two version numbers.
    ///
    /// This function takes two version numbers as strings, splits them by the dot character,
    /// and compares each corresponding pair of version parts. If one version has more parts
    /// than the other, the missing parts are considered as zero.
    ///
    /// # Parameters
    ///
    /// * `v1: String` - The first version number as a string.
    /// * `v2: String` - The second version number as a string.
    ///
    /// # Returns
    ///
    /// * `i32` - Returns 1 if the first version number is greater than the second, -1 if the
    /// first version number is less than the second, and 0 if both version numbers are equal.
    ///
    /// # Errors
    ///
    /// This function will panic if the version strings contain non-numeric characters.
    pub fn compare_version(v1: String, v2: String) -> i32 {
        // Split the version strings by the dot character
        let mut rev_strings1 = v1.split('.');
        let mut rev_strings2 = v2.split('.');

        // Function to parse a version part string to an integer
        let parse_rev = |rev_str: &str| rev_str.parse().unwrap();

        loop {
            match (rev_strings1.next(), rev_strings2.next()) {
                // If both version strings have no more parts, the versions are equal
                (None, None) => return 0,
                (rev_str1, rev_str2) => {
                    // Parse the version parts to integers, or use 0 if a version has no more parts
                    let rev1 = rev_str1.map_or(0, parse_rev);
                    let rev2 = rev_str2.map_or(0, parse_rev);

                    // If the first version part is greater than the second, the first version is greater
                    if rev1 > rev2 {
                        return 1;
                    }

                    // If the first version part is less than the second, the first version is less
                    if rev1 < rev2 {
                        return -1;
                    }
                }
            }
        }
    }
}
