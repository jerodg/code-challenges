// Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>
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
// program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

//! This module contains the implementation of the `num_rescue_boats` function, which calculates
//! the minimum number of rescue boats required to save all people.

use std::collections::HashMap;

/// `Solution` is a struct that provides a solution to a given problem.
impl Solution {
    /// Calculates the minimum number of rescue boats required to save all people.
    ///
    /// # Arguments
    ///
    /// * `people` - A vector of weights of the people.
    /// * `limit` - The maximum weight that a boat can carry.
    ///
    /// # Returns
    ///
    /// * The minimum number of boats required to save all people.
    ///
    /// # Example
    ///
    /// ```
    /// let people = vec![1, 2];
    /// let limit = 3;
    /// let result = Solution::num_rescue_boats(people, limit);
    /// assert_eq!(result, 1);
    /// ```
    pub fn num_rescue_boats(people: Vec<i32>, limit: i32) -> i32 {
        let limit = limit as usize;
        let mut counts = HashMap::new();
        let mut n_boats = 0;

        let mut min = usize::MAX;
        let mut max = 0;

        // Count the number of people with each weight and find the minimum and maximum weights.
        for p in people {
            *counts.entry(p as usize).or_insert(0) += 1;
            min = min.min(p as usize);
            max = max.max(p as usize);
        }

        let mut i = min;
        let mut j = max;

        // Iterate over the weights from both ends.
        while i < j {
            // Find the next weight from the left that has a non-zero count.
            while i < j && *counts.get(&i).unwrap_or(&0) == 0 { i += 1; }
            // Find the next weight from the right that has a non-zero count.
            while i < j && *counts.get(&j).unwrap_or(&0) == 0 { j -= 1; }

            // If the sum of the weights is less than or equal to the limit, decrement the count of
            // the left weight.
            if i < j {
                if i + j <= limit {
                    *counts.get_mut(&i).unwrap() -= 1;
                }
                // Decrement the count of the right weight and increment the number of boats.
                *counts.get_mut(&j).unwrap() -= 1;
                n_boats += 1;
            }
        }
        // If the double of the remaining weight is less than or equal to the limit, add half of the
        // count to the number of boats.
        // Otherwise, add the count to the number of boats.
        if i + i <= limit {
            n_boats + ((*counts.get(&i).unwrap_or(&0) + 1) / 2) as i32
        } else {
            n_boats + *counts.get(&i).unwrap_or(&0) as i32
        }
    }
}
