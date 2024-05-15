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
// `leet_code` is a package that contains solutions for problems from LeetCode.
//
// This file, `861.rs`, contains the solution for LeetCode problem 861, "Score After Flipping Matrix".

/// `Solution` is a struct that is used to encapsulate the solution for LeetCode problem 861.
pub struct Solution;

impl Solution {
    /// `matrix_score` is a method on the `Solution` struct that calculates the maximum possible score
    /// after flipping the binary matrix.
    ///
    /// # Parameters
    ///
    /// * `grid` - A mutable 2D vector of integers representing the binary matrix.
    ///
    /// # Returns
    ///
    /// * An integer representing the maximum possible score after flipping the binary matrix.
    ///
    /// # Examples
    ///
    /// ```
    /// let mut grid = vec![vec![0, 0, 1, 1], vec![1, 0, 1, 0], vec![1, 1, 0, 0]];
    /// assert_eq!(Solution::matrix_score(grid), 39);
    /// ```
    pub fn matrix_score(mut grid: Vec<Vec<i32>>) -> i32 {
        // `m` is the number of rows in the matrix.
        let m = grid.len();
        // `n` is the number of columns in the matrix.
        let n = grid[0].len();
        // `res` is the initial score, calculated by shifting 1 `n - 1` places to the left and multiplying by `m`.
        let mut res = (1 << (n - 1)) * m as i32;
        for j in 1..n {
            // `same` is the count of elements in the current column that are the same as the first column.
            let mut same = 0;
            for i in 0..m {
                if grid[i][0] == grid[i][j] {
                    same += 1;
                }
            }
            // `diff` is the count of elements in the current column that are different from the first column.
            let diff = m - same;
            // Update `res` by adding the maximum of `same` and `diff`, shifted `n - 1 - j` places to the left.
            res += (1 << (n - 1 - j)) * std::cmp::max(same, diff) as i32;
        }
        // Return the final score.
        res
    }
}
