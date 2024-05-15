// Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
//
// This program is free software: you can redistribute it and/or modify it under the terms of the
// Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
// or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
// even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
// for more details.
//
// The above copyright notice and this permission notice shall be included in all copies or
// substantial portions of the Software. You should have received a copy of the SSPL along with this
// program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.

// Package leet_code
//
// This file contains the implementation of the Solution struct and its associated methods.
// The main method in this file is `maximum_happiness_sum` which calculates the maximum happiness sum.

use std::collections::BinaryHeap;
use std::cmp::Reverse;

/// The Solution struct does not hold any data and is only used to group related methods.
pub struct Solution {}

impl Solution {
    /// This method calculates the maximum happiness sum from a given list of happiness values and a limit.
    ///
    /// # Parameters
    ///
    /// * `happiness`: A vector of happiness values.
    /// * `k`: The limit on the number of values to consider.
    ///
    /// # Returns
    ///
    /// The maximum happiness sum as a 64-bit integer.
    ///
    /// # Example
    ///
    /// ```
    /// let happiness = vec![1, 2, 3, 5];
    /// let k = 3;
    /// let result = Solution::maximum_happiness_sum(happiness, k);
    /// assert_eq!(result, 10);
    /// ```
    pub fn maximum_happiness_sum(mut happiness: Vec<i32>, k: i32) -> i64 {
        // The length of the happiness vector
        let n = happiness.len();
        // The limit as a usize
        let k = k as usize;
        // The top k+1 happiness values if k+1 is less than the length of the happiness vector
        let top_k = if k + 1 < happiness.len() {
            happiness.select_nth_unstable(n - k - 1).2
        } else {
            happiness.as_mut_slice()
        };
        // Sort the top k+1 happiness values in unstable order
        top_k.sort_unstable();

        // Calculate the maximum happiness sum
        (0..).zip(top_k.iter().copied().rev())
            .take_while(|&(penalty, unpenalized)| penalty < unpenalized)
            .take(k as usize)
            .map(|(penalty, unpenalized)| (unpenalized - penalty) as i64)
            .sum()
    }
}
